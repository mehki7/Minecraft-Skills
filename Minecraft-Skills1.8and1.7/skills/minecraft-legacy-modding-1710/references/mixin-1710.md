# Mixin as a bolt-on in 1.7.10

Mixin 0.7.x was used by some 1.7.10 mods as a bolt-on alternative to raw coremods
(`IFMLLoadingPlugin` + `IClassTransformer`). It was not the default — coremods were
the native Forge approach for ASM-level patching in this era.

## Should you use Mixin for a 1.7.10 mod?

For a plain Forge 1.7.10 mod (not Lunar, not OneClient), using a coremod
(`IFMLLoadingPlugin`) is generally more straightforward and better documented for
this era. Use Mixin only if:
- You have a specific reason to prefer the Mixin API over raw ASM
- You are porting a Mixin-based mod from another version and want to preserve structure

If targeting OneClient or Lunar (which have their own mixin setups), see those
skills instead — the configuration differs.

## If you do use Mixin on plain Forge 1.7.10

- Mixin version: 0.7.x era
- `compatibilityLevel`: `JAVA_7` or `JAVA_8` depending on your toolchain
- A refmap can be used with MCP stable_12 names if the build annotation processor
  is correctly wired (see FG1.2 limitations — this can be fiddly to set up)
- Or disable refmap and use direct names with `remap = false`

In most cases for 1.7.10 plain Forge, a coremod is less work than wiring Mixin's
build pipeline correctly into a FG1.2 project.
