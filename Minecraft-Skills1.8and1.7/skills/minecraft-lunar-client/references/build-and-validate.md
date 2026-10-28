# Building and validating a Lunar 1.8.9 mixin mod

## Build setup

Target a Java 17 toolchain (not Java 8 — this lane runs `compatibilityLevel: JAVA_17`,
confirmed in TARGET.md). Your `build.gradle` should use standard Gradle + Java 17 plugin
conventions, not ForgeGradle 2.1 (that is for plain Forge 1.8.9 — separate toolchain).

Compile against `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` as a file dependency,
not a Maven artifact — Lunar does not publish to any public Maven repository.
Pin the exact jar hash in TARGET.md before building (see canary-pinning.md).

Key compile flags:
```
-Dmixin.env.disableRefMap=true
```
Include an empty `"refmap": ""` in your mixin config. Mixin will skip the remap
step entirely, which is what you want since you are hardcoding obfuscated names.

## Mixin config minimum

```json
{
  "minVersion": "0.8",
  "package": "your.mod.mixin",
  "target": "CLIENT",
  "required": true,
  "compatibilityLevel": "JAVA_17",
  "refmap": "",
  "mixins": []
}
```

Match the structure of Lunar's own configs exactly (no extra keys you have not
verified are actually consumed by Lunar's loader).

## Definition of done — do not call it done until all of these pass

| Check | Evidence needed |
|---|---|
| Build passes | `./gradlew build` exits 0 with no errors |
| Mixin config loads | In-game log shows your config being processed (not silently skipped) |
| Mixin attaches | `-Dmixin.debug=true -Dmixin.checks=true -Dmixin.verbose=true` log confirms the method was found and patched |
| Feature works | Actual in-game observable behavior matches the intended outcome |
| No client crash | Full launch cycle without crash, not just "compiled fine" |

A successful compile **does not prove any of the last four checks.** A compile
only proves the Java source is syntactically valid against your hardcoded names —
it says nothing about whether Mixin actually attached anything at runtime.
Always do the in-game check with debug flags before marking a feature done.

## Coverage map — fill this out before shipping

| Feature | Mixin class | Target (obf name) | Status | Evidence |
|---|---|---|---|---|
| (your feature) | YourMixinClass | IOOCCRIRH... (from RECON) | implemented | log line from mixin.debug run |

## Packaging

Your mod ships as a jar with its own mixin config. The question of *where* that jar
goes so Lunar actually loads it remains UNVERIFIED — see external-mods.md and
TARGET.md's UNVERIFIED section. Resolve the loading mechanism before assuming a
drop-in path works. Record the exact jar hash and the pinned Lunar build hash
together in your release notes.
