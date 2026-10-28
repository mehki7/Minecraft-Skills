#!/usr/bin/env python3
"""
RECON/02-mine-mixin-targets.py

Resolves the one blocking UNVERIFIED item in TARGET.md: which vanilla
Minecraft class/method each of Lunar's mixin classes actually patches.

Run this from a local agent with real file access to your Lunar install
(do NOT try to do this by hand in cmd + notepad — that's what this script
replaces).

What it does, for every mixin class listed in a given mixins.*.json config:
  1. Extracts the .class file from the jar
  2. Runs `javap -p -v` on it
  3. Parses the @Mixin annotation's "value"/target class reference out of
     the constant pool
  4. Writes a markdown table to RECON/04-name-map-output.md with the raw
     javap evidence for each row, or marks it "unresolved" if parsing fails

Usage:
    python 02-mine-mixin-targets.py <path-to-jar> <mixin-config.json> [output.md]

Example:
    python 02-mine-mixin-targets.py ^
        C:\\Users\\marckie\\.lunarclient\\offline\\multiver\\legacy-0.1.0-SNAPSHOT-all-nomappings.jar ^
        mixins.legacy_forge_v1_8.json ^
        RECON\\04-name-map-output.md
"""

import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def load_mixin_config(jar_path: Path, config_name: str) -> dict:
    with zipfile.ZipFile(jar_path) as zf:
        with zf.open(config_name) as f:
            return json.load(f)


def class_entry_path(package: str, mixin_name: str) -> str:
    # mixin_name may itself contain dots for nested classes, e.g.
    # "IOOC....IOOC....RHOIC" -> nested inner classes separated by '.'
    fq = f"{package}.{mixin_name}"
    return fq.replace(".", "/") + ".class"


def extract_class(jar_path: Path, entry: str, dest_dir: Path) -> Path:
    with zipfile.ZipFile(jar_path) as zf:
        data = zf.read(entry)
    out = dest_dir / Path(entry).name
    out.write_bytes(data)
    return out


def run_javap(class_file: Path) -> str:
    result = subprocess.run(
        ["javap", "-p", "-v", str(class_file)],
        capture_output=True,
        text=True,
    )
    return result.stdout + "\n" + result.stderr


MIXIN_ANNOTATION = "Lorg/spongepowered/asm/mixin/Mixin;"


def find_mixin_target(javap_output: str) -> list[str]:
    """
    Pulls class names referenced near the @Mixin annotation in the constant
    pool dump. This is a heuristic (javap's verbose dump doesn't cleanly
    label "this is the mixin target"), so always keep the raw output too —
    don't trust this list blindly, eyeball it.
    """
    if MIXIN_ANNOTATION not in javap_output:
        return []
    # Grab every class-looking constant pool entry near the annotation block.
    # ConstantPool entries referencing classes look like:
    #   #12 = Class   #34  // some/package/ClassName
    candidates = re.findall(r"// ([A-Za-z0-9_$]+(?:/[A-Za-z0-9_$]+)+)", javap_output)
    # Filter out obvious library/JDK noise, keep anything that isn't
    # java/..., org/spongepowered/... etc.
    filtered = [
        c for c in candidates
        if not c.startswith("java/")
        and not c.startswith("org/spongepowered/")
        and not c.startswith("com/moonsworth/lunar")  # exclude self-refs
    ]
    # de-dupe, preserve order
    seen = []
    for c in filtered:
        if c not in seen:
            seen.append(c)
    return seen


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    jar_path = Path(sys.argv[1])
    config_name = sys.argv[2]
    out_path = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("RECON/04-name-map-output.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    config = load_mixin_config(jar_path, config_name)
    package = config["package"]
    mixins = config["mixins"]

    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for mixin_name in mixins:
            entry = class_entry_path(package, mixin_name)
            try:
                class_file = extract_class(jar_path, entry, tmp_dir)
            except KeyError:
                rows.append((mixin_name, "UNRESOLVED", "entry not found in jar: " + entry))
                continue

            javap_out = run_javap(class_file)
            targets = find_mixin_target(javap_out)
            evidence = "\n".join(targets) if targets else "UNRESOLVED (see raw dump)"
            rows.append((mixin_name, evidence, javap_out[:2000]))

    with out_path.open("w", encoding="utf-8") as f:
        f.write(f"# RECON output — {config_name}\n\n")
        f.write(f"Source jar: `{jar_path}`\n\n")
        f.write(f"Package: `{package}`\n\n")
        f.write("| Mixin class | Candidate target class(es) |\n")
        f.write("|---|---|\n")
        for name, targets, _ in rows:
            short_targets = targets.replace("\n", "<br>")
            f.write(f"| `{name}` | {short_targets} |\n")
        f.write("\n\n## Raw javap evidence (first 2000 chars per class)\n\n")
        for name, _, raw in rows:
            f.write(f"### {name}\n\n```\n{raw}\n```\n\n")

    print(f"Wrote {len(rows)} rows to {out_path}")
    print("Candidate targets are a heuristic guess from the constant pool —")
    print("always check the raw javap evidence in the output file before")
    print("trusting a row, then move it from LIKELY to VERIFIED in TARGET.md.")


if __name__ == "__main__":
    main()
