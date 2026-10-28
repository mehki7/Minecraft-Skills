# Pinning to a specific build

Lunar's offline/canary jars are not a stable, versioned release in the
way a Maven artifact is — the obfuscated names, the mixin configs, even
which classes exist can drift the next time Lunar updates its offline
bundle. Treat whatever `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` you
built against as an ABI snapshot, not "1.8.9 support" in the abstract.

## Practical pinning steps

1. Record the jar's exact file hash (`certutil -hashfile
   legacy-0.1.0-SNAPSHOT-all-nomappings.jar SHA256` on Windows) alongside
   the date you pulled it, in TARGET.md.
2. Keep a copy of the exact jar you built against somewhere safe, outside
   the live Lunar install folder — Lunar will silently replace it on its
   next auto-update.
3. Because refmaps are disabled and names are hardcoded (see
   SKILL.md port doctrine), any Lunar update that changes its ProGuard
   obfuscation mapping will break your mod's mixin targets outright, not
   gracefully. There's no fallback — the mixin just won't apply, and
   depending on `"required": true` in your config, that can hard-crash
   the client instead of silently no-op'ing.
4. Before relying on a build again after any Lunar update, re-run the
   RECON script against the new jar and diff the output against the
   last-known-good name map before assuming nothing changed.
