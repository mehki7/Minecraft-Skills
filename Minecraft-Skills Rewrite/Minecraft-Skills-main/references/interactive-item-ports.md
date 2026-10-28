# Interactive item, menu and travel ports

These lessons come from the completed **Portal Gun v1.1.1** session on **Minecraft 1.20.1 / Forge 47.4.26 / Java 17 / GeckoLib 4.8.4**. They describe a playable **1.1.1-alpha.1 adaptation**, not complete Bedrock parity. [Session identity, reports and hashes](evidence.md#portal-gun).

## Carry state and interactions across the port

Inventory scripts alongside item/entity JSON. This source's five guns, fluid assembly/refill/depletion, configurable graph modes and saved destinations required Java gameplay, packets and persistent records; copying geometry could not implement them.

- Keep valid source IDs and use a collision-resistant identity for each tool. Portal Gun retains `ram_pg` and dotted item IDs, while adapting a small random integer to a UUID. Its tests preserve identity and partial charge across assembly and dismount/refill.
- Keep active link records authoritative in world saved data rather than relying only on an inventory-held list. Check reciprocal references, unloaded-aware removal, close-all and mode/destination changes.
- Define graph invariants per mode. The source's FIFO, LIFO, independent pairs and root/child links have different removal/update rules. Exact portal caps and mode names are this source's design, not universal requirements.
- Validate action sender, held hand/tool identity and bounded input on the server. The inspected network checks the UUID still belongs to the held gun; the local client exercises the real save/use packet paths. General adversarial packet robustness was not tested.
- Reject forbidden actions before charging or placing content. The blue-gun cross-dimension check demonstrates no charge loss or placement; it does not imply every invalid setting path was covered.

For travel, distinguish the original entity from the replacement returned by cross-dimension movement. The inspected 1.20.1 implementation supplies arrival information through `ITeleporter`, applies guard/cooldown data to the moved entity, temporarily activates portal/destination chunks and clears reentry protection through the registered level-tick event after the entity leaves. Test a cold dimension, exit, guard clearance and return by UUID. Mounted entities/occupied vehicles were intentionally excluded, so a successful unmounted cow/player trip does not certify rider transport.

## Failed approaches and evidenced fixes

| Observed failure or correction | Actual fix and evidence | Reusable decision |
|---|---|---|
| Strict parsing rejected comments/trailing commas; client definitions did not always use `default` aliases | The converter accommodated the inspected syntax and actual alias maps; final inventory reports no malformed source JSON | Use the source's documented syntax and resolve semantic aliases. Do not generalize “take the first map entry” to ambiguous definitions. |
| Guessed `ender_eye` renaming broke interspatial brewing | The diff removes the incorrect substitution; final tests assert all eight output conversions | Verify target registry IDs, then exercise outputs. Valid identifiers need no English-name rewrite. |
| Quantum isotope's generated drop was guessed as an empty beaker | Converter now reads source loot; a final native block-drop assertion checks the isotope item | Preserve actual source loot, not a plausible simplification. |
| Mock-player teleport setup failed because its network channel was null | 1.20.1 tests use `FakePlayerFactory` and nonnetwork positioning; real client packets remain a separate QA route | Separate game-logic fixtures from network/lifecycle evidence; diagnose the fixture before changing production gameplay. |
| The poison shot missed the cow despite emitted projectiles | Fixture aim was corrected into its body; final checks observe both effects and death through world ticks | Assert a real hit and outcome. Changing wait durations alone does not fix missed geometry. |
| GeckoLib's polygon deserializer rejected source indexed vector data | Source `poly_mesh` is retained separately and drawn by a pack-specific adapter on animated bone matrices | Check exact library support before loading foreign geometry. Preserve topology/UVs/pose; do not silently drop polygons. Arbitrary topology is unverified. |
| Renderer resource paths contained `null` after early item initialization | Item model names changed from captured strings to lazy suppliers; subsequent client checks completed | Match resource lookup to registration/construction timing rather than supplying dummy assets. |
| Hair was misplaced, held guns oversized, icons offset and menu clipped | Diffs adjust source-specific pivots/hand transforms, route GUI icons separately and center them; scaled GUI drawing also transforms mouse coordinates | Check each viewing context. Drawing scale and input hit-testing must agree; these numeric transforms are not portable defaults. |
| Holding a block-hit action could repeat cycling | The event handler responds to the `START` action and cancels later phases for relevant items | Identify event phases before treating one player action as one callback. This is source-inspected, not exhaustive physical-input QA. |
| Nether travel required correct arrival info and exit-guard cleanup; a warm-world pass later failed in a fresh world | Diffs add explicit arrival info, transient chunk tickets and level-tick cleanup; the final cold-world fixture permits activation and waits for the returned live replacement, then all nine required tests pass | Exercise ordinary activation and return in fresh worlds. Keep bounded state-aware waiting distinct from weakening an assertion. |
| Menu list state disappeared during rebuilding | The source preserves search text across list rebuilding and clears it when changing pages | Track UI state intentionally; search/rename/delete were not exhaustively exercised by the final packet checks. |

The renderer also retains compatible gun ray/bubble curves and slices the source's portal swirl into 75 frame textures. Java owns sound/gameplay triggers, while removed Bedrock particle keyframes, shader glow and camera choreography remain adaptations. The source's low-alpha solid pixels and genuine glass transparency need different handling. All 17 supplied OGG sound events decoded; listening quality remains unreviewed.

## Verification and chronological delivery

Historical QA covers nine required server GameTests, production save/use/travel packets on a real local client with integrated server, and representative gun/portal/equipment/menu captures. Item/world NBT round trips establish serialization, not a real crash/restart. All 13 crafting resources load and eight brewing conversions produce specified outputs; this does not show every crafting GUI interaction or a full Survival progression session.

The session clean-builds without its validation flag and reobfuscates the release, then inspects class target 61, metadata/dependencies, recipes and absence of QA payloads. Its dependency JAR is delivered alongside the mod. Runtime QA used development classes; neither packaging inspection nor later user feedback rewrites that fact.

The build-time documents predate the user's explicit installation request. The later receipt verifies both copied hashes and records no tooling launch, then the supported session records user confirmation that it worked. Treat that as an actual user outcome with unspecified depth. Update documentation from this timeline rather than repeating the earlier “not installed” statement as current state.

**Checked during this knowledge update:** exact session identity/three turns, relevant reports/diffs/source, source archive and both artifact hashes, ZIP integrity/class target/QA exclusion/recipe metadata, and visual review of three saved final frames. **Not rerun:** Minecraft, GameTests, screenshot capture, listening or installation. Source revision is untracked in its workspace; selected file hashes identify the inspected state.
