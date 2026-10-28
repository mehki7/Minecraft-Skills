# Loader and version selection

Read this before choosing a target or changing the build baseline.

## Record a compatibility tuple

Write down Minecraft edition and version, loader and exact build, mappings, Gradle wrapper, build plugin, compile JDK, runtime Java, and rendering/library dependencies. Preserve a user-selected target. Check whether essential dependencies support it before generating a project.

| Situation | Useful choice criterion |
|---|---|
| Existing Forge project | Keep Forge unless the task asks for a loader change or a required dependency forces a decision. |
| Fabric / NeoForge requested | Use that loader's version-specific project template and APIs; a Forge JAR is not a transferable implementation. |
| Legacy behavior port | Choose an attainable target that can support the required mechanics and assets. Plan compatibility adapters. |
| Several game versions | Keep explicit per-target builds/branches and a shared behavior specification. Validate each artifact independently. |
| Bedrock conversion | The source edition does not select a Java loader. Resolve the target separately. |

### Observed project tuples, not universal defaults

| Project snapshot | Game / loader | Java | Evidence |
|---|---|---|---|
| DBC saved 0.104 preview | 1.20.1 / Forge project | 17 in build configuration | [DBC](evidence.md#dbc) |
| Kaiju v2/v3/Legacy alpha | 1.20.1 / Forge 47.4.10; GeckoLib 4.8.4 in v3/Legacy notes | 17 | [Kaiju](evidence.md#kaiju) |
| Portal Gun 1.1.1-alpha.1 | 1.20.1 / Forge 47.4.26; GeckoLib 4.8.4; ForgeGradle 6.0.54; Gradle 8.8 | 17 | [Portal Gun](evidence.md#portal-gun) |
| NEI 2.0.0-port.1, older target | 1.20.1 / Forge 47.4.10; JEI 15.62.0.219; ForgeGradle 6.0.54; Gradle 8.8 | 17 | [NEI](evidence.md#not-enough-items) |
| NEI 2.0.0-port.1, newer target | 1.21.1 / Forge 52.1.0; JEI 19.64.0.453; ForgeGradle 6.0.54; Gradle 8.12.1 | 21 | [NEI](evidence.md#not-enough-items) |
| Mutant Creatures 1.4.9-port.1, older target | 1.20.1 / Forge 47.4.10; Puzzles Lib 8.1.36; ForgeGradle 6.0.54; Gradle 8.8 | 17 | [Mutant Creatures](evidence.md#mutant-creatures) |
| Mutant Creatures 1.4.9-port.1, newer target | 1.21.1 / NeoForge 21.1.259; Puzzles Lib 21.1.64; ModDevGradle 2.0.148; Gradle 8.14.3 | 21 | [Mutant Creatures](evidence.md#mutant-creatures) |
| ZillaCraft main | 26.3 / Forge 66.0.9 in project properties | 25 | [ZillaCraft](evidence.md#zillacraft) |
| ZillaCraft 1.20.1 branch | 1.20.1 / Forge 47.x; exact pin in that branch | 17 | [ZillaCraft](evidence.md#zillacraft) |
| BerthaCraft targets | 26.2 / 65.1.3; 26.3 / 66.0.9; 1.20.1 / 47.4.26 | 25 / 25 / 17 | [BerthaCraft](evidence.md#berthacraft) |

Forge's [versioned 1.20.1 getting-started guide](https://docs.minecraftforge.net/en/1.20.1/gettingstarted/) specifies JDK 17. Its [26.3 source README](https://github.com/MinecraftForge/MinecraftForge/blob/26.3/docs/README.md), checked 2026-10-13, lists Java 25 for 26.1+, Java 21 for 1.20.6–1.21.11, and Java 17 for 1.18–1.20.4. Treat these as dated guidance and recheck the exact release, particularly versions outside those ranges. Do not guess requirements for a gap such as 1.20.5 from the table alone.

For other loaders consult [Fabric's environment setup](https://docs.fabricmc.net/develop/getting-started/setting-up-a-development-environment) or [NeoForge's versioned setup guide](https://docs.neoforged.net/docs/1.21.1/gettingstarted/) using the target version selector. The latter specifies Java 21 for 1.21/1.21.1. Mutant Creatures adds bounded project-tested NeoForge evidence; no tested Fabric port is established by this inventory.

## Establish a buildable baseline

Start from the exact loader's MDK/generator or the matching existing branch. Compare wrapper and plugin versions with it; keep dependency pins reproducible instead of assuming a floating plugin range resolves forever to the historically tested version. Inspect local dependency source/JAR signatures when docs do not cover the API.

If the user requests Forge's recommended build, resolve that channel for each requested Minecraft version. NEI used 47.4.10 and 52.1.0 as checked on 2026-10-13; these are dated pins, not permanent recommendations. Read the whole target MDK: the 52.1.0 template merged class/resource output and used official runtime names with reobfuscation disabled. Removing those details allowed compilation but broke mod discovery. The 47.4.10 target still used `reobfJar`. Neither a newer game version nor Java 21 implies ForgeGradle 7.

For implementation or build diagnosis, run `java -version`, `javac -version`, the project's wrapper `--version`, and the relevant compile task. During document-only planning, identify declared versions and propose these checks without claiming they ran. Gradle's daemon JVM and Java toolchain can differ. Verify the launch JVM too. A cached Java 8 helper in a newer ForgeGradle workspace is not evidence that the mod itself targets Java 8. See [JDK diagnosis](java-porting.md).

Use target-specific artifact names and accurate dependency metadata. ZillaCraft's game-version suffix and BerthaCraft's branch-specific artifact names reduce accidental cross-version installation. Do not infer that a declared version range has been tested at every endpoint.

## Preserve access and resource rules when changing build plugins

Combining a multiloader project's common and platform sources into a standalone build can expose access rules previously supplied by its toolchain. In the **1.21.1 / NeoForge 21.1.259 / ModDevGradle 2.0.148** Mutant port, the explicit access-transformer configuration restored access to explosion fields and inherited data-generator members. Widening methods alone still left `BlockModelGenerators$BlockEntityModelGenerator` inaccessible; the nested class also needed the appropriate visibility. Inspect the exact dependency's access widener/transformer and target signatures before deleting apparently broken data generators. Use the selected plugin's build DSL; the [versioned AT specification](https://docs.neoforged.net/docs/1.21.1/advanced/accesstransformers/) explains targets and descriptors, not one interchangeable DSL for all plugins.

Inspect resource-template variables and resource-root precedence as well. This build initially lacked `resourcePackFormat`/`dataPackFormat` expansion keys; its own Chemical X model and full language overlay needed priority over upstream files with the same paths. Confirm the winning packaged entries rather than treating duplicate exclusion as a generally safe fix. When retaining a mutable snapshot build helper, pin the tested bytes and license: the Forge target vendored its tested MixinGradle JAR by hash. These are observed repairs for this source/dependency combination, not a universal AT list or template.
