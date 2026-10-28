# Toolchain and Gradle for this era

## Plain Forge 1.8.9 target

- Java 8, ForgeGradle 2.1-era conventions.
- MCP stable_22 mappings.
- `build.gradle` uses the old `buildscript { ... }` ForgeGradle plugin
  application style (not the modern plugin DSL), and version/mappings are
  declared via `minecraft { version = "1.8.9-11.15.1.2318" ... }`-style
  blocks specific to that ForgeGradle generation. Check whatever specific
  ForgeGradle 2.1 documentation/examples are available rather than
  assuming current ForgeGradle 6 syntax works — it doesn't, the DSL
  changed substantially between generations.

## Lunar-targeting build (not plain Forge)

Per confirmed evidence in `minecraft-lunar-client`'s TARGET.md, Lunar's
own 1.8 mixin lane runs `compatibilityLevel: JAVA_17`. If you're building
a mod meant to mixin-patch Lunar directly (not compile against plain
Forge), target a Java 17 toolchain for that build, even though the game
version is 1.8.9. Don't default to Java 8 here just because the game
version looks old — confirm which of the two targets (plain Forge vs
Lunar) you're actually building for first, since they need different
toolchains.

## General rule

Never write a Gradle file that just says "use Java 8" or "use modern
Forge" as a blanket default for "1.8.9 modding." The actual correct
toolchain depends on whether the real target is plain Forge (Java 8) or
Lunar's bundled lane (Java 17, confirmed). State which one explicitly.
