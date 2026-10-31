---
name: minecraft-legacy-modding-189
description: General knowledge for modding Minecraft 1.8.9 specifically — old MCP mappings, Mixin basics, Java 8-era tooling. Use for plain Forge 1.8.9 targets. Pair with minecraft-lunar-client when the actual target is Lunar Client, and with minecraft-legacy-modding-1710 for 1.7.10 work.
---

# Legacy Minecraft modding (1.8.9)

This covers the general 1.8.9 modding landscape. If the actual
target is Lunar Client (not plain vanilla+Forge), read
`minecraft-lunar-client` as well — Lunar breaks several of the default
assumptions below. For 1.7.10 work, pair with `minecraft-legacy-modding-1710`.

## Default assumptions for this era — and the one exception

For **plain Forge 1.8.9** (`1.8.9-11.15.1.2318`):
- Java 8 toolchain, ForgeGradle 2.1-era conventions
- MCP stable_22 mappings
- Full FML lifecycle: `@Mod`, `FMLPreInitializationEvent`,
  `@SubscribeEvent` on `MinecraftForge.EVENT_BUS`, `GameRegistry`,
  `@SideOnly`, `ObfuscationReflectionHelper`
- Mixin exists in this era but is a bolt-on, not the default hook
  mechanism — coremods (`IFMLLoadingPlugin` + `IClassTransformer`) are
  the "native" Forge way of doing ASM-level patching.

**Exception, confirmed by direct testing (not a guess):** if the actual
target is Lunar Client's bundled 1.8 lane rather than plain Forge, none
of the above FML/Java-8 assumptions hold. See `minecraft-lunar-client`
and TARGET.md for the full confirmed picture.

## Anti-patterns

- Copying 1.20.1-era ForgeGradle 6 / Java 17 patterns onto plain Forge
  1.8.9 — wrong toolchain for that target.
- Copying modern (1.21.x) asset path conventions onto a 1.8.9 resource
  pack — pack format is completely different.
- Assuming Mixin's default remapper handles everything — on this era,
  direct-name + `remap = false` is often the pragmatic choice, same as
  the Lunar-specific guidance.

---

## Toolchain and Gradle for this era

### Plain Forge 1.8.9 target

- Java 8, ForgeGradle 2.1-era conventions.
- MCP stable_22 mappings.
- `build.gradle` uses the old `buildscript { ... }` ForgeGradle plugin
  application style (not the modern plugin DSL), and version/mappings are
  declared via `minecraft { version = "1.8.9-11.15.1.2318" ... }`-style
  blocks specific to that ForgeGradle generation.

### Lunar-targeting external mod build (not plain Forge)

**Confirmed by smoke test (2026-10-29):** Java 8 (javac 1.8.0_504)
compiles external mixin jars that load correctly inside Lunar's 1.8 lane.
Compile with `-proc:none` to skip the Mixin annotation processor (avoids
a Gson dependency error). Lunar's own shipped mixin classes use
`compatibilityLevel: JAVA_17`, but external mod jars compiled at Java 8
load without issue alongside them.

Do NOT assume you need Java 17 just because Lunar's internal lane
declares it — that applies to Lunar's own code, not to the jars you drop
in the mods folder.

### General rule

Never write a Gradle file that says "use Java 8" or "use modern Forge"
as a blanket default for "1.8.9 modding." The actual correct toolchain
depends on whether the target is plain Forge (Java 8) or Lunar (Java 8
for external mods, confirmed). State which one explicitly.

---

## 1.8.9 API surface

### Plain Forge 1.8.9

Standard FML-era API: `@Mod`, `FMLPreInitializationEvent`/
`FMLInitEvent`/`FMLPostInitializationEvent`, `@SubscribeEvent` on
`MinecraftForge.EVENT_BUS`, `@SideOnly(Side.CLIENT)` for client-only
code, `ObfuscationReflectionHelper` for reaching obfuscated vanilla
members from source that uses MCP names.

### Porting a 1.12.2 mod down to 1.8.9

- Texture/model systems differ meaningfully between 1.8.x and 1.12.x —
  don't assume a 1.12.2 mod's rendering code ports 1:1.
- Networking API exists in both eras but specific method signatures can
  differ — check against the pinned Forge build (`1.8.9-11.15.1.2318`).

### If the actual target is Lunar, not plain Forge

None of this FML-era API applies. See `minecraft-lunar-client`. Do not
mix vanilla-Forge API assumptions into Lunar-targeted mixin code.

---

## Mixin in the 1.8.9 era

Mixin existed during this era but was not Forge's primary hook mechanism
— coremods (`IFMLLoadingPlugin` + `IClassTransformer`, raw ASM) were the
"native" Forge way to do bytecode-level patching.

### Key era-specific facts

