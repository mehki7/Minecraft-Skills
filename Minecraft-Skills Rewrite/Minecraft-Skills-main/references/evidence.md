# Source and evidence index

Inspected **2026-10-13** through supported project/task discovery, read-only local project files and authenticated GitHub reads; updated later that day from the Portal Gun, NEI and Mutant Creatures sessions below. No source mod builds/tests were rerun during these documentation updates and no source projects were edited. Read-only source/archive/artifact identity, ZIP/class, installation-hash and NEI release checks were performed separately. [source-snapshots.json](source-snapshots.json) records selected file hashes and revision pointers; it contains metadata, not source payloads.

Evidence labels used throughout this package:

- **Reported runtime:** a saved project report or result file says a check ran; this task inspected that evidence.
- **Inspected source:** source/config/tool documentation establishes an implementation or API observation, without claiming a fresh runtime pass.
- **Official guidance:** target-specific primary documentation checked during this task.
- **Proposed workflow:** a reusable recommendation derived from these lessons, not independently demonstrated as a complete workflow.
- **Checked in this update:** explicitly named documentation/metadata/byte checks performed here; source gameplay/render/audio results remain historical unless stated otherwise.

Test totals count the named historical checks. They do not measure complete mod parity, cover every branch, or validate another version by inheritance.

## DBC

**Dragon Block C 1.20.1 port** — registered local project `dragon block c port`; local root alias `dbc` resolves to `Documents/ChatGPT/dragon block c port` on the source machine.

| Pointer | Evidence / limit |
|---|---|
| `CHECKPOINT.txt`, saved 2026-10-13 01:16:59 UTC | 0.104 preview; 700 server checks and bounded native client check reported passed. Full port unfinished. |
| `reports/installation.json` | `installed_incomplete_reconstruction`, `full_port_complete: false`, artifact SHA-256 and original-unchanged receipt. Installation was historical; this task did not install anything. |
| `reports/living-attack-provenance.json` | Controlled helper transaction comparisons, composed original account graph, native checks, preserved order/failure effects; ordinary activation and broader systems explicitly pending. |
| `reports/ui-rates-provenance.json` | Signed byte/float boundary recovery, source/client guards and configuration limits. |
| `reports/full-port-checklist.json` | Broader completion accounting; individual proven services do not complete the whole port. |
| `build.gradle` | Target Java 17 and project build configuration. |

The handoff supplied an earlier **0.95 / 627 checks** milestone. The later file snapshot and supported read of the paused `Update to 1.20.1` task establish a newer historical checkpoint, not new validation. No raw task messages are included. The task remains paused.

## ZillaCraft

