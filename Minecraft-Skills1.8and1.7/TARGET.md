# TARGET.md — ABI pin for Lunar Client 1.8.9 porting

Single source of truth for what is confirmed about the target vs what is still a guess.
Every claim is tagged. Nothing marked UNVERIFIED may be treated as fact anywhere else
in this skill pack. If a reference file needs it, it links back here and says
"run RECON to confirm on your machine."

## Pin

- Game: Minecraft 1.8.9
- Client: Lunar Client, offline multiver bundle (`.lunarclient/offline/multiver/`)
- 1.8 lane ships as: `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` (code) +
  `lunar-platform-mappings-v1_8.jar` (mapping data, contents not yet inventoried)
- Java toolchain for the mixin classes: **17**, not 8 — see VERIFIED below.
  This overturns the naive assumption that 1.8.9 = old Java 8 Forge toolchain.
- Mixin: `minVersion` declared as `"0.8"` in the shipped configs.

## Out of scope for this skill pack

Version 1.12.2 and all versions newer than 1.8.9 are explicitly excluded.
Do not reference 1.12.2 modding patterns, ForgeGradle 6, Java 17 Forge conventions,
or any modern NeoForge/Fabric APIs in this skill. The only targets here are
1.8.9 (primary) and 1.7.10 (handled in the separate `minecraft-legacy-modding`
skill for plain Forge).

## Status triage

### VERIFIED (pulled directly from user's own install, 2026-10-27)

- Mod jars/bundles live at `C:\Users\<user>\.lunarclient\offline\multiver\`.
  Source: `dir /s /b /o:gn` of that folder.
- The 1.8 legacy code bundle is `legacy-0.1.0-SNAPSHOT-all-nomappings.jar`.
  It also bundles 1.7 and 1.12 mixin classes in the same jar under their own
  packages (`v1_7`, `v1_8`, `v1_12`, plus `legacy/optifine` for OptiFine hooks).
- Mixin config files present for the 1.8 lane:
  `mixins.legacy_forge_v1_8.json`, `mixins.legacy_lunar_v1_8.json`,
  `mixins.legacy_optifine_v1_8.json`, `mixins.legacy_bridge_v1_8.json`,
  plus `_combined` variants.
- `compatibilityLevel` in both inspected configs is **`"JAVA_17"`**. Raw evidence:
  ```json
  {"minVersion":"0.8","package":"com.moonsworth.lunar.v1_8.forge.mixin",
   "target":"CLIENT","required":true,"compatibilityLevel":"JAVA_17",
   "mixinPriority":200, ...}
  ```
- `minVersion` for Mixin is declared as `"0.8"` in both configs (not 0.7.11-SNAPSHOT).
- No `"refmap"` key in either config. Shipped configs rely on direct/raw name matching,
  not a remap pipeline. This matches the port doctrine (build direct, refmap off).
- All class names inside the jar are ProGuard-style obfuscated: random uppercase letter
  sequences, e.g. `com/moonsworth/lunar/v1_8/forge/mixin/IOOCCRIRHHROHIHRCHHRRIOICHIOIR.class`.
  No MCP name, no searge name, nothing human-readable.
- The `com.moonsworth.lunar.*` package pattern is confirmed correct on this build.

### LIKELY (design for it, not yet directly confirmed)

- `lunar-platform-mappings-v1_8.jar` contains the deobfuscation/retrace mapping table
  for the v1_8 lane. Its internal file names don't literally contain "map" (a prior
  filter search returned nothing), so it needs a full `jar tf` listing to see what's
  actually inside.
- Lunar's external-mod support for 1.8.9 (if any) piggybacks the same `legacy` jar
  rather than a separate loader.

### UNVERIFIED — must be resolved by RECON before relying on it

- [ ] **Which vanilla class/method each mixin actually targets.**
      This is the item that blocks writing real mixin code. The `@Mixin` annotation
      on each obfuscated `.class` names the target, buried in the bytecode's constant
      pool. **Resolve with:** `RECON/02-mine-mixin-targets.py` — run from a local agent
      with real file access. Do not attempt by hand in cmd.
- [ ] Exact path of the **user-facing external mods folder** for 1.8.9 specifically.
      What was found (`offline/multiver/`) is Lunar's own internal bundle folder, not
      confirmed as a drop-in mods folder.
- [ ] Manifest/launch keys the 1.8 lane honors (`TweakClass`, `MixinConfigs`, a custom
      key, or none — loaded entirely by Lunar's bootstrap).
- [ ] Contents of `lunar-platform-mappings-v1_8.jar` — open and inventory it.
- [ ] Whether `Forge_v1_8.jar` (present in the same folder, separate from the mixin-based
      `legacy` jar) is an alternate/fallback launch path. If Lunar can launch straight
      into real Forge 1.8.9, that may be a far cheaper porting route than mixin-patching
      Lunar's own client.

## Rule

No reference file in this pack may assert an UNVERIFIED item as settled fact.
Either cite RECON evidence above it, or say explicitly "this is unverified, run RECON first."
