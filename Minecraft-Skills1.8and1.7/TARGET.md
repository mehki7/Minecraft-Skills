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
- Java toolchain for Lunar's OWN mixin classes: **17** — see VERIFIED below.
  External mod jars compiled at **Java 8** load correctly alongside these;
  confirmed by smoke test (javac 1.8.0_504, `-proc:none`).
- Mixin: `minVersion` declared as `"0.8"` in the shipped configs.
- Ichor remapping pipeline: Lunar remaps bytecode to **Searge names** BEFORE
  Mixin processes. All `@Inject(method=...)` values must use Searge names
  (e.g. `func_78472_g`), NOT MCP names, when `remap=false` is set.

## Status triage

### VERIFIED (pulled directly from the user's own install)

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

{“minVersion”:”0.8",”package”:”com.moonsworth.lunar.v1_8.forge.mixin”,
“target”:”CLIENT”,”required”:true,”compatibilityLevel”:”JAVA_17",
“mixinPriority”:200, ... }

- `minVersion` for Mixin itself is declared as `"0.8"` in both configs —
  not the `0.7.11-SNAPSHOT` originally guessed.
- No `"refmap"` key is present in either config. Mixin only looks for a
  refmap when the config declares one, so the shipped configs are relying
  on direct/raw name matching, not a remap pipeline — matches the port
  doctrine ("build direct, refmap off") the original plan recommended.
- All class names inside the jar (both mixin classes and the vanilla/game
  classes they patch) are ProGuard-style obfuscated: random uppercase letter
  sequences, e.g.
  `com/moonsworth/lunar/v1_8/forge/mixin/IOOCCRIRHHROHIHRCHHRRIOICHIOIR.class`.
  This confirms the "you must resolve names yourself" premise — there is
  no human-readable class name anywhere in this jar.
- The package `com.moonsworth.lunar.*` pattern from the original research
  doc is confirmed correct on this build.

**Added 2026-10-29 — smoke test session results:**

