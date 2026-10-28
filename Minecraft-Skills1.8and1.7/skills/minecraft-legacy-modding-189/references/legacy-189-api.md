# 1.8.9 API surface notes

## Plain Forge 1.8.9

Standard FML-era API: `@Mod`, `FMLPreInitializationEvent`/
`FMLInitEvent`/`FMLPostInitializationEvent`, `@SubscribeEvent` on
`MinecraftForge.EVENT_BUS`, `@SideOnly(Side.CLIENT)` for client-only
code, `ObfuscationReflectionHelper` for reaching obfuscated vanilla
members from source that uses MCP names (Forge remaps this for you at
runtime via its own deobfuscation data).

## What's different about this 1.8.9 vs later Forge versions worth
   knowing before porting a mod written for, say, 1.12.2 down to 1.8.9

- Texture/model systems differ meaningfully between 1.8.x and 1.12.x —
  don't assume a 1.12.2 mod's rendering code ports 1:1.
- Networking API (`SimpleNetworkWrapper` etc.) exists in both eras but
  specific method signatures can differ across minor Forge builds within
  even the same MC version — check against the actual pinned Forge build
  (`1.8.9-11.15.1.2318`) rather than a general "1.8.x Forge" assumption.

## If the actual target is Lunar, not plain Forge

None of this FML-era API applies at all — see `minecraft-lunar-client`.
Do not mix vanilla-Forge API assumptions into Lunar-targeted mixin code;
they're unrelated systems that happen to share a Minecraft version
number.
