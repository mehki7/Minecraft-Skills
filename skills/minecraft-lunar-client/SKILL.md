name: minecraft-lunar-client
description: Port or patch client-side Minecraft mods onto Lunar Client's own closed, Mixin-based 1.7/1.8/1.12 "legacy" bundle (not Forge, not Fabric). Use when the target is Lunar Client specifically, its offline/multiver jars, or porting a Forge mod to run inside Lunar. Do not use for ordinary Forge or Fabric modding with no Lunar involvement — use minecraft-legacy-modding-189 or the main minecraft-modding skill for that.
---

# Lunar Client (legacy, 1.7/1.8/1.12 lane) modding

Lunar Client is not a mod loader. It is a complete closed client with its
own classloader and its own bundled, ProGuard-obfuscated game jars. There
is no `@Mod`, no event bus, no registry API, no FML lifecycle inside it.
The only way in is Mixin, patched directly onto Lunar's classes.

Always read [TARGET.md](../../TARGET.md) first. It is the single source of
truth for what's actually confirmed on the pinned build vs still a guess.
Never assert something from this file that TARGET.md marks UNVERIFIED.

---

## Step 0 — Smoke test (mandatory before writing any real mixin code)

Before writing a single line of real mod code, confirm the pipeline works
on your specific machine and Lunar build.

**Canonical build example:** `Example Mod for 1.8/smoketest/` — not the
Kotlin Architectury Loom template in `Example Mod for 1.8/Example-1.8.9-Mod/`
(that template uses a different build system and implies FML exists; see
`Example Mod for 1.8/README-EXAMPLE.md`).

1. Build `smoketest.jar` (source in `Example Mod for 1.8/smoketest/`) with:

javac -proc:none -cp FuriahVisuals.jar -d classes SmokePlugin.java MixinEntityRendererSmoke.java
jar cfm smoketest.jar META-INF\MANIFEST.MF -C classes . mixins.smoketest.json mcmod.info


