# Lunar's loader mechanics

## What Lunar is, structurally

Lunar Client is built on `LunarClient/LegacyLauncher`, a public fork of
Mojang's old LaunchWrapper: a classloader with class-name mapping and
bytecode-transforming built in. That's the host process. There's no FML
sitting on top of it for the 1.8 lane — the only transformer doing
anything is Mixin.

## The jar layout you'll actually see on disk

Everything for the "offline multiver" setup lives under
`.lunarclient/offline/multiver/` (confirmed path — see TARGET.md). Relevant
files for 1.8.9 specifically:

| File | What it is |
|---|---|
| `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` | The actual 1.7/1.8/1.12 mixin classes + configs |
| `lunar-platform-mappings-v1_8.jar` | Presumed mapping/retrace data for 1.8 (unverified contents) |
| `lunar.jar` | The core/shared Lunar client code, not version-specific |
| `Forge_v1_8.jar` | A separate file — relationship to the mixin-based lane is UNVERIFIED. Could be a real standalone Forge jar Lunar can launch into as an alternate path. Worth checking before assuming the mixin route is the only one. |
| `OptiFine_v1_8.jar` / `optifine-...-all.jar` | OptiFine integration, separate concern from modding |

## Why there's no lifecycle

Forge gives you `@Mod`, `FMLPreInitializationEvent`, a registry API,
because FML is designed to host arbitrary third-party mods safely. Lunar's
mixin configs are declaring `"required": true` and a `"target": "CLIENT"`
— this is Lunar patching its *own* client, not hosting a plugin API for
you. Anything you add has to look, to Mixin, exactly like one more of
Lunar's own first-party patches. There's no boundary that keeps a broken
mixin from affecting the whole client process.

## Open question worth resolving early

Whether `Forge_v1_8.jar` is a legitimate alternate launch route is a cheap
check that could save a lot of mixin work — if Lunar can launch straight
into real Forge 1.8.9 for a profile, normal Forge modding conventions
(from `minecraft-legacy-modding`) apply instead of any of this. Check
Lunar's launcher UI for a version/profile dropdown that mentions Forge
directly, and confirm whether selecting it changes which jar actually
loads.
