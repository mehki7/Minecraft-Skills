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
- **Forge loader confirmed**: the active profile (`1.8-furiahvisuals`) uses
  Forge 1.8.9 as its loader. `Forge_v1_8.jar` in the multiver folder is what
  powers this. Confirmed by Lunar launcher UI showing Version: 1.8.9, Loader:
  Forge icon (2026-10-30).
- Java toolchain for Lunar's OWN mixin classes: **17** — see VERIFIED below.
  External mod jars compiled at **Java 8** load correctly alongside these;
  confirmed by smoke test (javac 1.8.0_504, `-proc:none`).
- Mixin: `minVersion` declared as `"0.8"` in the shipped configs.
- Ichor remapping pipeline: Lunar remaps the game bytecode to **Searge names**
  before the mod classloader runs. This means ALL vanilla method/field
  references in mod jars must use Searge names at the bytecode level — not
  MCP names. This applies to compiled call sites AND to Mixin annotation
  strings.

## Status triage

### VERIFIED (pulled directly from the user's own install)

- Mod jars live at `C:\Users\<user>\.lunarclient\offline\multiver\`.
- The 1.8 legacy code bundle is `legacy-0.1.0-SNAPSHOT-all-nomappings.jar`.
  It bundles 1.7, 1.8, and 1.12 mixin classes under their own packages
  (`v1_7`, `v1_8`, `v1_12`, plus `legacy/optifine`).
- Mixin config files for the 1.8 lane: `mixins.legacy_forge_v1_8.json`,
  `mixins.legacy_lunar_v1_8.json`, `mixins.legacy_optifine_v1_8.json`,
  `mixins.legacy_bridge_v1_8.json`, plus `_combined` variants.
- `compatibilityLevel` in both inspected configs is **`"JAVA_17"`**:

{“minVersion”:”0.8",”package”:”com.moonsworth.lunar.v1_8.forge.mixin”,
“target”:”CLIENT”,”required”:true,”compatibilityLevel”:”JAVA_17",
“mixinPriority”:200, ... }

- `minVersion` is `"0.8"` in both configs.
- No `"refmap"` key in either config — direct/raw name matching only.
- All Lunar classes are ProGuard-obfuscated (`com.moonsworth.lunar.*`
  package, random uppercase class names).

**Added 2026-10-29 — smoke test session results:**

- **External mods folder confirmed**:
  `C:\Users\marckie\.lunarclient\profiles\1.8-furiahvisuals\mods\`
  Drop a `.jar` there; Lunar picks it up with zero configuration.
  Evidence: `smoketest.jar` → `onLoad` fired:

[17:53:16] [main/INFO]: [SMOKETEST] *** SMOKE TEST PASS -- plugin onLoad fired for package: com.smoketest.mixin ***


- **Manifest keys confirmed** — no JVM args required:

Manifest-Version: 1.0
FMLCorePluginContainsFMLMod: true
ForceLoadAsMod: true
TweakClass: org.spongepowered.asm.launch.MixinTweaker
TweakOrder: 0
MixinConfigs: mixins.smoketest.json

  (trailing blank line required; no trailing spaces)

- **Mixin pipeline confirmed end-to-end**:

[17:53:16] [main/INFO]: [SMOKETEST] *** SMOKE TEST PASS -- plugin onLoad fired ***
[19:32:19] [Client thread/INFO]: [STDOUT]: [SMOKETEST] *** INJECT PASS -- updateLightmap HEAD fired in net.minecraft.client.renderer.EntityRenderer ***


- **Mixin annotation strings require Searge names**:
  `@Inject(method = "updateLightmap", remap = false)` → silent failure
  `@Inject(method = "func_78472_g", remap = false)` → fires correctly
  This is specifically about the STRING in the annotation — the compiler
  cannot check it, Mixin resolves it at runtime against already-remapped
  bytecode. `defaultRequire: 1` makes wrong names throw instead of silently
  skipping. Always use `defaultRequire: 1`.

- **Java 8 (javac 1.8.0_504) confirmed** for external mod jars.
  Compile with `-proc:none`.

- **`@Inject` not `@Overwrite`** — FuriahVisuals hooks the same classes.

**Added 2026-10-30 — Forge events VERIFIED; Searge-compile VERIFIED:**

- **Forge events VERIFIED working** — `@SubscribeEvent EntityJoinWorldEvent`
  fires correctly on this Lunar Forge build. Evidence: CuteMobModelsYarr
  (`YarrCuteMobModelsRemake-1.0.11-1.8.9.jar`) uses `EntityJoinWorldEvent`
  with `@SubscribeEvent`, contains NO mixin at all (MANIFEST.MF has no
  TweakClass or MixinConfigs, confirmed by `jar tf`), and ran fully on this
  profile. Forge event bus is live.

- **All vanilla call sites in mod bytecode MUST be Searge-named** — `func_`
  methods and `field_` fields. MCP names (`setPosition`, `isRemote`, etc.)
  do not exist in the runtime and silently miss. This is why plain MCP-era
  Forge mods "load but don't function" — FML reads `mcmod.info` so the mod
  appears loaded, but every vanilla method call fails to link.
  Evidence from `javap -verbose` on CMMREventHandler.class:

func_70107_b (setPosition) func_72838_d (spawnEntityInWorld)
func_180432_n (copyDataFromOld) func_70106_y (setDead)
field_70165_t (posX) field_70163_u (posY)
field_70161_v (posZ) field_72995_K (isRemote)

  CuteMobModels is fully Searge-compiled and worked. It is NOT a Mixin mod.

- **Compile against the game jar to resolve Searge names** — use
  `-cp legacy-0.1.0-SNAPSHOT-all-nomappings.jar` (the same classpath the
  smoke test already uses). That jar has the Searge-named methods, so javac
  resolves `func_xxxxx` calls at compile time. Every port mod uses this
  classpath regardless of whether it uses Mixin, Forge events, or both.

- **Revised doctrine**:
  Forge events are a valid first choice for hooks Forge exposes (entity
  spawn, tick, HUD). Mixin is required for hooks Forge doesn't expose
  (renderer internals, shader-level effects, FuriahVisuals-style visuals).
  Both paths require Searge names — Forge events via compiled call sites in
  the mod bytecode, Mixin additionally via the annotation string. The compile
  classpath is identical for both.

### LIKELY (design for it, not yet directly confirmed)

- `lunar-platform-mappings-v1_8.jar` contains the deobfuscation mapping
  table for the v1_8 lane (contents not yet fully inventoried).

### UNVERIFIED — must be resolved by RECON before relying on it

- [ ] Contents of `lunar-platform-mappings-v1_8.jar` — open and inventory it.

## Runtime Name Table

All names below confirmed by querying `lunar2searge.tsrg`
(`C:\Users\marckie\AppData\Roaming\.minecraft\.ichor\lunar2searge.tsrg`,
6,028,239 bytes).

**TSRG format**: indented lines are `    MCPname (descriptor) SeargeName`.
Unindented class lines: `runtimePath runtimePath` — Ichor does NOT rename
classes. Use the MCP class name in `@Mixin(targets=...)` and in `extends`/
`implements` declarations. Use the Searge name in `@Inject(method=...)`,
`@Shadow`, and every vanilla method call site in the mod bytecode.

Forge-owned classes and methods are NOT in the tsrg. Use the MCP name
directly for anything in a `net.minecraftforge.*` class.

---

### Classes (10 confirmed)

| Runtime class name | Evidence |
|---|---|
| `net.minecraft.client.renderer.EntityRenderer` | `net/minecraft/client/renderer/EntityRenderer net/minecraft/client/renderer/EntityRenderer` — live-confirmed: inject fired `[19:32:19]` |
| `net.minecraft.profiler.Profiler` | `net/minecraft/profiler/Profiler net/minecraft/profiler/Profiler` |
| `net.minecraft.client.gui.GuiIngame` | `net/minecraft/client/gui/GuiIngame net/minecraft/client/gui/GuiIngame` |
| `net.minecraft.client.settings.GameSettings` | `net/minecraft/client/settings/GameSettings net/minecraft/client/settings/GameSettings` |
| `net.minecraft.world.biome.BiomeGenBase` | `net/minecraft/world/biome/BiomeGenBase net/minecraft/world/biome/BiomeGenBase` |
| `net.minecraft.util.BlockPos` | `net/minecraft/util/BlockPos net/minecraft/util/BlockPos` |
| `net.minecraft.client.renderer.RenderGlobal` | `net/minecraft/client/renderer/RenderGlobal net/minecraft/client/renderer/RenderGlobal` |
| `net.minecraft.util.Timer` | `net/minecraft/util/Timer net/minecraft/util/Timer` |
| `net.minecraft.entity.Entity` | `net/minecraft/entity/Entity net/minecraft/entity/Entity` |
| `net.minecraftforge.client.ForgeHooksClient` | **NOT in tsrg** — Forge class, use MCP name directly. |

---

### Methods (10 confirmed — Searge name goes in `@Inject(method=...)` and in call sites)

| Class | MCP name | Descriptor | Searge name | Evidence |
|---|---|---|---|---|
| `EntityRenderer` | `updateLightmap` | `(F)V` | **`func_78472_g`** | `    updateLightmap (F)V func_78472_g` — live-confirmed `[19:32:19]` |
| `EntityRenderer` | `hurtCameraEffect` | `(F)V` | **`func_78482_e`** | `    hurtCameraEffect (F)V func_78482_e` |
| `EntityRenderer` | `renderWorldPass` | `(IFJ)V` | **`func_175068_a`** | `    renderWorldPass (IFJ)V func_175068_a` |
| `EntityRenderer` | `updateCameraAndRender` | `(FJ)V` | **`func_181560_a`** | `    updateCameraAndRender (FJ)V func_181560_a` |
| `EntityRenderer` | `renderRainSnow` | `(F)V` | **`func_78474_d`** | `    renderRainSnow (F)V func_78474_d` |
| `EntityRenderer` | `addRainParticles` | `()V` | **`func_78484_h`** | `    addRainParticles ()V func_78484_h` |
| `Profiler` | `endStartSection` | `(Ljava/lang/String;)V` | **`func_76318_c`** | `    endStartSection (Ljava/lang/String;)V func_76318_c` |
| `GuiIngame` | `renderGameOverlay` | `(F)V` | **`func_175180_a`** | `    renderGameOverlay (F)V func_175180_a` |
| `BiomeGenBase` | `getFloatTemperature` | `(Lnet/minecraft/util/BlockPos;)F` | **`func_180626_a`** | `    getFloatTemperature (Lnet/minecraft/util/BlockPos;)F func_180626_a` |
| `ForgeHooksClient` | `dispatchRenderLast` | `()V` | **`dispatchRenderLast`** (no remap) | **NOT in tsrg** — Forge method, use MCP name. |

---

### Fields (3 confirmed — use Searge name in `@Shadow` and in field access bytecode)

| Class | MCP name | Searge name | Evidence |
|---|---|---|---|
| `GameSettings` | `gammaSetting` | **`field_74333_Y`** | `    gammaSetting field_74333_Y` |
| `Entity` | `posX` | **`field_70165_t`** | CuteMobModels javap: `net/minecraft/entity/Entity.field_70165_t:D` |
| `World` | `isRemote` | **`field_72995_K`** | CuteMobModels javap: `net/minecraft/world/World.field_72995_K:Z` |

---

**Total confirmed: 23** (10 classes + 10 methods + 3 fields)

## Rule

No reference file in this pack may assert an UNVERIFIED item as settled
fact. Either cite the RECON evidence above it, or say explicitly "this is
unverified, run RECON first."
**Added 2026-10-31 - GuiIngame inject results:**

- **`func_175183_b` (`showCrosshair`, `()Z`) - VERIFIED LIVE.** Inject fired:
  `[STDOUT]: [PORT-GUIINGAME] *** INJECT PASS -- showCrosshair fired ***`
  tsrg line: `    showCrosshair ()Z func_175183_b`
  This is the second distinct class proven, so the pipeline is not EntityRenderer-specific.

- **`func_175180_a` (`renderGameOverlay`, `(F)V`) - TAIL UNREACHABLE.** Inject registered cleanly (defaultRequire 1 would have thrown on a bad name) but never fired. `showCrosshair` is called from inside this method and it does fire, so the method runs - the TAIL is simply never reached. Cause is likely an early return or Lunar replacing the method body.
  **Rule: never inject at TAIL in Lunar's GuiIngame. Use HEAD or a specific call site.** HEAD test on this method pending.

- **Duplicate `@Inject` on one method is safe.** FuriahVisuals also injects `func_175183_b`; two `@Inject` callbacks both run, Mixin stacks them. Only `@Overwrite` or `@Redirect` on the same call actually collide. `showCrosshair` is usable as-is, no priority work needed.

- **`func_180475_a` (`renderScoreboard`) - LIKELY, not yet tested.** Not in tsrg yet - resolve with `findstr renderScoreboard` before use.