2. Drop it in `.lunarclient\profiles\<your-profile>\mods\`.
3. Launch, load a world, quit.
4. `findstr "SMOKETEST" latest.log` — you need BOTH lines:
   - `*** SMOKE TEST PASS -- plugin onLoad fired ***`
   - `*** INJECT PASS -- updateLightmap HEAD fired ***`

If either line is missing, stop and debug before writing real code — see
the Debugging section below.

---

## What's actually there (confirmed structure)

The 1.7/1.8/1.12 "legacy" lane ships as two jars in
`.lunarclient/offline/multiver/`:

- `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` — the actual mixin classes.
  Bundles three separate version lanes in one jar:
  - `com.moonsworth.lunar.v1_7.optifine.mixin`
  - `com.moonsworth.lunar.v1_8.forge.mixin`
  - `com.moonsworth.lunar.v1_8.optifine.mixin`
  - `com.moonsworth.lunar.v1_12.forge.mixin`
  - `com.moonsworth.lunar.legacy.optifine.mixin`
- `lunar-platform-mappings-v1_8.jar` — presumed mapping data. Contents
  not yet inventoried — see TARGET.md LIKELY section.

Mixin configs bundled in the legacy jar for 1.8:
`mixins.legacy_forge_v1_8.json`, `mixins.legacy_lunar_v1_8.json`,
`mixins.legacy_optifine_v1_8.json`, `mixins.legacy_bridge_v1_8.json`,
and `_combined` variants.

Every config inspected declares:
- `"compatibilityLevel": "JAVA_17"` — Lunar's own code targets Java 17.
  External mod jars compiled at Java 8 load fine alongside these
  (confirmed by smoke test).
- `"minVersion": "0.8"` for Mixin.
- No `"refmap"` key — direct name matching, no remap step.

---

## External mods — VERIFIED (2026-10-29)

**Confirmed drop-in folder:**

C:\Users<you>.lunarclient\profiles<profile-name>\mods\


Drop a `.jar` there. No launch arguments, no config, no registration.
Lunar's 1.8.9 lane picks it up automatically.

Evidence: `smoketest.jar` (unknown, unsigned, not on any approved list)
dropped in `.lunarclient\profiles\1.8-furiahvisuals\mods\` →
`onLoad` fired at `[17:53:16]`, inject fired at `[19:32:19]`. An
"approved mods" list in the launcher UI is a convenience filter, not a
security gate — unknown jars load anyway.

**Required MANIFEST.MF** (trailing blank line, no trailing spaces):

Manifest-Version: 1.0
FMLCorePluginContainsFMLMod: true
ForceLoadAsMod: true
TweakClass: org.spongepowered.asm.launch.MixinTweaker
TweakOrder: 0
MixinConfigs: mixins.<yourmod>.json


`MixinConfigs` in the manifest is the sole confirmed loading mechanism.
Zero JVM launch arguments needed.

---

## Obfuscation and name resolution

### What is and isn't obfuscated

**Lunar's own classes** (`com.moonsworth.lunar.*`): ProGuard-obfuscated
to random uppercase letter sequences (e.g. `IOOCCRIRHHROHIHRCHHRRIOICHIOIR`).
No human-readable name anywhere in the shipped jar.

**Vanilla Minecraft classes**: class names are NOT renamed by Ichor.
`net.minecraft.client.renderer.EntityRenderer` is `net.minecraft.client.renderer.EntityRenderer`
at runtime (confirmed by tsrg: same name both sides, and by live inject).

**Vanilla Minecraft methods and fields**: Ichor remaps these to **Searge
names** (e.g. `func_78472_g`, `field_74333_Y`) BEFORE Mixin runs. This
is the critical discovery from the smoke test:
- `@Inject(method = "updateLightmap", remap = false)` → silent failure
- `@Inject(method = "func_78472_g", remap = false)` → fires correctly

### How to find Searge names

**Primary source:** `lunar2searge.tsrg` at
`C:\Users\<you>\AppData\Roaming\.minecraft\.ichor\lunar2searge.tsrg`
(6 MB). Query with `findstr "methodName" lunar2searge.tsrg` — output
format: `    MCPname (descriptor) SeargeName`.

**Pre-resolved names:** TARGET.md's Runtime Name Table has 21 confirmed
entries with raw tsrg evidence quoted. Use those directly — no RECON
needed for those specific names.

**For new names not in the table:** query the tsrg, paste the output,
record it in TARGET.md before using the name in any mixin annotation.

### `lunar-platform-mappings-v1_8.jar`

Presumed (not yet confirmed) to hold the mapping table that lets Lunar's
crash reporter retrace obfuscated `com.moonsworth.lunar.*` names. Inventory
with `jar tf lunar-platform-mappings-v1_8.jar` (no filter — a previous
attempt filtering for "map" in filenames turned up nothing, which only
means the files inside aren't literally named with that word).

---

## Loader mechanics

Lunar Client is built on LegacyLauncher (a fork of Mojang's LaunchWrapper):
a classloader with class-name mapping and bytecode-transforming built in.
No FML on top of it for the 1.8 lane — the only transformer is Mixin plus
Ichor's own remapping pipeline.

### Jar layout under `.lunarclient/offline/multiver/`

| File | What it is |
|---|---|
| `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` | 1.7/1.8/1.12 mixin classes + configs |
| `lunar-platform-mappings-v1_8.jar` | Presumed mapping/retrace data (unverified contents) |
| `lunar.jar` | Core/shared Lunar client code |
| `Forge_v1_8.jar` | Separate file — relationship to the mixin lane is UNVERIFIED. May be a real standalone Forge launch path. |
| `OptiFine_v1_8.jar` / `optifine-...-all.jar` | OptiFine integration |

### Why there's no lifecycle

Lunar's mixin configs declare `"required": true` and `"target": "CLIENT"` —
this is Lunar patching its *own* client, not hosting a plugin API. Anything
you add has to look, to Mixin, exactly like one more of Lunar's own first-
party patches. A broken mixin affects the whole client process.

### Open question worth resolving early

Whether `Forge_v1_8.jar` is a legitimate alternate launch route is a cheap
check — if Lunar can launch straight into real Forge 1.8.9, normal Forge
conventions from `minecraft-legacy-modding-189` apply instead of any of
this. Check Lunar's launcher for a profile dropdown that mentions Forge.

---

## Port doctrine

- **Default route**: rewrite the hook layer as Mixin, targeting vanilla
  MC class names directly (they're not renamed — see Obfuscation above).
  Drop FML/`@Mod`/the event bus entirely.
- **Use Searge names in `@Inject`**: confirmed by smoke test. Query
  `lunar2searge.tsrg` or use TARGET.md's Runtime Name Table. Never guess
  a Searge name or use the MCP name with `remap=false`.
- **Use `remap=false`** on every `@Mixin` and `@Inject`. Set
  `"injectors": { "defaultRequire": 0 }` in your mixin JSON during
  development so missing targets fail silently rather than hard-crashing
  (flip to `1` once confirmed working).
- **MixinConfigs in manifest** is the confirmed loading mechanism. No
  launch args. See External mods section above.
- **Compile with `-proc:none`** (not `mixin.env.disableRefMap=true`) to
  skip the annotation processor and avoid Gson dependency errors.
- **Prefer `@Inject` over `@Overwrite`**: FuriahVisuals (another mod on
  this machine) hooks the same classes. `@Inject` stacks safely;
  `@Overwrite` fights other mods.
- Treat the specific build you're pinned to as an ABI. A Lunar update
  that changes its Searge mapping will break your mixin targets outright.

---

## Porting a Forge 1.8.9 mod onto Lunar

### Two realistic routes

**Route A — rewrite as Mixin (default, recommended).**
Take the mod's actual logic and re-implement the hook points as `@Mixin`
classes targeting vanilla MC class names with Searge method names (from
TARGET.md or tsrg). Drop FML/`@Mod`/event bus entirely.

**Route B — forge-shim package (cheaper, narrower).**
Build a small local package reimplementing just enough of `@Mod`, a
minimal event bus, and `GameRegistry` against vanilla registries so the
original mod's source compiles with minimal edits. This only gets you
compiling — you'd still need Mixin glue to wire the shimmed registration
calls into something Lunar invokes. Worth it only if the mod's logic is
large enough that rewriting the hook layer is impractical.

### Steps

0. **Run the smoke test first** — confirm the pipeline works on your
   machine before writing any mod-specific code. Source: `Example Mod for
   1.8/smoketest/`. See Step 0 above.
1. Look up the target class and method in TARGET.md's Runtime Name Table.
   If not there, query `lunar2searge.tsrg` and record the result in
   TARGET.md with the raw output pasted as evidence.
2. Write the mixin with `remap=false`. Use the Searge method name in
   `@Inject(method=...)`. Use the MCP class name in `@Mixin(targets=...)`.
3. Compile: `javac -proc:none -cp FuriahVisuals.jar -d classes *.java`
4. Package with the required MANIFEST.MF (see External mods section).
5. Drop in mods folder, launch, load a world, quit.
6. Grep latest.log for your log line. A clean compile proves nothing about
   whether the mixin attached correctly at runtime.
7. If it crashes or the log line is missing, see Debugging below.

---

## Debugging

### Turn on Mixin diagnostics

Launch with (add temporarily to Lunar's JVM args, remove when done):

-Dmixin.debug.verbose=true


### Common failure shapes

- **Log line never appears, no crash** — mixin silently failed. Most
  likely cause: wrong method name. Check that you're using the Searge
  name (`func_78472_g`), not the MCP name (`updateLightmap`). Verify with
  `findstr "methodName" lunar2searge.tsrg`.
- **"Target class not found" at mixin-apply time** — the class name you
  used doesn't exist in this build. Either a typo, or Lunar updated and
  the mapping shifted. Re-query the tsrg.
- **Crash with obfuscated class names in stack trace** — `lunar-platform-
  mappings-v1_8.jar` (once inventoried) should let you retrace these.
- **A clean compile with no runtime verification** — not a passing result.
  A successful compile only proves the Java is syntactically valid.
  Always do the in-game check before calling a port finished.

---

## Pinning to a specific build

Lunar's offline/canary jars are not stable versioned releases — obfuscated
names, mixin configs, even which classes exist can drift on the next
update. Treat whatever jar you built against as an ABI snapshot.

### Practical pinning steps

1. Record the jar's exact file hash alongside the date in TARGET.md:
   `certutil -hashfile legacy-0.1.0-SNAPSHOT-all-nomappings.jar SHA256`
2. Keep a copy of the exact jar you built against somewhere safe, outside
   the live Lunar install — Lunar will silently replace it on auto-update.
3. Because names are hardcoded as Searge names (not refmap-generated), any
   Lunar update that changes its Ichor/Searge mapping will break your
   mixin targets outright — the mixin won't apply, and with `"required": true`
   that's a hard client crash.
4. Before relying on a build again after any Lunar update, re-query the
   tsrg for your target methods and diff against the last-known-good names
   in TARGET.md before assuming nothing changed.