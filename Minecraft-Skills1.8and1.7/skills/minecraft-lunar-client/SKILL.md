---
name: minecraft-lunar-client
description: Port or patch client-side Minecraft 1.8.9 mods onto Lunar Client's own closed, Mixin-based legacy bundle (not Forge, not Fabric). Use when the target is Lunar Client 1.8.9 specifically, its offline/multiver jars, or porting a Forge 1.8.9 mod to run inside Lunar. Do not use for ordinary Forge modding with no Lunar involvement — use minecraft-legacy-modding for that. Versions newer than 1.8.9 and 1.12.2 are out of scope.
---

# Lunar Client (1.8.9 lane) modding

Lunar Client is not a mod loader. It is a complete closed client with its
own classloader and its own bundled, ProGuard-obfuscated game jars. There
is no `@Mod`, no event bus, no registry API, no FML lifecycle inside it.
The only way in is Mixin, patched directly onto Lunar's obfuscated classes.

**Always read [TARGET.md](../../TARGET.md) first.** It is the single source of
truth for what is confirmed on the pinned build vs still a guess. Never assert
something from this file that TARGET.md marks UNVERIFIED — point at the relevant
RECON script instead.

## Scope reminder

This skill covers **1.8.9 only**. 1.12.2 is out of scope. Versions newer than
1.8.9 are out of scope. If something in here looks like it could apply to 1.12.2,
that is incidental — do not extend these patterns to that version.

## What is actually there (confirmed structure)

The 1.8 "legacy" lane ships as two jars in `.lunarclient/offline/multiver/`:

- `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` — the actual mixin classes.
  Despite the name, it bundles three separate version lanes in one jar:
  - `com.moonsworth.lunar.v1_7.optifine.mixin` (1.7, OptiFine compat)
  - `com.moonsworth.lunar.v1_8.forge.mixin` (1.8, Forge compat)
  - `com.moonsworth.lunar.v1_8.optifine.mixin` (1.8, OptiFine compat)
  - `com.moonsworth.lunar.v1_12.forge.mixin` (1.12, Forge compat — separate lane, not our target)
  - `com.moonsworth.lunar.legacy.optifine.mixin` (shared/base OptiFine lane)
- `lunar-platform-mappings-v1_8.jar` — presumed deobfuscation/mapping data
  for the v1_8 lane. Contents not yet inventoried — see TARGET.md LIKELY section.

Mixin configs for the 1.8 lane, bundled inside `legacy-...-nomappings.jar`:
`mixins.legacy_forge_v1_8.json`, `mixins.legacy_lunar_v1_8.json`,
`mixins.legacy_optifine_v1_8.json`, `mixins.legacy_bridge_v1_8.json`, and
`_combined` variants.

Every config inspected declares:
- `"compatibilityLevel": "JAVA_17"` — this lane runs Java 17, not Java 8.
  This is the single most important correction vs naive "1.8.9 = old Java 8 Forge."
- `"minVersion": "0.8"` for Mixin itself.
- No `"refmap"` key — names are matched directly, raw/obfuscated, no remap step.

All class names are ProGuard-obfuscated to random uppercase letter sequences
(e.g. `IOOCCRIRHHROHIHRCHHRRIOICHIOIR`). There is no human-readable name
anywhere in the shipped jar. See [obf-and-retrace.md](references/obf-and-retrace.md).

## Routing

| Need | Read |
|---|---|
| Lunar's loader mechanics, jar layout, obfuscation state | [lunar-loader.md](references/lunar-loader.md) |
| Where external mod jars actually go | [external-mods.md](references/external-mods.md) |
| Resolve an obfuscated class/method name to something targetable | [obf-and-retrace.md](references/obf-and-retrace.md) |
| Lock a port to this specific build | [canary-pinning.md](references/canary-pinning.md) |
| Porting an existing Forge 1.8.9 mod's source onto Lunar | [forge-to-lunar-port.md](references/forge-to-lunar-port.md) |
| Mixin not applying, crash on load, wrong class error | [debugging.md](references/debugging.md) |
| Building and testing a mod for release | [build-and-validate.md](references/build-and-validate.md) |

## Port doctrine

- Default route: rewrite the hook layer as Mixin, targeting Lunar's
  obfuscated classes directly. Drop FML/`@Mod`/the event bus entirely.
- Since you are pinning to one build (not chasing portability across
  releases), do not build a remapping pipeline. Compile with
  `mixin.env.disableRefMap=true`, an empty `"refmap": ""`, and write mixin
  targets using the exact obfuscated runtime names resolved via RECON.
  This matches what Lunar's own shipped configs already do (no refmap key).
- For any `@Mixin` targeting a Lunar-internal class
  (`com.moonsworth.lunar.*`), always set `remap = false` explicitly.
  Mixin's remapper only touches `net.minecraft.*`-shaped names — left on
  default, it will silently fail to match or mismatch Lunar's own classes.
- Treat the specific build you are pinned to as an ABI, not a version number.
  A canary/offline build can rename classes on its next update.

## Coverage map — make one for every porting task

Before writing any mixin code, record:

| Source feature | Hook point (obf name, from RECON) | Target vanilla class | Status | Behavior difference |
|---|---|---|---|---|
| (your feature) | UNVERIFIED until RECON runs | UNVERIFIED | proposed | — |

Use `implemented`, `adapted`, `omitted`, `blocked`, or `unverified` precisely.
Do not mark anything `implemented` until in-game verification passes
(`-Dmixin.debug=true -Dmixin.checks=true -Dmixin.verbose=true`).

## Anti-patterns

- Assuming Java 8 / old ForgeGradle 1.8.9 conventions apply here — they do not.
  This lane is Java 17.
- Letting Mixin's default remapper touch `com.moonsworth.lunar.*` targets.
- Treating `Forge_v1_8.jar` (a separate file in the same folder) as part of
  this mixin-based lane — its relationship is UNVERIFIED. See lunar-loader.md.
- Claiming a mixin target is correct because the mod compiled. A compile only
  proves the Java source is valid — it says nothing about whether the mixin
  actually attached to the right method at runtime. Always verify in-game.
- Importing or referencing 1.12.2 mixin patterns from the `v1_12` package
  inside the same jar — those are a separate, out-of-scope lane.
