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