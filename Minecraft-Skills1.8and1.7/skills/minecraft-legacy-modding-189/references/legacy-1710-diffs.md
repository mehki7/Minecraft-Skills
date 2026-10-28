# 1.7.10 vs 1.8.9 differences worth knowing before porting between them

This file documents meaningful API and behavior differences between 1.7.10 and 1.8.9
plain Forge. It is a reference for down-porting from 1.8.9 to 1.7.10 or up-porting
from 1.7.10 to 1.8.9. Do not use it for anything newer than 1.8.9.

## Toolchain

| Aspect | 1.7.10 | 1.8.9 |
|---|---|---|
| Forge build | `10.13.x` series | `11.15.x` series |
| ForgeGradle | 1.2 era | 2.1 era |
| MCP mappings | stable_12 (1.7.10 era) | stable_22 (1.8.9 era) |
| Java | 7 (minimum), 8 (common in practice) | 8 |

Do not mix ForgeGradle 2.1 syntax into a 1.7.10 project or vice versa. The DSL
changed between generations. Check a 1.7.10-era MDK or actual 1.7.10 mod template
for the correct buildscript structure — do not assume it matches 1.8.9.

## Rendering and model system

The shift from 1.7.x to 1.8.x is when Mojang overhauled the rendering pipeline to
the JSON block/item model system. In 1.7.10:
- Block and item rendering still uses the pre-JSON Techne/geometry approach.
- `ISimpleBlockRenderingHandler` / `IItemRenderer` are the relevant interfaces.
- There is no `ModelLoader.setCustomModelResourceLocation` — that is 1.8.x+.

In 1.8.9:
- JSON block models under `assets/<modid>/models/block/` and item models under
  `assets/<modid>/models/item/` are the standard.
- `ModelLoader.setCustomModelResourceLocation` is how you register item models.
- Techne-era rendering code does not port 1:1. Expect a rewrite of the render layer.

If you are porting a mod's renderer between these versions, the rendering code is
almost certainly a full rewrite, not a search-and-replace.

## Event system

Both versions use `MinecraftForge.EVENT_BUS` and `@SubscribeEvent`. Core signatures
are similar but individual event classes and their fields/methods may differ between
1.7.10 and 1.8.9 Forge builds. Always verify the exact event class and method
signatures against the specific pinned Forge build, not a generic assumption.

## Networking

`SimpleNetworkWrapper` exists in both, but exact constructor and registration patterns
differ between the two Forge generations. Check the actual API in the pinned Forge
build jar before writing packet code.

## Recipes

`GameRegistry.addRecipe` and `GameRegistry.addShapelessRecipe` are available in both
eras. The underlying registry mechanism is compatible, but do not assume any 1.12.2+
recipe JSON format works here — it does not. Everything is code-registered in this era.

## Entity system

Entity registration through `EntityRegistry.registerModEntity` exists in both eras
with similar API shape. Entity NBT serialization works the same way at a high level,
but verify exact field names and serialization methods against the pinned build.

## What to do when porting 1.7.10 → 1.8.9

1. Update the toolchain: ForgeGradle 1.2 → 2.1, MCP stable_12 → stable_22, update
   the Forge version to `1.8.9-11.15.1.2318`.
2. Rewrite the entire rendering layer (see above — this is not optional).
3. Verify every event class and method signature against the 1.8.9 Forge source.
4. Check networking handler registration against the 1.8.9 Forge API.
5. Test: compile, load, and exercise actual gameplay — do not just check that it builds.

## What to do when porting 1.8.9 → 1.7.10

The reverse is generally harder: you are giving up the JSON model system and
dropping back to the pre-JSON renderer. If the 1.8.9 mod uses JSON models
(the standard for that version), you will need to implement 1.7.10-era rendering
equivalents. This is a significant undertaking — scope it explicitly before starting.
