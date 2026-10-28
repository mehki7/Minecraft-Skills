# Mixin in the 1.7/1.8/1.12 era

Mixin existed during this era but was not Forge's primary hook mechanism
— coremods (`IFMLLoadingPlugin` + `IClassTransformer`, raw ASM) were the
"native" Forge way to do bytecode-level patching, and Mixin was more of a
bolt-on option some mod authors used.

## Key era-specific facts

- Typical Mixin versions seen in this era: 0.7.x-0.8.x line.
  (Confirmed on Lunar's own 1.8 lane: `"minVersion": "0.8"` — see
  `minecraft-lunar-client`'s TARGET.md.)
- `compatibilityLevel` is normally `JAVA_6` or `JAVA_8` for genuine
  1.8.9-era Forge projects targeting the original Java 8 toolchain. This
  is NOT universal — Lunar's own bundled 1.8 mixins declare `JAVA_17`
  (confirmed), because Lunar's client itself runs on a modern JVM even
  while emulating 1.8.9 game logic. Check which situation applies before
  assuming either value.
- Refmaps: in genuine old Forge+MCP projects, a refmap lets your mixin
  target MCP/searge names and get remapped to obfuscated names at
  runtime/build time automatically. This requires the refmap-generation
  tooling to be wired into your build (annotation processor output).
  When that tooling isn't set up, or when you're targeting hardcoded
  names directly (as Lunar's own shipped configs do — no refmap key),
  disable it explicitly: `mixin.env.disableRefMap=true`, empty
  `"refmap": ""`, and `remap = false` per-mixin.

## When to use Mixin vs a coremod for a legacy Forge port

If the original mod you're porting used a coremod/`IClassTransformer`,
you can often re-implement the same patch as a Mixin instead — Mixin is
generally easier to maintain and less fragile against version drift than
hand-written ASM. This is a reasonable modernization to make during a
port, not scope creep, as long as the resulting hook point and behavior
match the original.