- **External mods folder confirmed**:
  `C:\Users\marckie\.lunarclient\profiles\1.8-furiahvisuals\mods\`
  Drop a `.jar` there; Lunar's 1.8.9 lane picks it up with zero configuration.
  Evidence: `smoketest.jar` placed there → `onLoad` fired in `latest.log`:

[17:53:16] [main/INFO]: [SMOKETEST] *** SMOKE TEST PASS -- plugin onLoad fired for package: com.smoketest.mixin ***


- **Manifest keys confirmed** — the following MANIFEST.MF entries are honored
  by Lunar's 1.8.9 lane for external mods with NO launch arguments required:

Manifest-Version: 1.0
FMLCorePluginContainsFMLMod: true
ForceLoadAsMod: true
TweakClass: org.spongepowered.asm.launch.MixinTweaker
TweakOrder: 0
MixinConfigs: mixins.smoketest.json

  (trailing blank line required; no trailing spaces on any line)
  Evidence: smoketest.jar with these exact keys, zero JVM args in Lunar
  launcher, both pipeline gates passed. `MixinConfigs` in manifest is the
  sole required mechanism — no per-user setup.

- **Mixin pipeline confirmed end-to-end**:
  - `IMixinConfigPlugin.onLoad` fired → Lunar honors plugin hooks
  - `@Inject` at method HEAD fired → Mixin transforms class bytecode at runtime
  Evidence:

[17:53:16] [main/INFO]: [SMOKETEST] *** SMOKE TEST PASS -- plugin onLoad fired for package: com.smoketest.mixin ***
[19:32:19] [Client thread/INFO]: [STDOUT]: [SMOKETEST] *** INJECT PASS -- updateLightmap HEAD fired in net.minecraft.client.renderer.EntityRenderer ***


- **Searge names required; MCP names fail silently**:
  `@Inject(method = "updateLightmap", remap = false)` → silent failure
  `@Inject(method = "func_78472_g", remap = false)` → fires correctly
  Root cause: Ichor remaps bytecode to Searge names BEFORE Mixin processes.
  `defaultRequire: 0` in mixin JSON means a wrong method name fails with no
  error — the inject is skipped silently. Always use Searge names.
  Confirmed by `lunar2searge.tsrg`:
  updateLightmap (F)V func_78472_g

- **No launch arguments needed**: zero JVM args in Lunar launcher throughout
  all testing; smoke test passed regardless. `MixinConfigs` in manifest is
  confirmed as the sole mechanism. This is the required pattern for all mods.

- **Java 8 (javac 1.8.0_504) confirmed** for compiling external mixin classes.
  Compile with `-proc:none` to skip annotation processor (avoids Gson error).
  Lunar's own shipped code targets Java 17, but Java 8 external jars load fine.

- **`@Inject` not `@Overwrite`** — FuriahVisuals hooks the same classes.
  `@Inject` stacks safely with other mods. `@Overwrite` fights them.
  Use `@Inject` everywhere unless there is no other option.

### LIKELY (design for it, not yet directly confirmed)

- `lunar-platform-mappings-v1_8.jar` contains the actual deobfuscation /
  retrace mapping table for the v1_8 lane (name implies it, contents not
  yet opened — a plain filename search for "map" inside it returned
  nothing, so its internal file names don't literally contain that word;
  needs a full `jar tf` listing with no filter to see what's actually in it).
- Lunar's official external-mod support for 1.8.9 piggybacks on the same
  `legacy` jar rather than a separate loader.

### UNVERIFIED — must be resolved by RECON before relying on it

- [ ] Contents of `lunar-platform-mappings-v1_8.jar` — open and inventory it.
- [ ] Whether `Forge_v1_8.jar` (present in the same folder, separate from
      the mixin-based `legacy` jar) is an alternate/fallback launch path —
      if Lunar can launch straight into real Forge 1.8.9, that may be a far
      cheaper porting route than mixin-patching Lunar's own client.

## Runtime Name Table

All names below confirmed by querying `lunar2searge.tsrg`
(`C:\Users\marckie\AppData\Roaming\.minecraft\.ichor\lunar2searge.tsrg`,
6,028,239 bytes, last modified 2026-10-29, confirmed present by `dir` output).

**TSRG format key**: indented lines are `    MCPname (descriptor) SeargeName`.
Unindented class lines show `runtimePath runtimePath` — same name both sides,
meaning Ichor does NOT rename classes. Class names in `@Mixin(targets=...)` use
the MCP name directly (dots, not slashes). Method/field names in `@Inject` /
`@Shadow` use the Searge name (rightmost column).

Forge-owned classes and methods are NOT in the tsrg — they are not obfuscated
by Lunar/Ichor. Use the MCP name as the runtime name directly.

---

### Classes (10 confirmed)

| Runtime class name | Evidence |
|---|---|
| `net.minecraft.client.renderer.EntityRenderer` | `net/minecraft/client/renderer/EntityRenderer net/minecraft/client/renderer/EntityRenderer` — also live-confirmed: inject fired at `[19:32:19]` |
| `net.minecraft.profiler.Profiler` | `net/minecraft/profiler/Profiler net/minecraft/profiler/Profiler` |
| `net.minecraft.client.gui.GuiIngame` | `net/minecraft/client/gui/GuiIngame net/minecraft/client/gui/GuiIngame` |
| `net.minecraft.client.settings.GameSettings` | `net/minecraft/client/settings/GameSettings net/minecraft/client/settings/GameSettings` |
| `net.minecraft.world.biome.BiomeGenBase` | `net/minecraft/world/biome/BiomeGenBase net/minecraft/world/biome/BiomeGenBase` |
| `net.minecraft.util.BlockPos` | `net/minecraft/util/BlockPos net/minecraft/util/BlockPos` |
| `net.minecraft.client.renderer.RenderGlobal` | `net/minecraft/client/renderer/RenderGlobal net/minecraft/client/renderer/RenderGlobal` |
| `net.minecraft.util.Timer` | `net/minecraft/util/Timer net/minecraft/util/Timer` |
| `net.minecraft.entity.Entity` | `net/minecraft/entity/Entity net/minecraft/entity/Entity` |
| `net.minecraftforge.client.ForgeHooksClient` | **NOT in tsrg** — Forge class, not obfuscated. `findstr` returned empty. Use MCP name as runtime name directly. |

---

### Methods (10 confirmed — use Searge name in `@Inject(method=...)`)

| Class | MCP name | Descriptor | Searge name | Evidence |
|---|---|---|---|---|
| `EntityRenderer` | `updateLightmap` | `(F)V` | **`func_78472_g`** | `    updateLightmap (F)V func_78472_g` — live-confirmed: inject fired `[19:32:19]` |
| `EntityRenderer` | `hurtCameraEffect` | `(F)V` | **`func_78482_e`** | `    hurtCameraEffect (F)V func_78482_e` |
| `EntityRenderer` | `renderWorldPass` | `(IFJ)V` | **`func_175068_a`** | `    renderWorldPass (IFJ)V func_175068_a` |
| `EntityRenderer` | `updateCameraAndRender` | `(FJ)V` | **`func_181560_a`** | `    updateCameraAndRender (FJ)V func_181560_a` |
| `EntityRenderer` | `renderRainSnow` | `(F)V` | **`func_78474_d`** | `    renderRainSnow (F)V func_78474_d` |
| `EntityRenderer` | `addRainParticles` | `()V` | **`func_78484_h`** | `    addRainParticles ()V func_78484_h` |
| `Profiler` | `endStartSection` | `(Ljava/lang/String;)V` | **`func_76318_c`** | `    endStartSection (Ljava/lang/String;)V func_76318_c` |
| `GuiIngame` | `renderGameOverlay` | `(F)V` | **`func_175180_a`** | `    renderGameOverlay (F)V func_175180_a` |
| `BiomeGenBase` | `getFloatTemperature` | `(Lnet/minecraft/util/BlockPos;)F` | **`func_180626_a`** | `    getFloatTemperature (Lnet/minecraft/util/BlockPos;)F func_180626_a` |
| `ForgeHooksClient` | `dispatchRenderLast` | `()V` | **`dispatchRenderLast`** (no remap) | **NOT in tsrg** — Forge method, not obfuscated. `findstr` returned empty. Use MCP name as-is. |

---

### Fields (1 confirmed — use Searge name in `@Shadow`)

| Class | MCP name | Searge name | Evidence |
|---|---|---|---|
| `GameSettings` | `gammaSetting` | **`field_74333_Y`** | `    gammaSetting field_74333_Y` |

---

**Total confirmed: 21** (10 classes + 10 methods + 1 field)

## Rule

No reference file in this pack may assert an UNVERIFIED item as settled
fact. Either cite the RECON evidence above it, or say explicitly "this is
unverified, run RECON/0X first."