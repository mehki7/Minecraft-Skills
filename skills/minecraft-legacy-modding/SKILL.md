---
name: minecraft-legacy-modding
description: General knowledge for modding Minecraft 1.7.x/1.8.x/1.12.x era — old MCP mappings, Mixin basics, Java 8-era tooling norms. Use when the target game version predates modern NeoForge/Fabric (26.x) or Forge 1.20.1. Pair with minecraft-lunar-client when the actual target is Lunar Client specifically, not plain Forge.
---

# Legacy Minecraft modding (1.7.x / 1.8.x / 1.12.x)

This covers the general old-Minecraft modding landscape. If the actual
target is Lunar Client (not plain vanilla+Forge), read
`minecraft-lunar-client` as well — Lunar breaks several of the default
assumptions below (see the Java version note).

## Routing

- Mixin basics for this era (vs Forge's event/coremod system) → [mixin-189.md](references/mixin-189.md)
- What replaces Forge's `GameRegistry` when there's no loader lifecycle → [no-loader-registration.md](references/no-loader-registration.md)
- Toolchain/Gradle setup for this era → [java8-gradle.md](references/java8-gradle.md)
- API surface specific to 1.8.9 → [legacy-189-api.md](references/legacy-189-api.md)

## Default assumptions for this era — and the one exception

For **plain Forge 1.8.9** (`1.8.9-11.15.1.2318`):
- Java 8 toolchain, ForgeGradle 2.1-era conventions
- MCP stable_22 mappings
- Full FML lifecycle: `@Mod`, `FMLPreInitializationEvent`,
  `@SubscribeEvent` on `MinecraftForge.EVENT_BUS`, `GameRegistry`,
  `@SideOnly`, `ObfuscationReflectionHelper`
- Mixin exists in this era but is a bolt-on, not the default hook
  mechanism — coremods (`IFMLLoadingPlugin` + `IClassTransformer`) are
  the "native" Forge way of doing ASM-level patching.

**Exception, confirmed by direct inspection (not a guess):** if the
actual target is Lunar Client's bundled 1.8 lane rather than plain Forge,
none of the above FML/Java-8 assumptions hold. Lunar's shipped mixin
configs for 1.8 declare `"compatibilityLevel": "JAVA_17"` — see
`minecraft-lunar-client`'s TARGET.md for the raw evidence. Don't default
to "1.8.9 = Java 8" without first checking which of these two situations
you're actually in.

## Anti-patterns

- Copying 1.20.1-era ForgeGradle 6 / Java 17 patterns onto plain Forge
  1.8.9 — wrong toolchain for that target.
- Copying modern (1.21.x) asset path conventions (singular `recipe/`
  etc.) onto a 1.8.9 resource pack — pack format is completely different,
  see the main `minecraft-modding` skill's resource-pack guidance for
  version-specific pack_format numbers.
- Assuming Mixin's default remapper handles everything — on this era,
  with old/incomplete refmap tooling, direct-name + `remap = false` is
  often the pragmatic choice, same as the Lunar-specific guidance.
