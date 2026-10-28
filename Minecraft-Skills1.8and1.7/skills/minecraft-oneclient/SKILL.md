---
name: minecraft-oneclient
description: Modding or patching Minecraft 1.8.9 on OneClient (a Forge-based client with its own classloader and potentially custom coremod/mixin layer). Use when the specific target is OneClient 1.8.9, not plain Forge, not Lunar. Versions newer than 1.8.9 are out of scope.
---

# OneClient 1.8.9 modding

OneClient is a Forge-based client, meaning it runs on top of Forge 1.8.9 and
in principle exposes the standard Forge FML lifecycle (`@Mod`, event bus, `GameRegistry`).
However, like Lunar Client, it ships its own classloader modifications and may bundle
its own coremod or mixin hooks that interact with the standard Forge load sequence.

**The key difference from plain Forge 1.8.9:** OneClient may intercept or modify
class loading in ways that affect coremod or mixin behavior. Read `references/oneclient-loader.md`
to understand what is confirmed about OneClient's specific classloader behavior
before writing any coremod or ASM hook.

## Status

Unlike Lunar Client (where the jar internals have been directly inspected and documented
in TARGET.md), OneClient's specific classloader and bundled modifications have not yet
been inventoried at the same level. Use the UNVERIFIED pattern: confirm the actual
behavior from a real install before relying on assumptions.

## Routing

| Need | Read |
|---|---|
| OneClient classloader behavior and bundle layout | [oneclient-loader.md](references/oneclient-loader.md) |
| Porting a plain Forge 1.8.9 mod to run on OneClient | [forge-to-oneclient-port.md](references/forge-to-oneclient-port.md) |
| Mixin vs coremod choice on OneClient | [oneclient-hooks.md](references/oneclient-hooks.md) |
| Debugging failures specific to OneClient | [debugging.md](references/debugging.md) |

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
the same way you would inspect Lunar's mixin layer — see `oneclient-hooks.md`.

If you are only adding a standalone content mod (new blocks, items, mobs, game mechanics)
that does not interact with OneClient's own features, plain Forge 1.8.9 patterns from
`minecraft-legacy-modding-189` will likely work directly.

## Anti-patterns

- Assuming OneClient's internal class names or package structure matches Lunar Client's.
  They are different clients with different implementations.
- Assuming a mod tested only on plain Forge 1.8.9 will work identically on OneClient
  without testing — verify on the actual client.
- Using anything newer than 1.8.9 APIs, ForgeGradle 6+, or Java 17 conventions here.
