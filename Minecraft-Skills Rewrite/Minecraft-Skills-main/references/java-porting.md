# Java Edition ports and JDK changes

## Classify the work

| Change | What it actually requires |
|---|---|
| Same Minecraft/loader, another JDK | Check wrapper/plugin support, daemon/toolchain/runtime selection and bytecode target. This alone does not change Minecraft APIs. |
| Minecraft Java version changes | Translate APIs, registries, events, resources, rendering, networking and save behavior for that exact target. JDK changes may accompany it. |
| Loader changes | Reimplement loader-specific entrypoints, registries, events, networking and client integration; reassess dependencies. |
| Bedrock to Java | Recreate source systems in Java and disclose adaptations. Use [the Bedrock guide](bedrock-to-java.md). |

## Port with a behavior contract

Identify stable IDs and save fields first. Compare source and target versions of each changed API rather than fixing compiler errors by deleting behavior. Keep a per-system map: old entrypoint/resource → new implementation → observable check → differences. Port shared behavior fixes to each maintained target deliberately; copying newer source wholesale can import unavailable APIs and resource schemas.

In inspected ZillaCraft and BerthaCraft branches, the 1.20.1 target uses ForgeGradle 6, Java 17 and older mappings/run configuration; newer targets use ForgeGradle 7, Java 25 and newer rendering/data APIs. These are [project examples](evidence.md#berthacraft), not a script for every mod. Use the target template's packaging/remapping/reobfuscation step: BerthaCraft's 1.20.1 build explicitly finalizes with `reobfJar`.

The NEI pair is a different observed tuple: both targets used ForgeGradle 6.0.54, while 1.20.1 used Java 17/reobfuscation and 1.21.1 used Java 21/official runtime names. Its shared sources kept small per-target adapters for registry-aware stacks, enchantments, JEI accessors and render poses. Read [the inventory/UI boundaries](inventory-ui-ports.md#keep-shared-behavior-behind-small-target-adapters) before copying either adapter to a new target.

Check behavior beyond compilation:

- Damage source identity, shields/armor, owner filtering, cooldown timing and RNG.
- Player powers after equipment removal, death/respawn, disconnect and dimension transfer.
- Entity target references, persistent state, registry IDs and old-save migrations.
- Spawn predicates, loaded chunks, placement, collision and world generation.
- Data directory names, item/equipment model formats, renderer state and networking signatures.

GameTest setup can also change. The inspected 1.20.1 branches create a controlled flat test world and use older registration/run paths; BerthaCraft's 26.2 harness documents data-driven test functions/instances/environments. Discover tasks with the wrapper's `tasks` command; do not assume `runGameTestServer` and ZillaCraft's `runGametestGameTestServer` are interchangeable. Never reset a user world to obtain a clean fixture.

The Mutant Forge/NeoForge pair also required target-specific harness changes for owner/tame APIs, crafting inputs, entity getters, bounds constructors and `structures` versus `structure` fixture paths. A shared behavior specification did not make copied harness source portable. Its NeoForge access-rule repairs are described in [loader/build-plugin boundaries](loader-version.md#preserve-access-and-resource-rules-when-changing-build-plugins); both targets' selected outcomes remain separate evidence.

## Diagnose Java compatibility separately

Record the failing stage: wrapper launch, dependency tool, compilation, mod loading, or game execution. Check [Gradle's compatibility matrix](https://docs.gradle.org/current/userguide/compatibility.html) for the wrapper version actually used. Java support for running Gradle and support for compiling through a toolchain are separate.

Use a task-local environment or explicit project toolchain. Do not change global `JAVA_HOME` or the launcher for unrelated projects. After changing the daemon JVM, stop the task's old daemon if needed and verify `--version` again. Changing `sourceCompatibility` alone does not guarantee older API availability or a loadable game artifact.

For a downport, remove unsupported language features and Java-library calls as well as Minecraft API uses. Inspect the resulting classfile target and load the production artifact under the intended runtime. For an upport, a newer JVM can run some older bytecode while the old loader or build plugin still fails; isolate that failure before rewriting gameplay.

No exhaustive arbitrary-version/JDK migration was executed for this package. The reusable procedure is proposed from inspected multi-target projects and official documentation, with historical test evidence described separately in [the index](evidence.md).
