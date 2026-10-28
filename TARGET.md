# TARGET.md — ABI pin for Lunar Client 1.8.9 porting

This is the single source of truth for what's actually confirmed about the
target vs what's still a guess. Every claim below is tagged. Nothing marked
UNVERIFIED may be treated as fact anywhere else in this skill pack — if a
reference file needs it, it links back here and says "go run RECON to
confirm this on your machine."

## Pin

- Game: Minecraft 1.8.9
- Client: Lunar Client, offline multiver bundle (`.lunarclient/offline/multiver/`)
- The 1.8 lane ships as: `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` (code) +
  `lunar-platform-mappings-v1_8.jar` (mapping data, contents not yet inspected)
- Java toolchain for the mixin classes: **17**, not 8 — see VERIFIED below.
  This overturns the original assumption that 1.8.9 Lunar support runs on
  an old Java 8 stack like vanilla Forge 1.8.9 does.
- Mixin: `minVersion` declared as `"0.8"` in the shipped configs.

## Status triage

### VERIFIED (pulled directly from the user's own install, 2026-10-27)

- Mod jars/bundles live at `C:\Users\<user>\.lunarclient\offline\multiver\`.
  Source: `dir /s /b /o:gn` of that folder.
- The 1.8 legacy code bundle is `legacy-0.1.0-SNAPSHOT-all-nomappings.jar`.
  It also bundles 1.7 and 1.12 mixin classes in the same jar, each under
  their own package (`v1_7`, `v1_8`, `v1_12`, plus a separate
  `legacy/optifine` package for OptiFine-specific hooks).
- Mixin config files present for the 1.8 lane (extracted and read directly):
  `mixins.legacy_forge_v1_8.json`, `mixins.legacy_lunar_v1_8.json`,
  `mixins.legacy_optifine_v1_8.json`, `mixins.legacy_bridge_v1_8.json`,
  plus `_combined` variants that bundle multiple lanes together.
- `compatibilityLevel` in both inspected configs
  (`mixins.legacy_lunar_v1_8.json`, `mixins.legacy_forge_v1_8.json`) is
  **`"JAVA_17"`**. Raw evidence:
  ```
  {"minVersion":"0.8","package":"com.moonsworth.lunar.v1_8.forge.mixin",
   "target":"CLIENT","required":true,"compatibilityLevel":"JAVA_17",
   "mixinPriority":200, ... }
  ```
- `minVersion` for Mixin itself is declared as `"0.8"` in both configs —
  not the `0.7.11-SNAPSHOT` originally guessed.
- No `"refmap"` key is present in either config. Mixin only looks for a
  refmap when the config declares one, so the shipped configs are relying
  on direct/raw name matching, not a remap pipeline — matches the port
  doctrine ("build direct, refmap off") the original plan recommended.
- All class names inside the jar (both mixin classes and, presumably, the
  vanilla/game classes they patch) are ProGuard-style obfuscated: random
  uppercase letter sequences, e.g.
  `com/moonsworth/lunar/v1_8/forge/mixin/IOOCCRIRHHROHIHRCHHRRIOICHIOIR.class`.
  This confirms the "you must resolve names yourself" premise — there is
  no human-readable class name anywhere in this jar.
- The package `com.moonsworth.lunar.*` pattern from the original research
  doc is confirmed correct on this build.

### LIKELY (design for it, not yet directly confirmed)

- `lunar-platform-mappings-v1_8.jar` contains the actual deobfuscation /
  retrace mapping table for the v1_8 lane (name implies it, contents not
  yet opened — a plain filename search for "map" inside it returned
  nothing, so its internal file names don't literally contain that word;
  needs a full `jar tf` listing with no filter to see what's actually in it).
- Lunar's official external-mod support (if any) for 1.8.9 piggybacks on
  the same `legacy` jar rather than a separate loader.

### UNVERIFIED — must be resolved by RECON before relying on it

- [ ] **Which vanilla Minecraft class/method each mixin actually targets.**
      This is the item that blocks writing real mixin code. The `@Mixin`
      annotation on each obfuscated `.class` file names the target class,
      but reading it requires decompiling/javap-ing the class file, which
      was not completed manually (Windows `javap` + path handling was too
      fiddly to do by hand over chat). **Resolve with:**
      `RECON/02-mine-mixin-targets.py` (script in this kit) run from a
      local agent with real file access — do not attempt this by hand in
      cmd again, script it.
- [ ] Exact path of a **user-facing external mods folder** (i.e. where
      *you* drop a 3rd-party `.jar` you want Lunar to load) for the 1.8.9
      lane specifically. What was found so far (`offline/multiver/`) is
      Lunar's own internal bundle folder, not confirmed to be a drop-in
      mods folder.
- [ ] Manifest/launch keys the 1.8 lane honors (`TweakClass`,
      `MixinConfigs`, a custom key, or none — loaded entirely by Lunar's
      own bootstrap instead).
- [ ] Contents of `lunar-platform-mappings-v1_8.jar` — open and inventory it.
- [ ] Whether `Forge_v1_8.jar` (present in the same folder, separate from
      the mixin-based `legacy` jar) is an alternate/fallback launch path —
      if Lunar can launch straight into real Forge 1.8.9, that may be a far
      cheaper porting route than mixin-patching Lunar's own client.

## Rule

No reference file in this pack may assert an UNVERIFIED item as settled
fact. Either cite the RECON evidence above it, or say explicitly "this is
unverified, run RECON/0X first."
