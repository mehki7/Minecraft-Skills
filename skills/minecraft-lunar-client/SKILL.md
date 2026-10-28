---
name: minecraft-lunar-client
description: Port or patch client-side Minecraft mods onto Lunar Client's own closed, Mixin-based 1.7/1.8/1.12 "legacy" bundle (not Forge, not Fabric). Use when the target is Lunar Client specifically, its offline/multiver jars, or porting a Forge mod to run inside Lunar. Do not use for ordinary Forge or Fabric modding with no Lunar involvement — use minecraft-legacy-modding or the main minecraft-modding skill for that.
---

# Lunar Client (legacy, 1.7/1.8/1.12 lane) modding

Lunar Client is not a mod loader. It is a complete closed client with its
own classloader and its own bundled, ProGuard-obfuscated game jars. There
is no `@Mod`, no event bus, no registry API, no FML lifecycle inside it.
The only way in is Mixin, patched directly onto Lunar's obfuscated classes.

Always read [TARGET.md](../../TARGET.md) first. It is the single source of
truth for what's actually confirmed on the pinned build vs still a guess.
Never assert something from this file that TARGET.md marks UNVERIFIED —
point at the relevant RECON script instead.

## What's actually there (confirmed structure)

The 1.7/1.8/1.12 "legacy" lane ships as two jars sitting side by side in
`.lunarclient/offline/multiver/`:

- `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` — the actual mixin classes.
  Despite the name implying only "legacy", it bundles three separate
  version lanes in one jar, each its own package:
  - `com.moonsworth.lunar.v1_7.optifine.mixin` (1.7, OptiFine compat)
  - `com.moonsworth.lunar.v1_8.forge.mixin` (1.8, Forge compat)
  - `com.moonsworth.lunar.v1_8.optifine.mixin` (1.8, OptiFine compat)
  - `com.moonsworth.lunar.v1_12.forge.mixin` (1.12, Forge compat)
  - `com.moonsworth.lunar.legacy.optifine.mixin` (a shared/base OptiFine lane)
- `lunar-platform-mappings-v1_8.jar` — presumed deobfuscation/mapping data
  for the v1_8 lane. Contents not yet inventoried — see TARGET.md LIKELY
  section.

Mixin configs for the 1.8 lane, bundled inside `legacy-...-nomappings.jar`:
`mixins.legacy_forge_v1_8.json`, `mixins.legacy_lunar_v1_8.json`,
`mixins.legacy_optifine_v1_8.json`, `mixins.legacy_bridge_v1_8.json`, and
`_combined` variants.

Every config inspected so far declares:
- `"compatibilityLevel": "JAVA_17"` — this lane runs on a Java 17
  toolchain, not Java 8. This is the single most important correction to
  make versus naive "1.8.9 modding = old Java 8 Forge assumptions."
- `"minVersion": "0.8"` for Mixin itself.
- No `"refmap"` key — names are matched directly, raw/obfuscated, with no
  remap step.

All class names, both the mixin classes and (presumed) the vanilla classes
they patch, are ProGuard-obfuscated to random uppercase letter sequences
(e.g. `IOOCCRIRHHROHIHRCHHRRIOICHIOIR`). There is no human-readable name
anywhere in the shipped jar. See [obf-and-retrace.md](references/obf-and-retrace.md).

## Routing

- Need to know Lunar's loader mechanics, jar layout, or obfuscation state → [lunar-loader.md](references/lunar-loader.md)
- Need to find or confirm where external mod jars actually go → [external-mods.md](references/external-mods.md)
- Need to resolve an obfuscated class/method name to something you can target → [obf-and-retrace.md](references/obf-and-retrace.md)
- Need to lock a port to this specific build so it doesn't break on Lunar's next update → [canary-pinning.md](references/canary-pinning.md)
- Porting an existing Forge 1.8.9 mod's source onto Lunar → [forge-to-lunar-port.md](references/forge-to-lunar-port.md)
- Mixin not applying, crash on load, wrong class error → [debugging.md](references/debugging.md)

## Port doctrine

- Default route: rewrite the hook layer as Mixin, targeting Lunar's
  obfuscated classes directly. Drop FML/`@Mod`/the event bus entirely —
  none of it exists inside Lunar.
- Since you're pinning to one build (not chasing portability across
  releases), don't build a remapping pipeline. Compile with
  `mixin.env.disableRefMap=true`, an empty `"refmap": ""`, and write mixin
  targets using the exact obfuscated runtime names you resolved via RECON.
  This matches what Lunar's own shipped configs already do (no refmap key).
- For any `@Mixin` targeting a Lunar-internal class
  (`com.moonsworth.lunar.*`), always set `remap = false` explicitly.
  Mixin's remapper only touches `net.minecraft.*`-shaped names — left on
  default, it will silently fail to match or mismatch Lunar's own classes.
- Treat the specific build you're pinned to as an ABI, not a version
  number. A canary/offline build can rename classes on its next update —
  see [canary-pinning.md](references/canary-pinning.md).

## Anti-patterns to avoid

- Assuming Java 8 / old ForgeGradle 1.8.9 conventions apply here — they
  don't, this lane is Java 17.
- Letting Mixin's default remapper touch `com.moonsworth.lunar.*` targets.
- Treating `Forge_v1_8.jar` (a separate file in the same folder) as part
  of this mixin-based lane — it may be an entirely separate launch path
  (real standalone Forge). Don't conflate the two until RECON confirms
  how they relate. See [lunar-loader.md](references/lunar-loader.md).
- Claiming a mixin target is correct because the mod compiled. A compile
  only proves the Java source is valid — it says nothing about whether
  the mixin actually attached to the right method at runtime. Verify with
  `-Dmixin.debug=true -Dmixin.checks=true -Dmixin.verbose=true` and watch
  the real in-game load.
