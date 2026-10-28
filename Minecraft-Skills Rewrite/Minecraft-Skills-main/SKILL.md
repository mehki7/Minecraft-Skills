---
name: minecraft
description: Create Minecraft Java mods, port mods between Minecraft versions or loaders, recover legacy behavior, and adapt Bedrock add-ons to Java with traceable coverage and validation. Use for mod development and porting; ordinary mod installation alone does not need this skill.
---

# Minecraft development and porting

Deliver the requested mod or port against an explicit Minecraft edition/version, loader/version and dependency set. Preserve the user's scope and existing project. A Java Edition version port, a JDK change, and a Bedrock adaptation are different jobs.

## Start with the actual project

- Inspect build files, registries, resources, source definitions and the latest relevant checkpoint. Record the baseline revision and existing changes before editing. Treat old READMEs, generator output and archive TODOs as dated evidence.
- Resolve the target from the request and existing project. If missing, propose a compatible target based on dependencies and intended players; clarify only choices that materially alter the work. Do not silently choose the newest release or force every project onto 1.20.1.
- Make a small coverage table: source feature/file, target implementation, status, behavior differences and evidence. Use `implemented`, `adapted`, `omitted`, `blocked` or `unverified` precisely. Record references with revision/date and file or method pointers.
- Read only the guides relevant to the task below. Historical project reports are examples of evidence, not tests performed on the current work.
- For planning or document-only review, inspect the supplied reports/configuration, record unavailable source/artifact baselines, and label future checks as proposed. Run implementation/build commands only when they belong to the requested work.

## Choose the relevant guide

| Need | Read |
|---|---|
| Choose loader, game version, mappings and toolchain | [Loader and version selection](references/loader-version.md) |
| Port Java Edition versions or diagnose a JDK/build change | [Java version ports and JDK compatibility](references/java-porting.md) |
| Recover an older mod, assess a maintained revival baseline or compare an oracle | [Original behavior and reference comparisons](references/behavior-recovery.md) |
| Convert an `.mcaddon` / `.mcpack` | [Bedrock to Java mapping](references/bedrock-to-java.md) |
| Implement mobs, items, player powers, networking or worldgen | [Mod implementation](references/mod-implementation.md) |
| Port stateful tools, menus, projectiles or cross-dimension travel | [Interactive item ports](references/interactive-item-ports.md) |
| Port inventory browsers, JEI screens or administrative utilities | [Inventory and UI ports](references/inventory-ui-ports.md) |
| Work on models, textures, animation, hitboxes or sounds | [Rendering, assets and SFX](references/rendering-assets-sfx.md) |
| Verify, package, release or pause work | [Testing, releases and checkpoints](references/testing-release.md) |
| Adapt a starting request | [Parameterized prompts](prompts/workflows.md) |
| Check where a lesson came from or its limits | [Source evidence](references/evidence.md) and [known gaps](references/known-gaps.md) |

## Implement and prove the change

Use the exact target's dependency sources and official documentation for APIs and resource formats. Translate mechanics and persistent state deliberately; preserve observed ordering, RNG use and failure side effects when fidelity is requested. Make adaptations explicit rather than hiding them behind a generic mob or an alpha label.

Choose checks for the changed behavior: pure logic where useful, real server integration, connected-client behavior and visual/audio review where relevant. Check actual damage, state, ownership, persistence and cleanup rather than only registration or absence of exceptions. A successful compile, test count or screenshot count does not establish complete parity.

Produce a clean production artifact with matching metadata and dependencies. Keep test harnesses and temporary hooks out of it; relate the delivered artifact to what was tested. Report exact checks performed, historical evidence reused, omitted features and remaining limitations. For a pause, save a concrete stopping point and next step without claiming the full port is finished.

Installation, launcher edits, publication and collaborator invitations remain separate actions: perform them only when requested. Work on this knowledge package does not authorize resuming another paused mod project. Preserve original creator credits and rights; no source asset or decompiled payload redistribution is implied.
