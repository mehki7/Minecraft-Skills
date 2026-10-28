# Testing and releasing a 1.8.9 / 1.7.10 legacy mod

Scoped to plain Forge 1.8.9 and 1.7.10. For Lunar-specific build/validation steps,
see `minecraft-lunar-client/references/build-and-validate.md`.

## Match claims to evidence

| Evidence layer | What it supports | What it leaves open |
|---|---|---|
| Compile passes | Java source valid against pinned API | Everything about runtime behavior |
| Manual in-game test | Observable gameplay on your machine | Multiplayer, other configs |
| Server test | Damage, state, entities, persistence | Rendered appearance |
| Visual check | Pose/material/frame at one moment | All other animation states |

Record: date, exact Forge version and build hash, MCP mapping set, selected tests,
pass/fail/skipped, and artifact identity. Keep passed, failed, skipped, and unverified
separate. A successful startup is not a gameplay pass.

## Build checklist

For 1.8.9 plain Forge (`1.8.9-11.15.1.2318`):
- [ ] ForgeGradle 2.1-era `build.gradle` syntax confirmed (not FG6 syntax)
- [ ] Java 8 compile target confirmed (`sourceCompatibility = '1.8'`)
- [ ] MCP stable_22 mappings declared
- [ ] `./gradlew build` exits 0
- [ ] `reobfJar` task ran and produced the obfuscated output JAR
- [ ] Production JAR inspected: correct manifest, no test fixtures bundled
- [ ] JAR loaded in actual Minecraft 1.8.9 + Forge instance
- [ ] Feature exercised in-game and behavior matches coverage map

For 1.7.10 plain Forge (`10.13.x`):
- [ ] ForgeGradle 1.2-era `build.gradle` syntax confirmed
- [ ] Java 7/8 compile target confirmed
- [ ] MCP stable_12 mappings declared
- [ ] Same in-game checklist as above, on actual 1.7.10 + Forge instance

## Production artifact

After the final QA change, rebuild with the correct era's remapping step.
Inspect JAR metadata, class target, required dependencies, and absence of test classes.
Do not install or publish unless explicitly requested separately from the build task.

## Checkpoint format (for pausing work)

Record concisely:
- Forge version/build hash; Java/toolchain tuple
- Implemented, adapted, pending systems; last verified behavior
- Exact evidence: tests run, failures, skipped items
- Next concrete task and prerequisites
