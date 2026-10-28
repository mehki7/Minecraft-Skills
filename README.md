# lunar-189-port-kit

Two agent skills + recon tooling for porting client-side Minecraft mods
onto Lunar Client's 1.8.9 "legacy" lane.

## Order to use this in

1. Read `TARGET.md` first, always. It's the one file that says what's
   actually confirmed vs still a guess, and it's based on real evidence
   pulled from an actual Lunar install (2026-10-27), not assumption.
2. If something you need is marked UNVERIFIED in `TARGET.md`, run the
   matching script in `RECON/` against your own install before trusting
   it. Right now that's just `RECON/02-mine-mixin-targets.py` (resolves
   which vanilla class a given mixin targets) — more RECON scripts can be
   added the same way as more unknowns come up.
3. Drop `skills/minecraft-legacy-modding/` and `skills/minecraft-lunar-client/`
   into your coding agent's skills folder. The agent should read
   `minecraft-lunar-client/SKILL.md` first for anything Lunar-specific —
   it links back to `TARGET.md` itself.

## Why two skills instead of one

`minecraft-legacy-modding` covers the general 1.7/1.8/1.12 modding
landscape (plain Forge era conventions). `minecraft-lunar-client` covers
what's specific to Lunar's own closed, obfuscated, Mixin-only client,
which breaks several of the general era's default assumptions (most
notably: Lunar's 1.8 lane runs Java 17, not Java 8 — confirmed, not a
guess). Keeping them separate means an agent reading only one doesn't
accidentally inherit the wrong toolchain or API assumptions from the
other.

## What's confirmed vs still open

See `TARGET.md`'s VERIFIED / LIKELY / UNVERIFIED triage. Short version:
jar layout, mixin config structure, Java 17 compat level, and the
no-refmap/obfuscated-names situation are all confirmed directly from an
actual install. Still open: what vanilla class each specific mixin
targets, where (if anywhere) a drop-in external mods folder exists for
this specific lane, and what's inside the platform-mappings jar.
