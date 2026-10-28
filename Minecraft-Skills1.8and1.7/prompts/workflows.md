# Parameterized prompts — Multi-launcher 1.8.9 / 1.7.10

Replace fields in braces with your actual values. These prompts are scoped strictly
to 1.8.9 (primary) and 1.7.10 (secondary). Never use them to drive work on 1.12.2
or any newer version.

## Launcher/client selector

Before using any prompt below, identify the target:

| Target | Skill to specify |
|---|---|
| Lunar Client 1.8.9 (mixin lane) | `minecraft-lunar-client` |
| OneClient 1.8.9 | `minecraft-oneclient` |
| Plain Forge 1.8.9 | `minecraft-legacy-modding-189` |
| Plain Forge 1.7.10 | `minecraft-legacy-modding-1710` |

---

## Port a Forge 1.8.9 mod onto Lunar Client

> Use `minecraft-lunar-client`. Read TARGET.md first. Port {source_mod}
> from plain Forge 1.8.9 onto Lunar Client's mixin-based lane. Confirm the pinned
> Lunar build hash. Run RECON/02-mine-mixin-targets.py and identify hook points
> for {feature_list}. Produce a coverage map with VERIFIED obfuscated target names
> — mark anything unconfirmed as UNVERIFIED. Write mixin code and build config.
> Verify with `-Dmixin.debug=true -Dmixin.checks=true` before marking done.

## Port a Forge 1.8.9 mod onto OneClient

> Use `minecraft-oneclient`. Read oneclient-loader.md first and inventory
> OneClient's coremod/patch layer from a real install before writing any hooks.
> Port {source_mod} to run on OneClient. If the mod has no OneClient-specific
> hooks, test the plain Forge build on OneClient first — it may work without
> changes. If OneClient-specific hooks are needed, document the hook approach
> (Mixin vs coremod) and confirm it with in-game testing.

## Create a new mod for plain Forge 1.8.9

> Use `minecraft-legacy-modding-189`. Target: Minecraft 1.8.9 /
> Forge 1.8.9-11.15.1.2318, Java 8, ForgeGradle 2.1, MCP stable_22.
> Implement {feature_scope}. Verify with in-game testing. Deliver source, built JAR,
> and coverage map with pass/fail evidence.

## Create a new mod for plain Forge 1.7.10

> Use `minecraft-legacy-modding-1710`. Target: Minecraft 1.7.10 /
> Forge 10.13.4.1614, Java 8, ForgeGradle 1.2, MCP stable_12.
> Implement {feature_scope}. Remember: no JSON models exist in this version —
> use ISimpleBlockRenderingHandler / IItemRenderer. Verify with in-game testing.

## Port 1.7.10 → 1.8.9

> Use `minecraft-legacy-modding-189`. Read legacy-1710-diffs.md and
> version-diff-1710-189.md first. Port {source_mod_1710} from Forge 1.7.10
> to Forge 1.8.9-11.15.1.2318. Update toolchain (FG1.2 → FG2.1, MCP stable_12
> → stable_22). Explicitly scope the rendering rewrite (x/y/z → BlockPos,
> pre-JSON renderer → JSON models). Verify each system in-game.

## Port 1.8.9 → 1.7.10 (downport)

> Use `minecraft-legacy-modding-1710`. Read version-diff-1710-189.md first.
> Port {source_mod_189} from Forge 1.8.9 to Forge 1.7.10 {target_forge_build}.
> Update toolchain (FG2.1 → FG1.2, MCP stable_22 → stable_12). Explicitly scope
> the rendering rewrite (BlockPos → x/y/z, JSON models → ISimpleBlockRenderingHandler).
> This is a heavier port than going the other direction — scope it explicitly.

## Diagnose a build failure (any target in this pack)

> Use {skill_name_for_target}. The project targets {1.8.9_or_1.7.10} /
> {launcher_and_forge_build}. Failure log: {log_or_error}. Check which JVM runs
> Gradle vs compiles vs launches. Check ForgeGradle version compatibility for this
> era (FG1.2 for 1.7.10, FG2.1 for 1.8.9). Fix the narrow cause without touching
> unrelated configuration.

## Save a pause checkpoint

> Use {skill_name_for_target}. Save and pause {project}. Record: Forge version/build
> hash, Java tuple, coverage map with implemented/pending/blocked labels, exact
> evidence of last verified behavior, failures and limits, and next concrete task
> with a reproducible command or source pointer. Stop after the checkpoint.
