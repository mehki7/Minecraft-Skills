# Debugging on OneClient

## Enable FML and Forge debug output

Launch with:
```
-Dfml.debugClassLoading=true
-Dfml.debugClassLoadingFine=true
```

The FML log (`logs/fml-client-latest.log`) will show all class transformers applied,
all coremods loaded, and any transform failures. This is the primary diagnostic tool.

## Common failure shapes

- **Mod does not appear in the mod list:** FML did not discover the mod JAR. Check
  that the JAR is in the correct mods folder (confirm path per `oneclient-loader.md`),
  that the JAR has a valid `mcmod.info`, and that the FML log shows it being scanned.
- **Mod loads but features do not work:** The FML lifecycle hook may not have fired,
  or a GameRegistry call failed silently. Add logging to your `@EventHandler` methods
  to confirm they are being called.
- **Coremod not applying:** Check that the `FMLCorePlugin` attribute in `MANIFEST.MF`
  is spelled correctly and that the implementing class is on the classpath inside the JAR.
  The FML log will list loaded coremods at startup — confirm yours appears.
- **Mixin not applying (if using Mixin):** Check that the mixin config is referenced
  in the jar manifest (`MixinConfigs` attribute) and that the config file is inside
  the JAR at the declared path. Mixin will log applied mixins if you launch with
  `-Dmixin.debug=true -Dmixin.checks=true`.
- **OneClient-specific crash after mod load:** Check whether OneClient's own coremod
  conflicts with your class transformer. If both your transformer and OneClient's
  transformer modify the same class, transform ordering matters — OneClient's
  transformer runs first (it was registered by its own `IFMLLoadingPlugin`).

## A compile is not a runtime test

Same rule as for any Forge mod: a successful build proves the Java is syntactically
valid. It says nothing about whether hooks fire, events dispatch, or features work
in the actual game. Always test in a real OneClient launch before marking work done.
