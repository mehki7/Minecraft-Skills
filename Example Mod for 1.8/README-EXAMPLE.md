# Example Mod for 1.8 — what's in this folder

## smoketest/ — the canonical build example

`smoketest/` is the reference implementation for the Lunar Client 1.8.9
port pattern. It demonstrates:

- `MANIFEST.MF` with the required `TweakClass`, `MixinConfigs`,
  `FMLCorePluginContainsFMLMod`, and `ForceLoadAsMod` entries
- `IMixinConfigPlugin` (`SmokePlugin.java`) confirming the onLoad gate
- `@Mixin(targets=..., remap=false)` + `@Inject(method="func_78472_g", ...)`
  confirming Searge-name injection into `EntityRenderer`
- Compile with `javac -proc:none`, package with `jar cfm`

Both smoke gates passed on 2026-10-29, profile `1.8-furiahvisuals`.
This is the proven build pattern. Start here.

## Example-1.8.9-Mod/ — reference only, NOT the Lunar pattern

This is a third-party Kotlin/Gradle Forge template using Architectury
Loom. It is kept here for reference, but it is **not** the pattern used
for Lunar Client porting:

- Requires two separate JDKs and Gradle
- Uses Architectury Loom, not plain `javac -proc:none`
- Implies FML exists (`@Mod`, event bus, etc.), which does not apply
  to the Lunar Client 1.8 lane
- The template's `MixinGuiMainMenu.java` uses MCP names without
  `remap=false` — this pattern silently fails on Lunar (see TARGET.md)

Do not use this template as a guide for Lunar porting. Use `smoketest/`
and the `minecraft-lunar-client` skill instead.