- Typical Mixin versions seen in this era: 0.7.x–0.8.x line.
  (Confirmed on Lunar's own 1.8 lane: `"minVersion": "0.8"`)
- `compatibilityLevel` is normally `JAVA_6` or `JAVA_8` for genuine
  1.8.9-era Forge projects. Lunar's own bundled 1.8 mixins declare
  `JAVA_17` (confirmed) — check which situation applies.
- **Searge names required on Lunar (confirmed):** Lunar's Ichor pipeline
  remaps vanilla Minecraft bytecode to Searge names (e.g. `func_78472_g`)
  BEFORE Mixin processes. Using MCP names (e.g. `updateLightmap`) with
  `remap=false` fails silently due to `defaultRequire: 0`. Always use
  the Searge name from TARGET.md or query `lunar2searge.tsrg` directly.
  Evidence: `@Inject(method="updateLightmap")` → no log line;
  `@Inject(method="func_78472_g")` → inject fired at `[19:32:19]`.
- Refmaps: in genuine old Forge+MCP projects, a refmap lets your mixin
  target MCP names and get remapped automatically. When targeting Lunar
  directly, disable it: use `-proc:none` at compile time, set
  `"injectors": { "defaultRequire": 0 }` in JSON, and use Searge names
  with `remap=false`.

### When to use Mixin vs a coremod for a legacy Forge port

If the original mod used a coremod/`IClassTransformer`, you can often
re-implement the same patch as a Mixin — Mixin is generally easier to
maintain. This is a reasonable modernization during a port, not scope
creep, as long as the hook point and behavior match the original.

---

## When there's no loader lifecycle to register against

Plain Forge gives you `GameRegistry.registerItem(...)` etc., called
during `FMLInitEvent`. When targeting Lunar (no FML lifecycle), you work
directly against vanilla 1.8.9's own registries:

- `Block.blockRegistry`
- `Item.itemRegistry`

Registering directly into these at the right point in the vanilla
bootstrap is the vanilla-style equivalent. Find the injection point via
Mixin, targeting wherever vanilla's own bootstrap populates these
registries — confirm the exact method via TARGET.md or RECON rather than
guessing a vanilla 1.8.9 method name from memory.

### Side-effects to watch for

Forge's registry system handles ID allocation, network sync for
multiplayer, and NBT persistence. Registering directly into vanilla's
registries bypasses all of that. For a purely client-side visual/QoL mod
(the more common Lunar use case), this mostly doesn't matter, but say
explicitly which case you're in before assuming it's safe to skip.
FIX 5 — README.md (full rewrite)
markdown
# Minecraft Skills — Lunar 1.8.9 Port Kit

Skill pack and runtime name table for porting 1.8.9 Forge mods onto
Lunar Client. Active target mods: FuriahVisuals (in progress) and
MoBends 1.7.10 backport (not started).

---

## Start here: TARGET.md

`TARGET.md` (repo root) is the single source of truth for what's
actually confirmed at runtime vs still unverified. Read it before
writing any mixin code. Never assert a class, method, or field name
that TARGET.md marks UNVERIFIED.

Key verified entries (as of 2026-10-29):
- `func_78472_g` = `updateLightmap(F)V` on `EntityRenderer` — tsrg + live inject
- 10 classes, 10 methods, 1 field confirmed
- External mods path: `.lunarclient\profiles\<profile>\mods\` — VERIFIED

---

## Step 0 before anything else: run the smoke test

Source in `Example Mod for 1.8/smoketest/`. Build commands:

```bat
javac -proc:none -cp FuriahVisuals.jar -d classes SmokePlugin.java MixinEntityRendererSmoke.java
jar cfm smoketest.jar META-INF\MANIFEST.MF -C classes . mixins.smoketest.json mcmod.info
copy smoketest.jar ".lunarclient\profiles\<profile>\mods\"
```

Launch, join a world, quit. Run:

```bat
findstr "SMOKETEST" .lunarclient\profiles\<profile>\logs\latest.log
```

You need both lines:
- `*** SMOKE TEST PASS -- plugin onLoad fired ***`
- `*** INJECT PASS -- updateLightmap HEAD fired ***`

If either is missing, stop and debug before writing real mod code. See
`skills/minecraft-lunar-client/SKILL.md` Debugging section.

---

## Skills in this pack

Install skills from the `skills/` folder. Four skills:

| Skill folder | When to use |
|---|---|
| `minecraft-lunar-client` | Any Lunar Client 1.8 porting work — load this first |
| `minecraft-legacy-modding-189` | Plain Forge 1.8.9 background, MCP mappings, Mixin basics. Pair with the Lunar skill. |
| `minecraft-legacy-modding-1710` | 1.7.10 lane only. **Mapping work NOT started. Unverified.** |
| `minecraft-oneclient` | OneClient-specific work. **Unverified on current builds.** |

The 1.8.9 lane is the only proven lane. Do not rely on 1710 or oneclient
skills for production porting work without first doing RECON and
updating TARGET.md.

---

## HANDOFF.md

`HANDOFF.md` (repo root) contains the full session history: what was
confirmed, what was corrected, and the next session starting point.

---

## `Example Mod for 1.8/`

- `smoketest/` — the canonical build example. Use this.
- `Example-1.8.9-Mod/` — a Kotlin Architectury Loom template, kept for
  reference only. Not the Lunar pattern. See `README-EXAMPLE.md` in that
  folder.

---

## `Minecraft-Skills Rewrite/`

In-progress rewrite. Do not delete or modify.

---

## Key facts confirmed by smoke test (2026-10-29)

- Vanilla MC class names are NOT obfuscated by Ichor
- Vanilla MC method/field names ARE remapped to Searge names
- Searge names must be used in `remap=false` injections
- Java 8 external mods load fine alongside Lunar's Java 17 internal lane
- No JVM arguments needed — manifest `MixinConfigs` is the only mechanism
- `Forge_v1_8.jar` in `offline/multiver/` is UNVERIFIED — check the
  Lunar launcher for a Forge profile before writing mixin code