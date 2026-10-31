---
name: minecraft-legacy-modding-1710
description: Plain Forge 1.7.10 modding (Forge 10.13.x, Java 7/8, MCP stable_12, ForgeGradle 1.2). Use when the target is vanilla+Forge 1.7.10 specifically, not 1.8.9, not Lunar, not OneClient. Pair with minecraft-legacy-modding-189 for 1.8.9 work.
---

# Legacy Minecraft modding — 1.7.10 (plain Forge)

> **⚠ WARNING — 1.7.10 MAPPING WORK NOT STARTED**
>
> This skill covers the 1.7.10 modding landscape in general terms only.
> The 1.8.9 lane (see `minecraft-lunar-client` and `minecraft-legacy-modding-189`)
> is the only lane where RECON has been done and names have been confirmed.
>
> For Lunar Client 1.7.10 specifically:
> - Whether `lunar2searge.tsrg` covers 1.7 classes is **UNVERIFIED**
> - No class, method, or field names have been confirmed from tsrg output
> - No inject test has been run on any 1.7 target
>
> Do not write mixin `@Inject` annotations for 1.7 targets based on guessed
> or MCP names. Run RECON against the actual tsrg and record results in
> TARGET.md before writing any mixin code for this lane.

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
- Writing Lunar-targeted mixin `@Inject` annotations for 1.7 without first
  running tsrg RECON and recording the output in TARGET.md.

skills\minecraft-oneclient\SKILL.md (full file)

markdown
---
name: minecraft-oneclient
description: Modding or patching Minecraft 1.8.9 on OneClient (a Forge-based client with its own classloader). Use when the specific target is OneClient 1.8.9, not plain Forge, not Lunar. Pair with minecraft-legacy-modding-189 for 1.8.9 background.
---

# OneClient 1.8.9 modding

> **⚠ WARNING — ONECLIENT UNVERIFIED ON CURRENT BUILDS**
>
> OneClient's classloader behavior, bundled modifications, and mixin layer
> have NOT been inventoried at the level that Lunar Client has been.
> No class, method, or field names have been confirmed from any OneClient
> jar. No inject test has been run on any OneClient install.
>
> The 1.8.9 lane on Lunar Client is the only proven lane in this repo.
> Do not assume OneClient behaves identically to Lunar or to plain Forge
> without first running RECON on a real install and recording the results
> in TARGET.md.

OneClient is a Forge-based client, meaning it runs on top of Forge 1.8.9 and
in principle exposes the standard Forge FML lifecycle (`@Mod`, event bus, `GameRegistry`).
However, like Lunar Client, it ships its own classloader modifications and may bundle
its own coremod or mixin hooks that interact with the standard Forge load sequence.

**The key difference from plain Forge 1.8.9:** OneClient may intercept or modify
class loading in ways that affect coremod or mixin behavior. Confirm the actual
classloader behavior from a real install before writing any hook that depends on it.

## Default assumptions (carry forward from plain Forge 1.8.9 until RECON contradicts)

- Java 8 toolchain (OneClient is Forge-based, so the standard FG2.1 / Java 8 baseline applies)
- ForgeGradle 2.1 era build setup
- MCP stable_22 mappings
- Standard FML lifecycle available: `@Mod`, `FMLPreInitializationEvent`, event bus
- `GameRegistry` works normally for block/item registration

**These assumptions may break** if OneClient bundles its own classloader that intercepts
registry calls or class transforms. Confirm with a real install test before relying on them
for a hook that touches OneClient's own client-side features.

## What is different from plain Forge 1.8.9

OneClient-specific features (minimap, cosmetics, performance overlays, etc.) are
implemented as coremods or patches on top of Forge. If you are trying to hook into or
interact with those specific OneClient features, you need to inspect their implementation
the same way you would inspect Lunar's mixin layer.

If you are only adding a standalone content mod (new blocks, items, mobs, game mechanics)
that does not interact with OneClient's own features, plain Forge 1.8.9 patterns from
`minecraft-legacy-modding-189` will likely work directly.

## Anti-patterns

- Assuming OneClient's internal class names or package structure matches Lunar Client's.
  They are different clients with different implementations.
- Assuming a mod tested only on plain Forge 1.8.9 will work identically on OneClient
  without testing — verify on the actual client.
- Using anything newer than 1.8.9 APIs, ForgeGradle 6+, or Java 17 conventions here.
- Writing mixin `@Inject` annotations using guessed or MCP names without first running
  tsrg RECON on a real OneClient install and recording the output in TARGET.md.