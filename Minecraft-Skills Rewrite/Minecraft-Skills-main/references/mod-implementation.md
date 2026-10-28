# Mod implementation

Use the target loader's source/template for syntax; this guide carries behavior lessons rather than a universal API scaffold.

## Implement a small playable slice

Choose a stable mod ID and explicit feature IDs. Connect registration, attributes/components, item/entity definitions, translations, recipes, loot, spawn rules and client assets. Test one complete path before expanding: obtain or spawn the content, interact with it, observe gameplay, save/reload, and inspect its appearance.

Separate common game logic from client rendering/input. Make the server authoritative for damage, energy, cooldowns, ownership and movement permissions; validate action indices, range, target state and equipment. A rendered client's input should reach the production packet handler rather than only a test shortcut.

For stateful tools and travel systems, read [interactive item ports](interactive-item-ports.md): stable tool identity across assembly/depletion, authoritative world records, server-validated menu actions, graph-mode cleanup and cross-dimension entity replacement need separate checks. Portal Gun's level-tick exit-guard cleanup and transient portal chunk tickets were source-inspected; its nine historical server checks and connected local client checks remain bounded evidence.

For inventory browsers and administrative screens, read [inventory/UI ports](inventory-ui-ports.md): cached GUI properties, dependency-owned overlays, quoted command payloads, native stack metadata and server permission gates need checks along the actual input path. A working screen or factory is insufficient if the list is hidden or the command never reaches a state-changing handler.

## Player powers and lifecycle

[X-Men, Justice League and Avengers reports](evidence.md#local-mods) supply concrete examples:

- Require the matching equipment state, and reject mixed/incomplete sets where the design calls for a full suit.
- Stop beams, holds, flight, weather visuals, modifiers and orphan projectiles on invalidation.
- Exercise real death/respawn and disconnect handlers. Tests that invoke cleanup themselves can miss a broken event binding.
- Restore only permissions/effects owned by the mod; preserve preexisting Creative flight or unrelated effects.
- Separate a simulated persisted-marker recovery test from a real server crash/restart test.
- Bound movement and sweep collision; reject unloaded destinations and validate sight/cover for attacks.

Use observable assertions: target health, saved fields, inventory consumption, player velocity, effect ownership, cleanup and expiry. A successful key event or visible beam alone does not prove server damage.

## Mobs, attacks and giant bodies

Give an encounter explicit telegraph, impact and recovery states with sensible cancellation and persistence. Check target acquisition without manually assigning the target. Respect the chosen rules for Creative/Spectator, peaceful difficulty, factions and terrain protection.

ZillaCraft/Kong use fitted body/tail hitboxes to make giant silhouettes attackable; [the mashup](evidence.md#mashup) carries the body-box concept into Rust. Test melee, projectiles and explosions against the intended owner and avoid duplicate damage from overlapping parts. A single center box or enlarged visual model does not establish full-body collision. Keep movement support/collision rules separate from rendering scale.

## Spawning, worldgen and travel

[Astra Nether](evidence.md#astranether) reproduced a boss that selected a Survival player but did not hurt them in its first attack cycle; the fix was checked with actual player damage after the telegraph. Its accelerated spawning test proved the natural-spawner path, not a passive encounter-frequency estimate.

Test registration, placement predicates and actual spawning/generation separately. Use the full scaled body for clearance, liquids and support checks. Verify rare-spawn spacing and biome/dimension rules with the production predicates. New worldgen features and existing generated chunks need different expectations.

For portals/dimensions, verify outbound and return travel, safe arrival, broken/obstructed frames, death/respawn, riders and persistent return data. Sift's reports test these paths while explicitly identifying invented mechanics; reference footage is insufficient evidence for unshown behavior. [Sift source](evidence.md#sift).

Keep a feature-to-test map. Add tests for regressions and meaningful invariants rather than generating tests that mirror implementation wording. Finish with [production validation](testing-release.md).

For large batches, BerthaCraft's project layout illustrates keeping feature-owned paths separate from shared registries/resources. Integrate shared language, loot, spawn and recipe data structurally, check ID/order collisions, then validate the combined artifact and maintained target branches. This organization can help avoid merges that compile while leaving a feature unregistered; it does not mandate parallel agents or a fixed module layout for every mod.
