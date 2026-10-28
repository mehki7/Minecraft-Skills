# Testing, releases and checkpoints

## Match claims to evidence

| Evidence layer | What it supports | What it leaves open |
|---|---|---|
| Unit/pure logic | deterministic math, cooldowns, geometry rules | game hooks and synchronization |
| Original-reference comparison | specified behavior on the compared vectors | uncontrolled helpers and full lifecycle |
| Server GameTest/runtime fixture | native state, damage, entities, persistence in a scenario | rendered appearance and human balance |
| Connected client | packets, actual input paths, client/server effects | WAN, scale and all user interactions |
| Visual capture | inspected pose/material/frame | unobserved transitions and all camera conditions |
| Audio decode/event check | usable resource and trigger | listener judgment |
| Packaged-JAR run/hash comparison | relation between tested and delivered bytes | combinations never exercised |

Record date, exact versions, source revision/hash, selected tests, required failures and artifact identity. Keep passed, failed, skipped and unverified separate. `NO-SOURCE`, zero selected tests or successful startup is not a gameplay pass. Do not hide a failing requirement by marking its test optional.

## Build fixtures that exercise production behavior

Use isolated disposable worlds and separate run directories. Check actual health loss, item use/consumption, saved state, cleanup, collision and line-of-sight; do not merely call a helper and check its own return value. Allow network synchronization and normal cooldown timing where the scenario requires them.

BerthaCraft's **26.2 / Forge 65.1.3 / ForgeGradle 7.0.40** harness notes distinguish source/bytecode checks from six historical real runs. They record data-driven tests, required-failure exit codes, no-selection failure, report-directory requirements and mock-player equipment/tick pitfalls. These details must be rechecked for another target. A mock player may not receive normal world ticks; do not use a fixture shortcut as evidence for connected-player lifecycle.

Astra's before/after Survival regression and superhero reports' real death/disconnect trials are stronger than startup alone. Keep before-fix failure evidence for a reproduced bug. An accelerated spawn fixture verifies a path, not normal encounter frequency. [Sources](evidence.md).