**ZillaCraft**, main snapshot [`286c6d4`](https://github.com/RochStudio/ZillaCraft/tree/286c6d4465e1537f84d5405b1abde963f5028980); 1.20.1 branch snapshot [`f7a6e3d`](https://github.com/RochStudio/ZillaCraft/tree/f7a6e3daa94fa2fa3f8a69e96722bb2793f4c540).

- [README](https://github.com/RochStudio/ZillaCraft/blob/286c6d4465e1537f84d5405b1abde963f5028980/README.md), `build.gradle`, `gradle.properties`: separate 26.3/1.20.1 editions, stable combined mod IDs, target-specific artifact names and run tasks. The README describes 63 in-game tests; their current pass was not rerun here.
- [Asset tools](https://github.com/RochStudio/ZillaCraft/blob/286c6d4465e1537f84d5405b1abde963f5028980/tools/README.md): model/texture co-generation, selective regeneration, code-generated previews and synthesized sound. Documented sampled hitbox fitting/coverage, not newly measured coverage.
- [Hitbox tests](https://github.com/RochStudio/ZillaCraft/blob/286c6d4465e1537f84d5405b1abde963f5028980/src/gametest/java/mod/kingkongtest/HitboxGameTests.java) and [client coverage code](https://github.com/RochStudio/ZillaCraft/blob/286c6d4465e1537f84d5405b1abde963f5028980/src/gametest/java/mod/kingkongtest/client/HitboxCoverage.java): traceable test/measurement implementation.
- Local `ZillaCraft`, `ZillaCraft-mc1.20.1`, `ZillaCraft-mc26.3`, Desktop `godzilla`, `kong`, and `kong-zilla` are related development/predecessor copies. `kong-zilla/README.md` describes six observed duels and unchanged mod IDs, but is an older balance snapshot. The inspected 2026-10-06 `ZillaCraft-mc26.3/run-gametest/gametest-report.xml` contains 63 cases with no failure/error/skipped nodes; `kong` has an older 19-case report. Local saved XMLs are not automatically tied to the pinned release and were not rerun.

**ZillaCraft-archive**, [`7a162e9`](https://github.com/RochStudio/ZillaCraft-archive/tree/7a162e988a8da5b1b19e2d0698874481a3d9fdb6): predecessor documentation/config inspected for provenance; duplicate mechanisms are not independent evidence.

## BerthaCraft

**BerthaCraft** main [`b716a5c`](https://github.com/RochStudio/BerthaCraft/tree/b716a5ca00fc64d1018a09674abfd34bb3f7a17b), 26.3 [`5dfa8b2`](https://github.com/RochStudio/BerthaCraft/tree/5dfa8b28f872f810e9535036affa3bcd6ba7f336), 1.20.1 [`190c234`](https://github.com/RochStudio/BerthaCraft/tree/190c2341d141e35617720f72c167e4df7922e483).

- `README.md` / branch `build.gradle` / `gradle.properties`: multi-target build examples; main README's 36 mobs describes a release snapshot. Main's [wave D commit](https://github.com/RochStudio/BerthaCraft/commit/b716a5ca00fc64d1018a09674abfd34bb3f7a17b) describes 23 additional unreleased mobs; it does not certify full OreSpawn completion.
- [Rendering notes](https://github.com/RochStudio/BerthaCraft/blob/b716a5ca00fc64d1018a09674abfd34bb3f7a17b/docs/api/02-entity-rendering.md): source/bytecode-verified 26.2 render-state, visibility, glow and historical model-call-order pitfalls. Not every API statement is runtime-tested.
- [Harness notes](https://github.com/RochStudio/BerthaCraft/blob/b716a5ca00fc64d1018a09674abfd34bb3f7a17b/docs/api/06-gametest-harness.md): explicit source, bytecode, historical real-run and unverified labels; six real runs dated 2026-10-03. Data-driven tests, no-selection failure, fixture ticking, report paths and production exclusions.
- `docs/ART_DIRECTION.md` and `docs/DESIGN.md`: inspected project art/scope/organization documentation; local machine concurrency or artistic choices are not universal Minecraft requirements.
- Local `orespawn-remake`, `orespawn-remake-26.3`, `orespawn-remake-1.20.1` and `orespawn-work` are related targets/module workspaces. An inspected `orespawn-remake/run-gametest-main.log` ends in a failed run (exit 10); it lacks a proven relation to the pinned main revision. No all-green/current-validation claim is made.

**spawncraft-archive**, [`c4f7e60`](https://github.com/RochStudio/spawncraft-archive/tree/c4f7e60ae0928cc46bf281c0b5b00daeda592f74): duplicate predecessor docs/config, not independent success.

**berthacraft-dev**, [`f556ac0`](https://github.com/RochStudio/berthacraft-dev/tree/f556ac07472a6b99cd2e497baf9f197a05fffa83): README inspected only for historical state, tool portability and original-material rights. Its paused wave D TODOs predate main's integrated commit. Decompiled/original payloads, agent briefs and internal integration notes were not imported into this package.

## Kaiju

**minecraft-kaiju-java-ports**, [`76c2d5d`](https://github.com/RochStudio/minecraft-kaiju-java-ports/tree/76c2d5de7bf6deac9ab3e0a0da889ed9391efa3f). Local production copies also exist in the `Convert Bedrock Add-on to Java Mod` task workspace (`Documents/Codex/2026-10-05/th`).

| Pointer under repository | Reported evidence / limit |
|---|---|
| [v2 notes](https://github.com/RochStudio/minecraft-kaiju-java-ports/blob/76c2d5de7bf6deac9ab3e0a0da889ed9391efa3f/docs/PORT-NOTES.txt), `docs/STRUCTURE-CONVERSION.json` | Six GameTests, four creature/armor rendered checks; actual palette substitutions and scaled effective HP. Long balance/multiplayer limits. |
| [v3 notes](https://github.com/RochStudio/minecraft-kaiju-java-ports/blob/76c2d5de7bf6deac9ab3e0a0da889ed9391efa3f/docs/Kaiju-Craft-V3-PORT-NOTES.txt), [validation](https://github.com/RochStudio/minecraft-kaiju-java-ports/blob/76c2d5de7bf6deac9ab3e0a0da889ed9391efa3f/docs/Kaiju-Craft-V3-VALIDATION.txt) | Six GameTests, 11 forms rendered, recipe/weapon/state checks; explicit script/Molang/faction/cinematic differences. Alpha. |
| [Legacy notes](https://github.com/RochStudio/minecraft-kaiju-java-ports/blob/76c2d5de7bf6deac9ab3e0a0da889ed9391efa3f/docs/Legacy-Of-Titans-PORT-NOTES.txt), [validation](https://github.com/RochStudio/minecraft-kaiju-java-ports/blob/76c2d5de7bf6deac9ab3e0a0da889ed9391efa3f/docs/Legacy-Of-Titans-VALIDATION.txt) | Eight GameTests, 40 models/80 captures; ownership/rider/HP transitions; 45 missing source audio references; simplified choreography and states. Alpha. |
| [Converter archive warning](https://github.com/RochStudio/minecraft-kaiju-java-ports/blob/76c2d5de7bf6deac9ab3e0a0da889ed9391efa3f/conversion-tools/README.md) | Archived tools can overwrite later fixes and depend on old local layouts. Build finished `ports/` projects directly. |

No original add-on/binary/texture/audio payload is included here. Original creator rights remain with their owners.

**Standalone Godzilla Java port**, local `Port Godzilla to Forge 1.20.1` task root (`Documents/Codex/2026-10-06/i-x20`): `outputs/Godzilla-Verification.json` reports eight GameTests, model-node/vertex accounting and **interactive_client_playtest: false**. Structural model checks do not prove visual correctness. It is separate from the Bedrock kaiju ports.

## AstraNether

**astranether**, [`e87fa46`](https://github.com/RochStudio/astranether/tree/e87fa46a7aa0a8376b58bd4d924f787067c1adc8); matching local project at `Documents/ChatGPT/astranether`.

- [1.2.0 verification](https://github.com/RochStudio/astranether/blob/e87fa46a7aa0a8376b58bd4d924f787067c1adc8/VERIFICATION.md): 12 mod GameTests plus one built-in, production server, connected Survival damage and captures; elevated/covered/dodged beams and one-time health-fraction migration. Ground navigation and balance/multiplayer limits.
- `VERIFICATION-1.1.0.md`: failed-before/passed-after Survival aggro regression and accelerated natural-spawner test. Spawn attempts are not a real encounter-rate measurement.

## Sift

**sift-dimension**, [`5460e7a`](https://github.com/RochStudio/sift-dimension/tree/5460e7ad2ae33b9a7d8905a18d59df6bc6825d6e); local root `sift-dimension`.

[README](https://github.com/RochStudio/sift-dimension/blob/5460e7ad2ae33b9a7d8905a18d59df6bc6825d6e/README.md): reference-inspired versus invented/unidentified content, procedural assets, portal/arrival behavior, 17 unit checks, 14 dedicated-server checks and 35 fresh-Survival client checks reported. These are project reports; this package neither verifies news claims about the source inspiration nor certifies a faithful official implementation.

## OpusMutant

**opus-mutant**, [`1e4b1cd`](https://github.com/RochStudio/opus-mutant/tree/1e4b1cdd7d4ea531643622740b9dd40cf69f88d9).

[README](https://github.com/RochStudio/opus-mutant/blob/1e4b1cdd7d4ea531643622740b9dd40cf69f88d9/README.md): original procedural geometry/textures, mob moves, spawning, dev-only scripted client harness with wait/await/view/capture controls. No exhaustive passing test count was established. Distinct from local `roch-mutant-mobs` below.

## DragonMod

**DragonMod**, [`69c7e77`](https://github.com/RochStudio/DragonMod/tree/69c7e7708f92599108af4fd241b60241e0b21205), local `Documents/ChatGPT/mincraft/dragonmod`.

`README.md`, `build.gradle`, `gradle.properties`: 26.2 Forge/JDK 25 baseline, fire-dragon features and build/install path. README/changelog/scaffold alone is not runtime proof. Desktop `claudedragon` and `dragontest` are predecessor/test copies; their docs/configs do not add a validated independent release. Registered `gptdragon` had no usable project documentation found in the scoped read.

## Local mods

Root alias `local_mods`: `Documents/ChatGPT/mincraft`.

| Project and source pointer | Historical evidence / limits |
|---|---|
| `roch-mutant-mobs/TEST-REPORT.md` | 2026-09-25: 65 runtime checks with real dedicated server/client, AI/damage/persistence and framebuffer captures; unit task `NO-SOURCE`. Distinct from Opus Mutant. |
| `roch-avengers/verification/test-report.md` | 2026-09-30: pure budget tests, native self-test and connected-client powers/lifecycle report; task-owned worlds and production exclusions. |
| `roch-xmen/TEST-REPORT.md` | 180 server, 49 client, 219 package checks; 70 captures; real death/disconnect, equipment rejection and release-byte comparison. Audio muted; WAN/long play/crash restart not tested. |
| `roch-justice-league/TEST-REPORT.md` | 2026-10-08: 36 server, 10 client trials, five lifecycle checks and package inspection; development-runtime gameplay, no launcher-profile install validation. |

These are local report pointers with hashes in the [snapshot metadata](source-snapshots.json). No costumes, original assets, source classes or raw logs are republished.

## Mashup

**zillacraft-mashup**, [`82cf6c1`](https://github.com/RochStudio/zillacraft-mashup/tree/82cf6c120e2de9416fb9065bd0a8646803550149).

[README](https://github.com/RochStudio/zillacraft-mashup/blob/82cf6c120e2de9416fb9065bd0a8646803550149/README.md), [body boxes](https://github.com/RochStudio/zillacraft-mashup/blob/82cf6c120e2de9416fb9065bd0a8646803550149/crates/kaiju/src/hitboxes.rs), `crates/kaiju/src/species.rs`: kaiju mechanics/body geometry reused in a Rust/IW4L Minecraft-related game. These are cross-engine design/implementation lessons, not Forge API evidence or a Minecraft Java mod artifact. No new runtime or packaging validation of the mashup was performed here.

## Portal Gun

Exact supported task: **“Port add-on to Forge 1.20.1”**, ID **`01a136a9-e2a7-71e2-844d-e1615c33a15d`**, local host, completed/idle; created **2026-10-13 19:07:45 UTC**, latest completed turn **20:08:27 UTC**. All three available turns were read through the supported task control: the supplied **Portal Gun v1.1.1.mcaddon** conversion, requested installation, then user success confirmation. This is distinct from the earlier kaiju and standalone Godzilla tasks. No raw conversation or launcher data is republished.

Root alias `portal_gun`: `Documents/ChatGPT/mincraft/portal-gun`. The directory is untracked in the source workspace, so there is no source commit claimed; 24 selected file hashes identify the inspected state. Source archive hash: `ed229ef442436cb84181627933ebda755fdf073883ed6849f9398bef29a0ddba`. Credits identify **JhonFX**. The package remains a **1.1.1-alpha.1** adaptation.

| Source pointer | Evidence / scope |
|---|---|
| `reports/VALIDATION.md`, `gametest-final.log` | Nine required server tests reported passed; final cold-world travel/return, brewing and source-loot checks. No tests rerun here. |
| `reports/gametest-initial-failures.log` and supported task diffs | Mock-player null-channel failure and incorrect brewing substitution, followed by fixture/identifier fixes. Later supported diffs distinguish fresh-world return timing from earlier warm-world passes. |
| `reports/client-initial-geometry-failure.log`, `client-constructor-failure.log`; `client-console.log` | Initial polygon deserializer and `null` model-path failures; later save/fire/travel packet pass/completion markers and reported visual corrections. |
| `reports/COVERAGE.md`; `tools/convert_assets.py` | 36 items, 11 blocks, 13 crafting plus eight brewing recipes, source identifiers/aliases, dormant helpers, compatible curves and explicit shader/camera/material/vehicle adaptations. Inventory counts do not establish behavior parity. |
| `src/main/java/dev/portalguns/client/ItemRenderers.java`, `MeshRenderer.java`, `GunScreen.java` | Source-inspected lazy name lookup, indexed mesh on animated bones, GUI icon transforms and drawing/input scaling. Version/pack-specific, not arbitrary mesh or UI proof. |
| `src/main/java/dev/portalguns/PortalManager.java`, `GameEvents.java`, `Network.java` | Source-inspected arrival info, replacement-entity guard data, temporary chunk activation, ordinary exit cleanup, event phase and held-tool/UUID validation. |
| `src/validation/java/dev/portalguns/validation/PortalGameTests.java` | Traceable fixtures for mode invariants, identity/charge, actual projectile impact, fatal poison, guard cleanup and cold return. Fake-player checks and real client packets are separate evidence. |
| `reports/resource-validation.json` | 17 source OGG events decoded; audio not listener-reviewed. GUI operations/settings, fluid travel and all poses/orientations remain incompletely tested. |
| `build.gradle`, `tools/package_release.py`, `dist/manifest.json` | Exact 1.20.1 / Forge 47.4.26 / Java 17 / GeckoLib 4.8.4 / ForgeGradle 6.0.54 / Gradle 8.8 tuple, clean reobfuscated production JAR, QA exclusions and dependency delivery. |
| `reports/installation.json`, later supported user outcome | Both JAR copies verified; tooling launch false; user subsequently confirmed it worked. Build-time “not installed” docs predate this receipt. This is not exhaustive installed-artifact QA. |

**Checked here, without executing mods:** source archive hash and both release artifact hashes match the manifest; production ZIP integrity, 32 classes at class target 61, 13 crafting resources, declared mod/dependency metadata and absent QA payloads. Mod artifact SHA-256: `9d90dbb252c5b1a57c0d0b252e75f5251d590fcb1255987a058dc8f063541315`; GeckoLib artifact hash is recorded in snapshot metadata. No code, models, sounds, binaries, screenshots or source archive were copied into this knowledge repo.

Three saved final captures were also visually inspected here: `reports/screenshots/portal_gun_menu.png` shows the full menu within its frame; `portal_equipment_and_beakers.png` shows head-mounted hair, coats and floor portals; `portal_held_standard_portal_gun.png` shows a held gun, charge HUD and three portal colors. This is review of historical frames, not a new client run or proof of every GUI scale, input target, animation or material.

**Limits:** development-runtime QA rather than a launcher production-JAR test; local integrated client rather than WAN/dedicated multiplayer; NBT serialization rather than crash/restart; mounted/occupied-vehicle travel and source camera/player choreography excluded. User confirmation has unspecified depth. The synthesized generic regression workflow in [interactive item ports](interactive-item-ports.md) does not promote untested paths to passed.

## Not Enough Items

The 2026-10-13 NEI session adapted the supplied **NotEnoughItems 1.7.10-1.0.5.120** JAR to **1.20.1 / Forge 47.4.10 / Java 17** and **1.21.1 / Forge 52.1.0 / Java 21**, followed by separately requested private repository and release creation. Source: [not-enough-items-modern-forge](https://github.com/RochStudio/not-enough-items-modern-forge/tree/dbf4c5e18604b53b2fecb728edea6f518b4886aa), revision **`dbf4c5e18604b53b2fecb728edea6f518b4886aa`**; [private prerelease `v2.0.0-port.1`](https://github.com/RochStudio/not-enough-items-modern-forge/releases/tag/v2.0.0-port.1). This skill update did not build, run, install or change that source project.

Original binary SHA-256: `3ebbc2f82b61812aa158375005a47da4d450bec870860fcbf015a64de74cde1c`. Its metadata identified ChickenBones and CodeChickenCore. The inspected upstream `1.7` branch at [`285e7c5`](https://github.com/Chicken-Bones/NotEnoughItems/tree/285e7c528a7a5695a2fc0a234da15bf68561ad20) dates to 2015-11-18; it was a behavior reference, not an established exact source revision for the supplied binary. The original was preserved during the port session; no original payload is republished here.

| Pinned project pointer | Evidence / limit |
|---|---|
| `README.md`, `COVERAGE.md`, `dist/RELEASE.json` | JEI-backed adaptation, exact dependency tuples and explicit incomplete parity; old API, Creative+, spawner editor and other features omitted |
| `1.20.1/build.gradle`, `1.21.1/build.gradle`, wrapper properties | ForgeGradle 6.0.54 on both; Gradle 8.8 / 8.12.1; older-target reobfuscation versus official runtime names and merged output on 52.1.0 |
| Per-target `src/main/java/dev/nei/Platform.java` | Native stack serialization, potion effects, static/dynamic enchantment registry adapters; not old-save migration proof |
| Per-target `client/JeiProperties.java`; shared `client/JeiBridge.java`, `ToolsScreen.java` | Immutable GUI dimensions after initialization, target-specific JEI accessors, exclusion areas and quoted effect-list command |
| Shared `ServerTools.java`, `validation/Checks.java` | Server permission gates, real command-tree parsing, bounds, inventory counts/data, save/load/undo, enchantments and potions |
| Per-target `validation/NEITests.java`, `TestPlatform.java` | Exact annotation/batch selection and FakePlayer versus embedded native mock connection; fixtures alone do not prove ordinary ticks |
| Shared `validation/ClientChecks.java`; both `verification/<version>/client-result.json` files | Fourteen checks per target recorded earlier in this session: normal mouse handler, visible JEI panel, actual utility state over a connection, item search/recipe screen and normal-tick magnet collection |
| Both `verification/<version>/gametest.txt` files; `VALIDATION.md` | Four required server tests per target recorded passed; development-runtime evidence, not launcher installation |
| `package_release.py`, release asset metadata | Compared clean production compilation with tested class hashes, excluded QA payloads, dependency identity and release digests; artifact checks do not establish missing feature parity |

**Read-only checks in this documentation update:** the local source tree matched the pinned commit without changes; both production JAR/bundle hashes matched the manifest, archive integrity passed, each production JAR contained thirteen classes at classfile major 61 or 65 with no validation/fixture payload, and the recorded result files contained the named server/client passes. The release remained a published prerelease in a private repository; its tag resolved to the source commit and all seven completed asset uploads matched their remote SHA-256 digests and sizes. Twenty-seven exact Git-blob payload hashes were appended to the existing sixty-eight source snapshots. No mod tests were rerun and no screenshots, source classes, logs, archives or binaries were copied into this knowledge package.

**Limits:** no original-JAR executable oracle; full legacy parity false; no launcher production-JAR run, WAN/arbitrary modpack test, comprehensive recipe transfer/category/GUI-scale test, old add-on compatibility or death/relog/cross-version snapshot migration proof. The UI and utility successes belong to the modern implementation. A private prerelease is distribution evidence, not proof that the requested original feature set is complete. [Focused lessons](inventory-ui-ports.md).

## Mutant Creatures

The 2026-10-13 session adapted the supplied **Mutant Creatures 1.7.10–1.4.9** JAR to **1.20.1 / Forge 47.4.10 / Java 17** and **1.21.1 / NeoForge 21.1.259 / Java 21**, then prepared a local NeoForge launcher profile and separately created a private source repository. Source: [mutant-creatures-legacy-port](https://github.com/RochStudio/mutant-creatures-legacy-port/tree/da3c174942ff31922d976de18f5428eda4561612), revision **`da3c174942ff31922d976de18f5428eda4561612`**. This is distinct from the independently designed `roch-mutant-mobs` project and Opus Mutant. No GitHub release/tag or new source-project change was made during this skill update.

Original binary SHA-256: `8ec0fc2b41a02ca05e65b3200dfe08379299d4460fbc6cd34f3de95b6afd0b6d`. Metadata identified **thehippomaster21** and **AnimationAPI**. The port openly used Mutant Monsters as the engine: upstream [1.20.1 revision `9e12427`](https://github.com/Fuzss/mutant-monsters/tree/9e12427a6b0a12b3e11275ddd7b376db82234c7f) and [1.21.1 revision `15e00d5`](https://github.com/Fuzss/mutant-monsters/tree/15e00d5b8cacfffeafc484a28743897ba03cec13). These are maintained revival baselines, not the exact source revision of the original binary. Original and revival credits and their separate rights are retained in the source project; no code, models, images, audio, binaries, raw logs, launcher configuration or recovered payloads are copied into this skill package.

| Pointer at the pinned project revision | Evidence / limit |
| --- | --- |
| `README.md`, `COVERAGE.md`, `THIRD-PARTY.md` | Revival-based adaptation; seven primary creatures/equipment; newly restored bottle/recipe/probability versus inherited modern behavior and no old-save migration |
| Both target `build.gradle`, wrapper properties; `1.21.1/src/main/resources/META-INF/accesstransformer.cfg` | ForgeGradle 6.0.54 / Gradle 8.8 versus ModDevGradle 2.0.148 / Gradle 8.14.3; explicit inherited field/method/nested-class access rules |
| `1.20.1/build-support/mixingradle-identity.json`; target ignore files | Exact vendored snapshot identity/license and narrowly included build/dependency JARs |
| Per-target `Common/src/main/java/fuzs/mutantmonsters/world/item/LegacyChemicalXItem.java`, `world/entity/LegacyChemicalXProjectile.java`, `world/entity/SkullSpirit.java` | Stackable epic bottle, one selected mob per impact, original crafting path and restored 50% probability; modern conversion/eligibility/failure effects retained |
| Per-target `src/verification/java/dev/mutantport/verification/PortTests.java`; `verification/<game>/gametest.log` | Eight selected required tests per target recorded passed: native damage, revival, ownership, collision, immunity, consumption, crafting and mutation cleanup; fixture branch counts are not statistical/original-oracle parity |
| Per-target `ClientChecks.java`; `verification/<game>/client-result.json`, `client.log` | Nineteen assertions per target recorded passed; actual integrated client input, authoritative bottle use and ordinary AI damage; onboarding/camera harness repairs and explicit capture limitations |
| `VALIDATION.md`; `verification/<game>/artifact-audit.json`, `tested-production-classes.json`; `tools/package_and_audit.py` | 167 / 177 matched production classes, majors 61 / 65, JSON/PNG inspection and forty OGG decodes per target recorded; Spanish encoding fix and default sound namespace handling; audio muted |
| `tools/assemble_delivery.py`, `dist/manifest.json`, `dist/SHA256SUMS.txt` | Canonical artifact set, matching library bundles and byte identities; extracted directories excluded from delivery accounting |
| `INSTALLATION.md` | Later installed-loader/missing-profile repair, separate Java 21 instance and exact copied JAR identities; ordinary launcher game not started by tooling |

**Checked in this documentation update:** authenticated source commit and private visibility; both mod/library JAR hashes against the pinned manifest; production ZIP integrity, 167 / 177 classes at majors 61 / 65 and absence of harness payloads; recorded eight-test server and nineteen-check client outcomes; both installed NeoForge JAR hashes against the local installation receipt. The receipt itself contains machine paths and remains outside this repository. Selected exact Git-blob hashes are appended to the previous 95 source pointers, which are preserved unchanged. No Minecraft build, runtime, audio decode or launcher mutation was repeated here.

Mod JAR hashes: Forge `b07ccc36085d16bb4bd12c1aad76d4aee9fcbab233c3c927f074acf66a6e857f`; NeoForge `5a72c67c845ac9527f592feb22e9b0443589baf3cb8dbba388dc344930ff81cc`. Puzzles Lib 8.1.36 / 21.1.64 hashes and the refreshed documentation bundle identities are recorded in the pinned manifest/checksum files and snapshot metadata.

**Limits:** no complete 1.4.9 parity or executable original oracle, no 1.7.10 world migration, no restored legacy natural spider-pig spawning, and no exhaustive special-attack/equipment/pet/riding/spawn-frequency tests. The historical client uses an integrated server; dedicated-server multiplayer, WAN/modpacks and long-term balance remain unverified. The later local installation has exact byte evidence but no tool-launched packaged-gameplay run or user play confirmation. Production class equality and a private source upload do not strengthen those claims.

## Official guidance and discovery limits

[Forge 1.20.1 setup](https://docs.minecraftforge.net/en/1.20.1/gettingstarted/), [Forge 26.3 Java requirements](https://github.com/MinecraftForge/MinecraftForge/blob/26.3/docs/README.md), [Gradle Java compatibility](https://docs.gradle.org/current/userguide/compatibility.html), [Fabric setup](https://docs.fabricmc.net/develop/getting-started/setting-up-a-development-environment) and [NeoForge setup](https://docs.neoforged.net/docs/gettingstarted/) were read on 2026-10-13. Version-specific facts must be checked again for new targets.

The Mutant update rechecked the [1.21.1 NeoForge setup](https://docs.neoforged.net/docs/1.21.1/gettingstarted/), [access-transformer specification](https://docs.neoforged.net/docs/1.21.1/advanced/accesstransformers/) and [sound-definition guide](https://docs.neoforged.net/docs/1.21.1/resources/client/sounds/). Tested build-plugin DSL and repairs are grounded in the pinned project files; documentation routes alone do not establish another loader/plugin's compatibility.

Local skill-creator and existing Bedrock guidance were consulted for packaging/workflow, with project reports used to ground technical claims. No private assistant instructions were copied. Relevant `.agents/skills` locations and repository file inventories yielded no additional Minecraft skill package. Supported Personal Context was unavailable. Backups, source-cache folders and the channel website do not add independent mod-test evidence. See [known gaps](known-gaps.md).
