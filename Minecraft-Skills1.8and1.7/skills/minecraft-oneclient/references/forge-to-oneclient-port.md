# Porting a Forge 1.8.9 mod to OneClient

## The short version

If your mod is a standard content mod (new blocks, items, mobs, mechanics) with no
Lunar-specific or client-specific hooks, it almost certainly already works on
OneClient without any changes. OneClient runs standard Forge 1.8.9 — drop the JAR
in the mods folder and test.

If your mod hooks into Lunar Client's internals (obfuscated class targets, no-FML
Mixin targets), those hooks will not work on OneClient because OneClient has a
different internal structure. The hook layer needs to be rewritten for OneClient's
specific internals — see `oneclient-loader.md` for how to discover what those are.

## Steps for a content mod

1. Confirm the OneClient mods folder path (see oneclient-loader.md)
2. Build the mod against plain Forge 1.8.9-11.15.1.2318 as normal
3. Copy the output JAR to the OneClient mods folder
4. Launch OneClient and check the FML log for successful mod load
5. Test the mod's features in-game

## Steps for a mod with client-specific hooks

1. Inventory OneClient's own coremod/patch layer (see oneclient-loader.md step 1)
2. Identify the specific hook point you need in OneClient's internals
3. Decide: Mixin or coremod (`IFMLLoadingPlugin` + `IClassTransformer`)?
   - If OneClient itself uses Mixin, Mixin is probably the cleaner choice
   - If OneClient uses raw coremods, match that approach for compatibility
4. Write the hook targeting OneClient's specific class names
5. Test with Forge's debug output enabled to confirm the hook applied
