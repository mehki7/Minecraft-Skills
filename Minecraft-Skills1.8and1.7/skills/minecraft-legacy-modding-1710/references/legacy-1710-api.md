# 1.7.10 API surface notes

## Core FML API

- Main class: `@Mod(modid = "yourmod", version = "1.0", name = "Your Mod")`
- Lifecycle hooks: `@EventHandler` on `FMLPreInitializationEvent`, `FMLInitializationEvent`,
  `FMLPostInitializationEvent`, `FMLServerStartingEvent`
- Event bus: `MinecraftForge.EVENT_BUS.register(this)` in pre-init or init
- Client-only code: `@SideOnly(Side.CLIENT)`

## Registration

```java
// Blocks
GameRegistry.registerBlock(MyBlock.instance, "myblock");

// Items
GameRegistry.registerItem(MyItem.instance, "myitem");

// Recipes
GameRegistry.addRecipe(new ItemStack(MyItem.instance), "XXX", "X X", "XXX", 'X', Items.iron_ingot);

// Entities
EntityRegistry.registerModEntity(MyEntity.class, "MyEntity", entityId, this, 80, 3, true);
```

## Rendering (pre-JSON)

```java
// Block renderer registration (in client proxy)
RenderingRegistry.registerBlockHandler(new MyBlockRenderer());

// Item renderer (in client proxy)
MinecraftForgeClient.registerItemRenderer(MyItem.instance, new MyItemRenderer());

// ISimpleBlockRenderingHandler interface:
// renderWorldBlock, renderInventoryBlock, shouldRender3DInInventory, getRenderId
```

## Networking

```java
SimpleNetworkWrapper network = NetworkRegistry.INSTANCE.newSimpleChannel("yourmod");
network.registerMessage(MyMessageHandler.class, MyMessage.class, 0, Side.SERVER);
network.registerMessage(MyMessageHandler.class, MyMessage.class, 1, Side.CLIENT);
```

## Key differences from 1.8.9 to watch for

- `ItemStack(Block/Item, quantity, damage)` constructor: same shape, but verify
  method signatures against the pinned Forge jar — minor differences exist.
- `EntityPlayer.getEquipmentInSlot(slot)` slot numbering: 0 = held, 1-4 = armor.
  Same as 1.8.9, but verify against actual source.
- World operations: `world.getBlock(x, y, z)` in 1.7.10 vs `world.getBlockState(pos)`
  in 1.8.9. The coordinate/BlockPos system is a major 1.8.x change — 1.7.10 still
  uses raw `int x, y, z` throughout.
- `IBlockAccess.getBlock(x, y, z)` / `setBlock(x, y, z, block, meta, flags)` — the
  pre-BlockState API. Every block interaction uses raw x/y/z, not BlockPos.

## MCP stable_12 name examples (compared to stable_22)

MCP mapping names can differ between stable_12 (1.7.10) and stable_22 (1.8.9).
Do not assume a name that works in 1.8.9 source is correct in 1.7.10 source.
Verify against the actual stable_12 mappings or against a known working 1.7.10 mod.
