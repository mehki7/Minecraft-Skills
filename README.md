# Lunar Client 1.8.9 Port Kit

Skill pack for porting Minecraft 1.8.9 mods onto Lunar Client.

## Start here: TARGET.md

`TARGET.md` is the single source of truth. Every ABI fact (class names,
method descriptors, Searge names, confirmed behaviors) is pinned there with
evidence. Read it before touching any code. Nothing marked UNVERIFIED in
TARGET.md may be treated as settled anywhere else in this pack.

## Two hard rules, before anything else

1. **Every vanilla method and field name must be Searge** (`func_78472_g`,
   `field_74333_Y`). MCP names (`updateLightmap`, `gammaSetting`) do not
   exist in the running game and fail silently. This applies to `@Inject`
   strings AND to ordinary call sites in your compiled code.
2. **`defaultRequire: 1`** in every mixin JSON, so a wrong name throws
   instead of being skipped in silence.

## Step 0 — run the smoke test first

The smoke test proves the Mixin pipeline works on YOUR install before you
write any port code. See `Example Mod for 1.8/smoketest/` — it has the
build commands, and its manifest and mixin JSON are the template for every
new port.

Drop the jar in the mods folder, launch, join a world. Both of these must
appear in `latest.log`:

    [SMOKETEST] *** SMOKE TEST PASS -- plugin onLoad fired
    [SMOKETEST] *** INJECT PASS -- updateLightmap HEAD fired

Both lines = pipeline confirmed. One or both missing = stop and debug.

## Skills (4)

| Skill | Status | Purpose |
|---|---|---|
| `skills/minecraft-lunar-client/` | VERIFIED | Lunar-specific Mixin doctrine; canonical port workflow |
| `skills/minecraft-legacy-modding-189/` | VERIFIED | 1.8.9 game API, vanilla class/method knowledge |
| `skills/minecraft-legacy-modding-1710/` | UNVERIFIED | 1.7.10 knowledge — no tsrg coverage confirmed |
| `skills/minecraft-oneclient/` | UNVERIFIED | OneClient — no names confirmed |

Do not use the 1710 or oneclient skills for production port work until
RECON is run and TARGET.md is updated.

## Example mods

- `Example Mod for 1.8/smoketest/` — the canonical build example. Copy its
  folder layout, manifest keys, and mixin JSON for every new port.
- `Example Mod for 1.8/port-guiingame/` — first real port. `@Inject` at
  TAIL of `func_175180_a` (`GuiIngame.renderGameOverlay`).
- `Example Mod for 1.8/Example-1.8.9-Mod/` — Kotlin/Architectury Loom
  template. Reference only, not the Lunar pattern. See `README-EXAMPLE.md`.

## Mods folder (VERIFIED)

    C:\Users\<user>\.lunarclient\profiles\1.8-furiahvisuals\mods\

Drop a `.jar` here; Lunar picks it up with zero configuration and no launch
arguments. Confirmed 2026-10-29.

## Doctrine

- **Forge events work** — `@SubscribeEvent` fires. Confirmed by a live
  Searge-compiled mod (`EntityJoinWorldEvent`). Use events for entity
  spawn, tick, and HUD work.
- **Mixin for what events can't reach** — renderer internals, shader-level
  effects. FuriahVisuals itself is Mixin-based for this reason.
- Use `@Inject`, not `@Overwrite` — FuriahVisuals hooks the same classes.
- Compile at Java 8 with `-proc:none`, classpath
  `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` so `func_` names resolve.
- Name source of truth: `lunar2searge.tsrg` at
  `C:\Users\<user>\AppData\Roaming\.minecraft\.ichor\lunar2searge.tsrg`