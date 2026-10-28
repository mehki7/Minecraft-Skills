# Minecraft Skills

Reusable Minecraft development knowledge distilled from RochStudio's Java mods, legacy ports, Bedrock adaptations and Minecraft-related mashup work. This is a private documentation repository with one installable skill. It contains original guides and prompts, not source mod binaries, assets, decompiled code or conversation exports.

Start with [SKILL.md](SKILL.md). Read a focused reference when it matches your task, or use a [prompt template](prompts/workflows.md). [The evidence index](references/evidence.md) separates project reports, inspected source, official documentation and proposed workflows; [known gaps](references/known-gaps.md) states what has not been established.

## Use without installation

Give your coding assistant the local path to `SKILL.md`, the relevant project, and your target Minecraft/loader versions. For example:

> Use the Minecraft skill in this repository to plan a ZillaCraft port from 26.3 to 1.20.1. Inspect the target branch first, preserve the moves and save IDs, and report changes in APIs, resources and testing. Do not install or publish the mod.

## Manual skill installation

Choose your assistant's documented skill directory. Create a folder named `minecraft`, then copy **`SKILL.md`, `references/` and `prompts/`** into that folder. The references must stay beside the entrypoint with the same relative paths. For Codex installations that use `~/.codex/skills`, the resulting entrypoint is `~/.codex/skills/minecraft/SKILL.md`; use the configured location if your installation differs. A repository-local `.agents/skills` location is another option where your assistant supports it.

Invoke it explicitly as `$minecraft` where supported, or refer to the file path. Check for an existing `minecraft` skill before copying and review any replacement yourself. This repository does not install itself, edit global instructions, change MCP configuration or require other skills. No code scripts are bundled because the useful source-project tools depend on their own projects and target APIs.

## Contents

- Loader/version selection and Java Edition ports versus JDK changes.
- Original behavior recovery, reference comparisons and fidelity limits.
- Maintained revival baselines, Forge/NeoForge access rules and replacement dependency delivery.
- Bedrock content, scripts, states, structures and rendering adaptations.
- Mod implementation, player lifecycle, networking and world generation.
- Models, textures, animation, giant hitboxes, sound provenance and audio review.
- Stateful item/menu ports, polygon meshes, cross-dimension travel and cold-world regressions.
- Inventory/JEI screen lifecycle, native stack metadata, utility permissions and version-specific test harnesses.
- Tests, production packaging, installation evidence and resumable checkpoints.
- Parameterized prompts and source coverage with pinned revisions/file hashes.

## Evidence and rights

Inventory inspected on **2026-10-13** and updated from the completed **“Port add-on to Forge 1.20.1”** Portal Gun session later that day. Source mod tests were not rerun during either documentation task; the update separately checked archive/artifact hashes and production ZIP/class metadata. Historical evidence includes an earlier supplied DBC 0.95/627 milestone and the newer saved 0.104/700 checkpoint; this update did not inspect or resume later DBC work. Existing archives and predecessor copies are not counted as independent successes.

A further **2026-10-13 NEI session update** adds the Forge 1.20.1/1.21.1 build, UI, command and release lessons. The source revision and private prerelease assets are pinned in the [NEI evidence record](references/evidence.md#not-enough-items). Its runtime passes occurred earlier in that session; this skill update rechecked recorded evidence and artifact identity without running the mods. Missing legacy features remain explicit.

The **2026-10-13 Mutant Creatures session update** adds a pinned revival-based Forge 1.20.1 / NeoForge 1.21.1 example, access-transformer and resource-overlay repairs, camera/onboarding and encoding regressions, dependency bundles, and an installed-loader/missing-profile diagnosis. [Its evidence record](references/evidence.md#mutant-creatures) keeps the eight server tests and nineteen connected-client assertions per target historical, and separates the later local NeoForge installation from packaged gameplay. This documentation update performs read-only identity and package checks; it does not rerun Minecraft, modify a launcher, install a skill or claim full old-version parity.

This package summarizes technical lessons in new prose. Source repositories retain their own licenses and creator notices. Private storage does not grant permission to redistribute third-party models, sounds, binaries or recovered code. No license for those materials is granted here.

For future updates, add a dated evidence pointer and its limits, then revise only the affected guide. Validate links/frontmatter and try a realistic task before publishing the update. See [package validation](VALIDATION.md) for checks performed on this revision.
