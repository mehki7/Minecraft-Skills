# Mixin vs coremod on OneClient

## Decision rule

First: inventory what OneClient itself uses (see `oneclient-loader.md`).

- **If OneClient bundles its own Mixin setup:** using Mixin for your own hooks is
  probably safe — OneClient's classloader already handles Mixin, so the pipeline
  is confirmed to exist. Use it.
- **If OneClient only uses raw coremods (`IFMLLoadingPlugin`):** Mixin is not
  confirmed to be wired in. Either use a raw coremod too, or verify that you can
  add Mixin as a dependency without conflicting with OneClient's classloader.
- **If OneClient uses neither** (pure standard Forge): standard Forge events and
  `@SubscribeEvent` are the right approach. No bytecode patching needed.

## Raw coremod approach (if needed)

```java
// In the META-INF/MANIFEST.MF of your jar:
// FMLCorePlugin: your.package.YourCoremodPlugin

public class YourCoremodPlugin implements IFMLLoadingPlugin {
    @Override
    public String[] getASMTransformerClass() {
        return new String[] { "your.package.YourTransformer" };
    }
    // ... other methods return null or empty
}

public class YourTransformer implements IClassTransformer {
    @Override
    public byte[] transform(String name, String transformedName, byte[] basicClass) {
        if (transformedName.equals("net.minecraft.client.Minecraft")) {
            // ASM transform here
        }
        return basicClass;
    }
}
```

MCP stable_22 names are available at dev time; the `transformedName` param gives you
the deobfuscated name in a dev environment and the obfuscated name in prod — handle both.

## Mixin approach (if confirmed available)

Same pattern as plain Forge 1.8.9 Mixin bolt-on. The toolchain wiring is the tricky
part — the annotation processor must generate a refmap, and the refmap must be wired
into the jar manifest correctly. Verify this actually works in the OneClient
environment before committing to Mixin for a hook.
