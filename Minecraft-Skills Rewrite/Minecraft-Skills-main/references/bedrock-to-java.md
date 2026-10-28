# Bedrock to Java: content and behavior mapping

## Inventory before conversion

Inspect `.mcaddon`/`.mcpack` containers and nested packs without executing their scripts. Read manifests, behavior/resource packs, entity events/component groups, client entities, render/animation controllers, geometry, textures/materials, sounds, scripts, items, recipes, loot and structures. Record malformed files and missing referenced resources.

Count playable species separately from alternate forms, helpers, projectiles, corpse/lifecycle states and vanilla overrides. Kaiju Craft v3's 51 source entity files yielded 11 Java forms, not 51 independent kaiju. Pack updates can remove systems: v3 did not contain v2's armor/crafting-block/structure content. Do not silently mix them. [Evidence and limitations](evidence.md#kaiju).

Use one identifier map through registrations, recipes, tags, events, loot and scripts; include namespace collisions and vanilla spelling differences. Make the coverage map system-based as well as entity-based.

The [Portal Gun session](evidence.md#portal-gun) adds item-heavy examples: accept the source's supported comment/trailing-comma JSON syntax without hiding genuine parse errors; retain valid dotted IDs; resolve actual geometry/texture aliases rather than assuming every client definition has a `default` key. Verify identifier substitutions against the target registry: changing valid Java `minecraft:ender_eye` to an English-looking alternative broke brewing. Source loot must be read rather than guessed, and unused shaped-recipe keys may need removal. See [interactive item ports](interactive-item-ports.md) for the fixes and limits.

| Source system | Java work | Limit to disclose |
|---|---|---|
| Component groups and events | goals, state transitions and explicit persistence | Simplified AI, omitted helpers or altered selection/timing |
| JavaScript | ownership, timers, commands, upgrades, progression, attacks | Bedrock Script API does not run as Java mod code |
| Molang/controllers | supported animation evaluation or Java state/controller logic | Constants/fallback clips alter source behavior |
| Geometry/materials | preserve hierarchy, pivots, UVs and target render path | Material, culling, scale and animation differences |
| Audio | real conversion to supported Java audio plus `sounds.json` | Absent source clips cannot be reconstructed by conversion |
| `.mcstructure` | translate NBT schema, palette/properties, positions and entity/block data | Unsupported blocks, commands and placement differences |
| UI/cameras | implement Java menus/views where required | Chat or vanilla perspective is an adaptation |

## Preserve interactions and state

Translate owner-only commands/riding, faction rules, growth, revival and form changes intentionally. Test multiple nearby entities so selection/ownership errors are visible. Transformations should preserve the required owner, rider, health fraction and cooldown state; specify exceptions if the source does something else. Summoning needs player-relative placement when expected, including underground.

The historical 1.20.1 kaiju ports handled source effective HP beyond the target's standard 1024 MAX_HEALTH cap by scaling **both damage and healing**, with effective HP in the boss UI. Test save/load, transformation, incoming damage and healing together. This is a target-specific solution; inspect limits in another target before applying it. Do not “correct” conflicting HP values silently—record source JSON, guide values and the chosen adaptation.

For structures, map newer/unavailable blocks explicitly, retain dimensions, and test placement/spawners/loot. v2 records replacements such as newer tuff masonry to stone-brick variants. Copying Bedrock NBT into a Java data pack or flattening blocks into one layer is not a conversion. Decide separately how command/script behavior survives.

Geometry does not establish a playable feature by itself. Portal Gun's summon-only distiller had no client appearance or distillation script/recipe, and its synthesis-bench model had no exposing item/block. The port documented dormant/omitted content instead of inventing those functions. Apply the same source relationship check before treating unused assets as missing gameplay.

## Render and deliver honestly

Inspect separately animated parts such as Ghidorah's wings. Mothlley's low-alpha emissive pixels and Rophan Spirit's intentional translucency required different mappings; making every texture opaque is incorrect. See [asset QA](rendering-assets-sfx.md).

The v3 and Legacy ports intentionally simplified factions, choreography, corpse/death states, cameras, multi-beam attacks, particles and unsupported Molang. Legacy also recorded 45 missing source audio references. Six/eight passing GameTests and many rendered models established useful alpha behavior, not complete Bedrock parity.

Build the finished project under its own target toolchain. Inspect archived generators before reuse: the kaiju conversion archive warns that rerunning them can overwrite later manual fixes. Deliver a loadable artifact, buildable source, exact dependencies, credits and a concrete adaptation/coverage report. Keep source creator rights intact.
