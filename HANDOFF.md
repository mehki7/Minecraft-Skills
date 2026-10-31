# HANDOFF.md

## What this repo is

Skill pack + name table for porting 1.8.9 Forge mods onto Lunar Client.
Two target mods: FuriahVisuals (in progress) and a MoBends 1.7.10 backport.

## Smoke test status

COMPLETE. Both gates passed as of 2026-10-29.

Gate 1 - plugin onLoad:
  [17:53:16] [main/INFO]: [SMOKETEST] *** SMOKE TEST PASS -- plugin onLoad fired for package: com.smoketest.mixin ***

Gate 2 - @Inject into EntityRenderer:
  [19:32:19] [Client thread/INFO]: [STDOUT]: [SMOKETEST] *** INJECT PASS -- updateLightmap HEAD fired in net.minecraft.client.renderer.EntityRenderer ***

Smoke test jar: C:\smoketest\smoketest.jar
Profile used: 1.8-furiahvisuals

## Key finding: Searge names required

Ichor remaps vanilla MC bytecode to Searge names BEFORE Mixin runs.
remap=false injections MUST use Searge names, NOT MCP names.

WRONG:  method = "updateLightmap"     (MCP name, fails silently)
RIGHT:  method = "func_78472_g"       (Searge name, confirmed working)

Mapping file: C:\Users\marckie\AppData\Roaming\.minecraft\.ichor\lunar2searge.tsrg
Format: class lines unindented, method lines indented as: MCPname (descriptor) SeargeName

Vanilla MC CLASS names are NOT renamed by Ichor.
Only methods and fields get Searge-remapped.
Lunar's own com.moonsworth.lunar.* classes are ProGuard-obfuscated separately.

## Key finding: zero JVM arguments needed

Manifest MixinConfigs entry is the sole mechanism for loading mixin configs.
No launch arguments required. No coremod registration needed.

Required manifest entries:
  TweakClass: org.spongepowered.asm.launch.MixinTweaker
  MixinConfigs: mixins.yourmod.json
  FMLCorePluginContainsFMLMod: true
  ForceLoadAsMod: true

## Key finding: external mods path VERIFIED

Drop compiled jars into:
  C:\Users\marckie\.lunarclient\profiles\<profile>\mods\
Confirmed working for profile 1.8-furiahvisuals.

## Runtime name table

Full table with tsrg evidence: TARGET.md (repo root)
Copied to: Minecraft-Skills1.8and1.7\TARGET.md

Key entries:
  func_78472_g   = updateLightmap(F)V        on EntityRenderer  [tsrg + live inject]
  func_78482_e   = hurtCameraEffect(F)V      on EntityRenderer  [tsrg]
  func_175068_a  = renderWorldPass(IFJ)V     on EntityRenderer  [tsrg]
  func_181560_a  = updateCameraAndRender(FJ)V on EntityRenderer [tsrg]
  func_78474_d   = renderRainSnow(F)V        on EntityRenderer  [tsrg]
  func_78484_h   = addRainParticles()V        on EntityRenderer  [tsrg]
  func_76318_c   = endStartSection(String)V  on Profiler        [tsrg]
  func_175180_a  = renderGameOverlay(F)V     on GuiIngame       [tsrg]
  func_180626_a  = getFloatTemperature(BlockPos)F on BiomeGenBase [tsrg]
  dispatchRenderLast                          on ForgeHooksClient [Forge, not in tsrg]
  field_74333_Y  = gammaSetting               on GameSettings    [tsrg]

## Skills updated this session

skills\minecraft-legacy-modding-189\SKILL.md
  - Renamed from minecraft-legacy-modding
  - Java 8 confirmed (was incorrectly Java 17)
  - Searge names section added
  - References inlined, references\ folder deleted

skills\minecraft-lunar-client\SKILL.md
  - external-mods path now VERIFIED
  - Port doctrine corrected: use Searge names from TARGET.md
  - Compile flag corrected: -proc:none (was mixin.env.disableRefMap=true)
  - Step 0 smoke test added as mandatory gate
  - @Inject preferred over @Overwrite to avoid fighting FuriahVisuals
  - References inlined, references\ folder deleted

## Build commands (confirmed working)

  javac -proc:none -cp "...FuriahVisuals.jar" -d C:\smoketest\classes SmokePlugin.java MixinEntityRendererSmoke.java
  jar cfm smoketest.jar META-INF\MANIFEST.MF -C classes . mixins.smoketest.json mcmod.info
  copy /Y smoketest.jar "...\.lunarclient\profiles\1.8-furiahvisuals\mods\smoketest.jar"

## What is NOT done

- Real mixin code for FuriahVisuals not written yet (smoke test was the gate)
- MoBends 1.7.10 backport not started
- Only EntityRenderer methods have live-inject confirmation; others are tsrg only

## Next session starting point

Read TARGET.md and both SKILL.md files first.
Smoke test passes. Names are confirmed. Ready to write real mixin code.
Start with FuriahVisuals: identify which EntityRenderer hooks it needs,
map each MCP name to Searge via TARGET.md, write @Inject with remap=false.
