# Toolchain and Gradle for Forge 1.7.10

## Version pins

- Forge: `10.13.4.1614-1.7.10` (widely-used recommended build; verify against your
  target if a specific build was requested)
- ForgeGradle: 1.2 era
- MCP mappings: stable_12
- Java: 7 (minimum), 8 (recommended for modern dev; both are valid targets)

## build.gradle structure (1.7.10 era)

The ForgeGradle 1.2 DSL is substantially different from FG2+ and FG6. The key
structure looks like:

```groovy
buildscript {
    repositories {
        mavenCentral()
        maven { url "http://files.minecraftforge.net/maven" }
        maven { url "https://oss.sonatype.org/content/repositories/snapshots/" }
    }
    dependencies {
        classpath 'net.minecraftforge.gradle:ForgeGradle:1.2-SNAPSHOT'
    }
}

apply plugin: 'forge'

minecraft {
    version = "1.7.10-10.13.4.1614-1.7.10"
    runDir = "run"
    mappings = "stable_12"
}
```

Do not use `plugins { id 'net.minecraftforge.gradle' ... }` (the modern plugin block)
in a 1.7.10 project. That is FG3+ syntax and will not resolve correctly.

## Java version handling

For Java 8 dev environment with Java 7 target compatibility:
```groovy
sourceCompatibility = JavaVersion.VERSION_1_7
targetCompatibility = JavaVersion.VERSION_1_7
```

Or keep Java 8 throughout if you do not need strict Java 7 compat — most 1.7.10
mods were built on Java 8 even though the game nominally supported Java 7.

## Output artifact

ForgeGradle 1.2 era produces a reobfuscated JAR via `gradle build`. The reobf task
is wired in automatically by the ForgeGradle `forge` plugin. The output goes to
`build/libs/`. Inspect the JAR to confirm it contains obfuscated (not MCP) names
before distributing.

## Common issues

- Gradle wrapper version: ForgeGradle 1.2 works with older Gradle (2.x-3.x range).
  Modern Gradle 7+ may have compatibility issues with FG1.2. Use the wrapper pinned
  in your project's `gradle/wrapper/gradle-wrapper.properties`.
- Maven repository URLs for ForgeGradle 1.2 may use `http://` (not https). If your
  build environment blocks non-TLS URLs, you may need to find a mirror or proxy.
  This is a known friction point with 1.7.10 era tooling in modern dev environments.
