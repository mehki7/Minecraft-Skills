# Parameterized Minecraft prompts

These are reusable requests. Replace the named fields in braces with your actual values; they are intentional input parameters. Supply only the relevant files. Each prompt supports implementation and evidence reporting without authorizing unrelated installation, publication or paused-task continuation.

## Inventory and choose a target

> Use $minecraft. Inspect {project_or_archive} and propose a target for {intended_players_and_dependencies}. Inventory playable features, source version, loader, toolchain, assets/scripts and the latest checkpoint. Explain any choice that changes scope. Produce a source-to-target coverage map and distinguish source facts, historical test reports and unverified assumptions. Make no source-project changes yet.

## Create a mod

> Use $minecraft to implement {feature_scope} in {workspace} for Minecraft {game_version}, {loader} {loader_version}. Start from the matching project/template. Keep IDs stable and implement the complete playable path, including {persistence_or_multiplayer_requirements}. Verify the changed behavior with appropriate server/client checks and inspect the production artifact. Deliver source, artifact/dependencies and concrete limits. Install or publish only if explicitly requested separately.

## Port a Java Edition version

> Use $minecraft to port {source_revision} from {source_game_loader} to {target_game_loader} in {target_workspace}. Preserve {behavior_and_save_requirements}. Inventory the supplied original before choosing any maintained revival; identify that baseline, replacement dependencies, restored mechanics and inherited differences explicitly. Compare exact target APIs and resource schemas; distinguish the Minecraft API port from JDK/build changes. Track each subsystem's implementation and test evidence. Verify target packaging/remapping and ordinary gameplay/lifecycle. Report intentional differences and untested features rather than claiming parity from compilation.

## Diagnose a JDK/build change

> Use $minecraft to diagnose {failure_log} in {project}. The intended game/loader is {game_loader}; desired Java runtime is {java_version}. Identify which JVM runs Gradle, compiles the mod and launches Minecraft. Check wrapper/plugin compatibility and bytecode/library constraints. Fix the narrow cause with task-local settings, verify the intended runtime, and explain whether any game API port is actually needed.

## Port an inventory browser or utility UI

> Use $minecraft to port {legacy_mod_revision} to {target_game_loader_versions}. Map original features and explain any core behavior delegated to {proposed_dependency_or_none}, including new installation requirements and omitted add-on compatibility. Preserve the requested scope. Start from each target's exact MDK; separate common behavior from registry, serialization, GUI and render adapters. Verify initialized GUI-property snapshots, visible overlays, normal input dispatch, namespaced command arguments, server permission rejection, native inventory data and real player-tick effects. Require actual selected GameTest results per target and disclose which runtime and release bytes were tested. Deliver {requested_artifacts}; keep original parity and installation claims separate from passing modern adaptation checks.

## Recover legacy behavior

> Use $minecraft to recover {system_or_methods} from {authorized_reference_version} into {target_project}. Record source identity/hash and observable input, mutation, RNG and failure semantics. Use an independent original oracle where available and label controlled versus native helper boundaries. Test ordering/boundaries and then the ordinary game entrypoints. Preserve required quirks or document adaptations. Keep the broader full-port checklist incomplete where systems remain pending.

## Adapt Bedrock content

> Use $minecraft to adapt {mcaddon_or_mcpack} to Minecraft Java {version} on {loader_version}. Inventory packs, scripts, species/forms/helpers, controllers/Molang, items/recipes, sounds, structures and malformed/missing data. Implement {requested_scope}; maintain a coverage map with adaptations and omissions. Verify ownership, commands, riding/forms, health/damage/healing, save/load, recipes and rendering as relevant. Compare source versions before retaining removed content. Deliver a buildable/loadable port with exact dependencies, creator credits and specific alpha limits.

## Review a rendered model

> Use $minecraft to diagnose {model_or_entity} in {target_project}. Compare {reference_views_or_geometry} with front/side/rear and action poses. Inspect pivots, hierarchy, UVs, alpha/materials, scale, culling, held-item transforms and hitboxes where relevant. Use available preview tools, then the real target client. Save representative evidence and label unavailable visual checks. Do not infer in-game correctness from a loaded geometry file.

## Port a stateful tool or travel system

> Use $minecraft to port {source_tool_or_portal_system} to {target_game_loader}. Map stable item IDs, assembly/depletion/refill state, ownership, link modes, saved destinations and server-validated UI actions. Inspect cube/polygon geometry, source aliases and effect-trigger ownership. Test real projectile impacts, rejected actions without resource loss, cold-dimension outbound/return travel, replacement entity identity, exit-guard cleanup and saved-state round trips. Check menu drawing and hit-testing at several GUI scales. Separate fake-player logic checks, connected-client packets, production artifact inspection and user installation feedback; disclose {known_adaptations_and_unverified_paths}.

## Improve SFX

> Use $minecraft to improve {sound_events} for {intended_style} in {project}. Inventory audio provenance/license, missing references and target format/channel needs. Propose a small audible comparison set using {available_authorized_sources_or_synthesis}. Check decode/mapping, triggers, mix and near/far playback. Distinguish listener feedback from muted automation. Preserve chosen files/settings and report quality or library-access gaps without inventing access.

## Verify and package

> Use $minecraft to verify {feature_change_or_revision} for {exact_runtime_tuple}. Derive checks from its coverage map, exercise production behavior, record selected/passed/failed/skipped checks and inspect the production JAR. Relate tested code/resources to delivered bytes. Report historical evidence separately, including rendering/audio and multiplayer limits. Deliver {requested_artifacts}; perform only the installation/publication actions explicitly included in my request.

## Save a pause checkpoint

> Use $minecraft to save and pause {project} at its current verified point. Record version/revision, artifact/hash, exact evidence, implemented/adapted/pending systems, failures/limits and the next concrete task. Preserve existing work. A passing test total is not a full-port completion claim. Stop after the checkpoint; do not resume other paused tasks.
