---
name: minecraft-legacy-modding-189
description: Plain Forge 1.8.9 modding (Forge 1.8.9-11.15.1.2318, Java 8, MCP stable_22, ForgeGradle 2.1). Use when the target is vanilla+Forge 1.8.9 specifically, not Lunar or OneClient. Covers old MCP mappings, Mixin basics, FML lifecycle, and Java 8 toolchain. Use when the target is plain vanilla+Forge, not Lunar Client. Pair with minecraft-lunar-client when the actual target is Lunar Client. Versions 1.9 through 1.12.2 and anything newer are out of scope.
---

# Legacy Minecraft modding — 1.8.9 (primary) / 1.7.10 (secondary)

This covers the general old-Minecraft modding landscape for plain Forge.
If the actual target is Lunar Client (not plain vanilla+Forge), read
`minecraft-lunar-client` as well — Lunar breaks several of the default
assumptions below (most importantly: Lunar's 1.8 lane is Java 17, not Java 8).

**Version scope:** 1.8.9 is the primary target. 1.7.10 is secondary.
Everything newer than 1.8.9, including 1.12.2, is **out of scope**.
Do not apply 1.12.2 patterns, APIs, or toolchains here.

## Routing

| Need | Read |
|---|---|
| Mixin basics for this era (vs Forge coremods) | [mixin-189.md](references/mixin-189.md) |
| What replaces `GameRegistry` when there is no loader lifecycle | [no-loader-registration.md](references/no-loader-registration.md) |
| Toolchain/Gradle setup for this era | [java8-gradle.md](references/java8-gradle.md) |
| API surface specific to 1.8.9 | [legacy-189-api.md](references/legacy-189-api.md) |
| 1.7.10 differences vs 1.8.9 | [legacy-1710-diffs.md](references/legacy-1710-diffs.md) |
| Behavior recovery and reference comparisons | [behavior-recovery.md](references/behavior-recovery.md) |
| Testing and packaging a legacy mod | [testing-release.md](references/testing-release.md) |

## Default assumptions for plain Forge 1.8.9 (`1.8.9-11.15.1.2318`)

- Java 8 toolchain, ForgeGradle 2.1-era conventions
- MCP stable_22 mappings
- Full FML lifecycle: `@Mod`, `FMLPreInitializationEvent`, `@SubscribeEvent` on
  `MinecraftForge.EVENT_BUS`, `GameRegistry`, `@SideOnly`, `ObfuscationReflectionHelper`
- Mixin exists but is a bolt-on, not the default. Coremods (`IFMLLoadingPlugin` +
  `IClassTransformer`) are the native Forge way of doing ASM-level patching.

**Confirmed exception:** If the actual target is Lunar Client's bundled 1.8 lane
rather than plain Forge, none of the above FML/Java-8 assumptions hold.
Lunar's shipped mixin configs declare `"compatibilityLevel": "JAVA_17"`.
See `minecraft-lunar-client`'s TARGET.md for the raw evidence.
Do not default to "1.8.9 = Java 8" without first confirming which of the two
situations you are actually in.

## Coverage map template

For any porting or modding task, record before writing code:

| Feature/system | Source API (1.8.9 or 1.7.10) | Implementation status | Behavior difference |
|---|---|---|---|
| (your system) | (exact class/method) | proposed | — |

Use `implemented`, `adapted`, `omitted`, `blocked`, or `unverified` precisely.
Check actual behavior beyond compilation: damage, state, ownership, persistence,
cleanup. A successful compile is not a gameplay pass.

## Anti-patterns

- Copying 1.20.1-era ForgeGradle 6 / Java 17 patterns onto plain Forge 1.8.9.
- Copying modern (1.16+, 1.21.x) asset path conventions onto a 1.8.9 resource pack —
  pack format is completely different.
- Assuming Mixin's default remapper handles everything on this era. With old/incomplete
  refmap tooling, direct-name + `remap = false` is often the pragmatic choice.
- Assuming 1.7.10 and 1.8.9 APIs are identical. They are not — especially
  rendering and networking. See legacy-1710-diffs.md.
- Applying anything from this guide to 1.12.2 — that is a different era, different
  Forge, different toolchain. It is out of scope here.