Portal Gun's earlier nine-test success was followed by a failure in a fresh world's Nether return path. Its final fixture allowed cold chunk activation and waited for the returned UUID-bearing entity, while production used transient chunk tickets and ordinary level-tick guard cleanup. Do not reuse a warm world as the only travel evidence, or merely extend a timeout without observing transfer/guard state. Its initial mock-player fixture failed on a null network channel; nonnetwork FakePlayer fixtures fixed those checks, with connected-client packets verified separately. [Detailed regression record](interactive-item-ports.md#failed-approaches-and-evidenced-fixes).

NEI's 1.21.1 fixture selected no tests when its namespace filter was paired with the default batch after prefix suppression. An explicit intended batch fixed selection. Its helper/annotation APIs and `data/<namespace>/structure` fixture path also differed from 1.20.1's `structures` path. Check both actual selection and completion results; a failed startup or assertion can coexist with a successful wrapper exit in these harnesses. Its final reports separately record four required server tests and fourteen connected-client checks **per target**, not one total inherited by both. [Inventory/UI regression details](inventory-ui-ports.md#failures-and-bounded-fixes).

Mutant's **eight required server tests and nineteen connected integrated-client assertions per target** separate health/damage, revival, ownership round trips, native crafting, real bottle impact, consumption and spirit cleanup from normal client input and AI damage. The sixteen mutation fixtures producing both successful and failed conversions establish those lifecycle branches; their counts do not prove a 50% distribution or original RNG parity. The integrated client is a real connection, but does not establish dedicated-server multiplayer or WAN behavior. [Evidence](evidence.md#mutant-creatures).

## Relate the release to the tested code

After the final QA change, rebuild the production artifact with the target's remapping/reobfuscation step. Inspect JAR metadata, class target, required dependencies, registry/resource references and excluded harness classes/data. Load that JAR when practical. If tests used a development runtime, say so; compare production classes/resources with the tested copy where appropriate.

The X-Men report compared every shipped JAR entry with its tested instrumented copy, whereas Justice League disclosed that gameplay used final development sources and did not test installation in a launcher profile. Preserve that distinction. No single packaging technique is required for every low-impact edit.

For multi-target artifacts, exclude every target's validation classes and fixture paths. NEI captured production-class hashes from tested development output, then compared clean ordinary builds before packaging. Its 1.21.1 official-name JAR classes could be compared directly; its 1.20.1 JAR was reobfuscated afterward, so equality of pre-reobfuscation compilation output is the narrower claim. Both artifacts had thirteen classes; their classfile majors were 61 and 65 respectively. Neither comparison proves launcher installation.

Mutant applies the same distinction across loaders: 167 Forge production classes matched the tested compilation before reobfuscation, while 177 NeoForge packaged classes could also be compared directly. Its dependency bundles and JSON/image/audio checks are separate evidence layers. Generate checksums from a canonical artifact list; a user's extracted bundle directory inside `dist` should not become another release payload or duplicate checksum entry.

For requested installation, resolve the active launch profile's actual game directory, back up the replaced version outside `mods`, avoid duplicate mod IDs, copy exact artifacts/dependencies and verify hashes. A correct JAR in an unused instance is not a completed installation. Keep launcher/world changes within the request.

Use chronological evidence after installation. Portal Gun's build-time README/report says it was not installed; the later installation receipt verifies both JAR hashes and records that tooling did not launch the game, followed by the user's success confirmation. These do not become an exhaustive production playtest. The profile reader also hit case-distinct `Forge`/`forge` keys; PowerShell's `ConvertFrom-Json -AsHashtable` handled that file without rewriting launcher configuration.

For requested launcher troubleshooting, distinguish delivered mod files, an installed loader version, a launcher profile and that profile's actual game directory. Opening a bundle folder does not create a game installation. In Mutant's later setup, NeoForge 21.1.259 and its required libraries were already present, but no profile referenced it. The repair added a named Java 21 profile with a separate game directory, copied the mod and matching Puzzles Lib, preserved existing profiles and refreshed the launcher after backing up its configuration. Check the existing version ID/inheritance and profile list before reinstalling a loader. Preserve case-distinct keys, and verify saved state after a launcher refresh so a live cached configuration does not undo the change. Its later installation receipt records exact copied hashes and **game not launched**; do not promote that repair into packaged-gameplay evidence.

For requested publication, inspect the selected tree for credentials, machine data, copied source payloads and unrelated files. State visibility and owner explicitly, then verify the pushed commit and remote state. A private repo does not broaden third-party redistribution rights.

Review inherited ignore rules when preparing a standalone source repository. Mutant's upstream `*.jar`/`*.txt` patterns would have excluded required local dependency JARs, the pinned build helper and its license without narrow exceptions. Include actual build inputs while excluding worlds, caches, decompiled reference payloads and launcher/account backups. Keep path-redacted test evidence distinguishable from fresh tests and retain exact binary hashes. The source repo contained both targets and finished bundles; repository creation did not create a GitHub release.

For a requested GitHub release, anchor the tag to the reviewed commit, describe dependency/feature limits, and verify that uploaded assets have completed upload with the expected sizes and SHA-256 digests where supplied by the host. NEI's private `v2.0.0-port.1` prerelease attached two bundles, two mod-only JARs, source, manifest and checksums; the tag commit and all seven remote digests were checked. Preserve the repository's requested visibility. Do not infer release, installation or public publication authorization from a request to build or to maintain this skill.

Use byte equality for JAR/ZIP delivery identity. Git's text normalization can make a working JSON file differ from its committed bytes without a semantic change: NEI compared parsed manifests, then uploaded the committed manifest bytes and calculated its checksum from that exact asset. Do not weaken binary hash checks or silently replace previously reviewed release files to accommodate text line endings.

## A useful checkpoint

Save a concise record with:

- version/revision and artifact hash; build/runtime tuple;
- implemented/adapted/pending systems and the last verified behavior;
- exact evidence files, failure/skipped checks and test limitations;
- installed artifact versus built-only artifact, if relevant;
- the next concrete task and prerequisites, with a reproducible command or source pointer.

Keep a full-port completion flag independent from test totals. DBC's checkpoint has many proven slices and a passing bounded client check while ordinary activation and wider lifecycle work remain unfinished. When asked to pause, save the point and stop; creating or maintaining this knowledge skill does not resume that task.
