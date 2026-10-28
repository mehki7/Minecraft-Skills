# Porting between 1.7.10 and 1.8.9

See also: `minecraft-legacy-modding-189/references/legacy-1710-diffs.md` for the
same content from the 1.8.9 perspective.

## The single biggest change: coordinate system + BlockState

1.7.10 uses raw `int x, y, z` everywhere for world coordinates.
1.8.9 introduced `BlockPos` (an immutable triple) and `IBlockState` (a block +
property map) to replace the old block + metadata system.

If you are porting a 1.7.10 mod up to 1.8.9:
- Every `world.getBlock(x, y, z)` call becomes `world.getBlockState(pos).getBlock()`
- Every `world.setBlock(x, y, z, block, meta, flags)` call becomes
  `world.setBlockState(pos, block.getDefaultState(), flags)` (or with properties set)
- Every entity/block position stored as three ints needs to become a `BlockPos`
- This is pervasive — expect it in every file that touches world state

## The second biggest change: rendering system

1.7.10: `ISimpleBlockRenderingHandler`, `IItemRenderer`, Techne models
1.8.9: JSON block/item models under `assets/<modid>/models/`, `ModelLoader` registration

This is not a porting task — this is a rewrite of the rendering layer. Plan for it.

## Networking

`SimpleNetworkWrapper` exists in both versions but with slightly different registration
patterns. Verify method signatures against each version's Forge source.

## Recipes

Code-registered in both versions via `GameRegistry`. No JSON recipes exist in either era.
Port is relatively straightforward, but verify `ItemStack` constructor signatures per version.

## Direction-specific notes

**1.7.10 → 1.8.9 (upport):**
- Rewrite all x/y/z to BlockPos
- Rewrite all block+meta to IBlockState + properties
- Rewrite the entire rendering layer to JSON models
- Update toolchain: FG1.2 → FG2.1, MCP stable_12 → stable_22, Java 7/8 → Java 8

**1.8.9 → 1.7.10 (downport — harder):**
- Rewrite all BlockPos back to x/y/z ints
- Rewrite all IBlockState back to block+meta
- Rewrite the entire rendering layer from JSON to ISimpleBlockRenderingHandler
- Update toolchain: FG2.1 → FG1.2, MCP stable_22 → stable_12
- A downport is generally more work than an upport for this version pair
