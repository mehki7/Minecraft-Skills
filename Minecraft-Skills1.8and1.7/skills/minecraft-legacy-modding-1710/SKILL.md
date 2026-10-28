---
name: minecraft-legacy-modding-1710
description: Plain Forge 1.7.10 modding (Forge 10.13.x, Java 7/8, MCP stable_12, ForgeGradle 1.2). Use when the target is vanilla+Forge 1.7.10 specifically, not 1.8.9, not Lunar, not OneClient. Versions newer than 1.7.10 are out of scope for this skill.
---

# Legacy Minecraft modding — 1.7.10 (plain Forge)

This skill covers vanilla+Forge modding for Minecraft 1.7.10 specifically.
For 1.8.9 plain Forge, use `minecraft-legacy-modding-189`. For Lunar Client,
use `minecraft-lunar-client`. For OneClient, use `minecraft-oneclient`.

## Toolchain

- Minecraft: 1.7.10
- Forge: `10.13.x` series (common recommended build: `10.13.4.1614`)
- Java: 7 (minimum), 8 (common in practice — prefer 8 for a modern dev environment)
- ForgeGradle: 1.2 era (not FG2, not FG6 — the DSL is completely different)
- MCP mappings: stable_12
- `build.gradle` uses the old-style `buildscript { ... }` ForgeGradle 1.2 plugin
  application. Do not use FG2+ syntax here.

## FML lifecycle

Same high-level structure as 1.8.9:
- `@Mod` annotation on your main class
- `@EventHandler` on `FMLPreInitializationEvent`, `FMLInitializationEvent`, `FMLPostInitializationEvent`
- `@SubscribeEvent` on `MinecraftForge.EVENT_BUS`
- `@SideOnly(Side.CLIENT)` for client-only code
- `GameRegistry.registerItem(...)`, `GameRegistry.registerBlock(...)` in FMLInitEvent
- `ObfuscationReflectionHelper` for reaching obfuscated vanilla members

## Rendering system — pre-JSON era

1.7.10 predates Mojang's JSON model system. Key differences from 1.8.9+:
- No JSON block/item models under `assets/<modid>/models/`. That system does not exist.
- Block rendering uses `ISimpleBlockRenderingHandler`.
- Item rendering uses `IItemRenderer`.
- Techne (`.tcn` format) was the common 3D model tool for this era.
- There is no `ModelLoader.setCustomModelResourceLocation`.

If you are porting a 1.8.9 mod down to 1.7.10, the entire rendering layer is a
rewrite — not optional, not a quick fix. Scope that explicitly.

## Routing

| Need | Read |
|---|---|
| Toolchain/Gradle setup details | [java7-gradle.md](references/java7-gradle.md) |
| 1.7.10 API surface notes | [legacy-1710-api.md](references/legacy-1710-api.md) |
| Porting from/to 1.8.9 | [version-diff-1710-189.md](references/version-diff-1710-189.md) |
| Behavior recovery | [behavior-recovery.md](references/behavior-recovery.md) |
| Testing and release | [testing-release.md](references/testing-release.md) |
| Mixin on 1.7.10 (if needed as bolt-on) | [mixin-1710.md](references/mixin-1710.md) |

## Coverage map template

| Feature | Source class/method (MCP stable_12 name) | Status | Behavior difference |
|---|---|---|---|
| (your feature) | (exact MCP name) | proposed | — |

## Anti-patterns

- Using ForgeGradle 2.1+ syntax in a 1.7.10 project.
- Assuming JSON models work here (they don't — not until 1.8).
- Assuming MCP stable_22 names match stable_12 names. They are different mapping
  sets and class/method names can differ between them.
- Applying 1.8.9+ event class signatures to 1.7.10 (verify per-version).
- Referencing any version newer than 1.7.10 in this skill's context.
