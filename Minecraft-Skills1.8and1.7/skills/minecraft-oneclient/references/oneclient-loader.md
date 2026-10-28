# OneClient loader mechanics — STATUS: PARTIALLY VERIFIED

OneClient is a Forge 1.8.9 based client. Unlike Lunar Client (which has no FML),
OneClient sits on top of Forge and in principle exposes the full FML lifecycle.

## What is confirmed

- OneClient ships as a modified Minecraft+Forge client that runs the standard
  Forge 1.8.9 FML bootstrap.
- Standard Forge mods (`.jar` files in the `mods/` folder) load normally via FML.
- The mods folder for OneClient follows the standard Forge convention:
  `.minecraft/mods/` (or the OneClient-specific game directory's `mods/` folder).

## What is NOT yet fully confirmed

- [ ] Whether OneClient bundles its own coremods (`IFMLLoadingPlugin` implementations)
      that modify class loading before standard Forge initializes.
- [ ] Whether OneClient's own client features (minimap, cosmetics, hit indicators, etc.)
      are implemented as coremods, mixins, or shader-level patches — this matters if
      you want to hook into or interact with those features.
- [ ] Exact game directory path when launched through OneClient's launcher vs through
      a standard Forge profile.
- [ ] Whether OneClient overrides the `mods/` folder location.

## How to confirm the unknowns

1. Launch OneClient and check the FML/Forge log at startup — it will list all loaded
   coremods and transformers. This tells you exactly what OneClient bundles on top
   of standard Forge.
2. Check OneClient's install directory for any jars that are not standard Forge
   artifacts — these may be OneClient's own coremod/patch jars.
3. If OneClient has a `config/` folder, check it for any transformer or classloader
   configuration files.

## Loading your mod

For a standard content mod with no OneClient-specific hooks:
- Build as a normal Forge 1.8.9 mod (see `minecraft-legacy-modding-189`)
- Drop the JAR in the `mods/` folder (confirm exact path as above)
- This should work without any OneClient-specific modification

For a mod that hooks into OneClient's own features:
- First inventory OneClient's own coremod/patch layer (step 1 above)
- Then write your hook targeting OneClient's specific classes
- This is analogous to the Lunar mixin approach, but confirm whether OneClient
  uses Mixin or raw ASM coremods before writing any hook code
