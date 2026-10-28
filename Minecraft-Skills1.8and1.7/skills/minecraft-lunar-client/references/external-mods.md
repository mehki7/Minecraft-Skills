# External mods folder — STATUS: UNVERIFIED for 1.8.9 specifically

Public documentation for Lunar's **modern** Fabric-based mod support
describes a per-profile mods folder:

```
~/.lunarclient/profiles/<profile-name>/mods/
```

That documentation is for current Minecraft versions using Lunar's
built-in Fabric loader. It is **not confirmed** to apply to the 1.8.9
canary/offline lane, which (per TARGET.md) uses a completely different,
Mixin-based mechanism with no Fabric involved at all.

## What's actually confirmed instead

The 1.8.9 lane's code lives in
`.lunarclient/offline/multiver/legacy-0.1.0-SNAPSHOT-all-nomappings.jar`
— this is Lunar's own bundled code, not a folder you drop your mod into.
There is currently no confirmed drop-in external mods folder for this
specific lane.

## How to resolve this

1. Check the Lunar launcher's Settings for a "game directory" or "mods
   folder" path while the 1.8.9 profile specifically is selected (not a
   modern version profile) — this is the fastest direct confirmation.
2. Search the extracted mixin configs for any class whose job looks like
   "scan a folder and load jars from it" — that would mean Lunar itself
   has an external-mod-loading mixin for this lane, and its target folder
   would be hardcoded or configurable somewhere nearby.
3. If no official mechanism exists for 1.8.9, the realistic fallback is:
   your mod doesn't load as an "external mod" at all — it gets built
   directly as another mixin bundle, dropped alongside
   `legacy-0.1.0-SNAPSHOT-all-nomappings.jar`, and wired into Lunar's own
   mixin config loading (if that's even configurable) or compiled into a
   fork of that jar. This is a meaningfully bigger undertaking than
   "drop a jar in a folder" — confirm which situation you're actually in
   before committing to a build approach.

Do not assume the `profiles/<name>/mods` path works here until step 1
confirms it for the 1.8.9 profile specifically.
