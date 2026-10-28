# Recover original behavior and compare references

Use when the requested result is faithful to an old mod, rather than an independently designed remake.

## Establish the reference

Identify the exact supplied version and hash. Inspect its manifest, registrations, assets, config defaults, data schema and relevant call graph. Use legally available source or authorized local binary inspection as reference material. Preserve original inputs; do not ship recovered third-party code or assets as part of a documentation package.

Write a behavior contract using concrete triggers and outcomes: input state, mutation sequence, return/exception, resource spending, RNG calls and externally visible effects. Compare executable behavior with guide text and explain disagreements. An adaptation can be reasonable, but must not be called original parity.

An upstream branch near the supplied binary's era is a separate reference, not proof of that binary's exact source revision. NEI's supplied 1.0.5.120 JAR and inspected 2015 `1.7` source branch had distinct identities. Its later JEI-backed implementation delegated core browser behavior and left legacy features missing; retain those differences in the coverage map rather than counting the replacement dependency as recovered parity. See [inventory/UI ports](inventory-ui-ports.md#choose-the-adaptation-deliberately).

## Using a maintained revival as the implementation base

Inventory the supplied binary before selecting a remake or revival. The [Mutant Creatures session](evidence.md#mutant-creatures) found snow golem, spider pig, creeper pets, eggs and equipment beyond the four best-known hostile mutants. An unrelated four-mob remake in the workspace did not satisfy that scope. The selected Mutant Monsters branches were pinned separately from the original JAR; their code and dependencies were identified to the user before implementation.

Keep inherited revival behavior, newly restored mechanics and original omissions separate in the coverage map. This port restored the craftable, stackable Chemical X bottle, single-target projectile behavior and 50% mutation probability, while retaining modern conversion, failed-attempt damage, spawning and equipment rules. A matching probability does not establish original target removal, eligibility, RNG continuation or failure ordering. Test modern behavior on its own terms and retain those differences even when all selected checks pass.

Explain replacement dependencies in player-facing terms. Here, Puzzles Lib supplied shared registration/configuration/network support and was required on the chosen targets; each bundle included the matching loader build alongside the mod. Preserving the revival's `mutantmonsters` namespace also meant duplicate-mod installation concerns and no automatic 1.7.10 save migration. Preserve both original and revival credits and separate code/asset rights.

## Make the comparison independent

Where practical, run an original method or bounded original service graph as an oracle, then feed the target the same scenarios. Do not generate both expected results and candidate code from the candidate logic. Record which helpers are original, simulated, stubbed or native. A correct isolated method does not prove its surrounding game lifecycle works.

The [DBC reports](evidence.md#dbc) distinguish controlled-helper attack transactions, complete composed original helper graphs, native server fixtures and client checks. They preserve details such as intermediate signed-byte conversion before absolute-value/capping, mastery work before knockout guards, attacker-selected Ultra Instinct counters, and target writes before malformed fusion data fails. These are bounded historical comparisons, not proof of the full port.

Choose vectors that expose ordering and boundary behavior:

| Dimension | Examples |
|---|---|
| Numeric representation | signed bytes, integer overflow/truncation, float thresholds, NaN/infinity only if the source permits them |
| Branches | early guards, Creative/Survival, player/NPC, source identity, absent targets |
| State | nondefault prior values, repeated calls, save/reload, reset/clone, stale caches |
| Failure | malformed tuples, null/index failures, helper callbacks that throw after a write |
| RNG | fixed seeds and the continuation after the operation, not only its immediate result |

Do not silently “clean up” a source quirk that is required for fidelity. If it must be changed, state the new behavior and reason. Test partial side effects before an exception when they matter; checking only the final exception type misses transaction ordering.

## Compose into the game

Bind recovered logic to native saved state, configuration, entities, inventory, damage and packets. Verify each bridge's semantics. Then exercise ordinary activation paths: player tick, attack/hurt, death/respawn, login/logout, client cache, menu and rendering. A manual fixture that calls an adapter directly is evidence for that adapter, not automatic hook activation.

Maintain a full-port checklist that includes dependencies and unmapped helpers. DBC's latest saved checkpoint explicitly leaves ordinary activation and wider lifecycle systems unfinished. Keep an incomplete label even when a large batch of comparisons passes. Use [checkpoint practice](testing-release.md) to preserve the proven stopping point.
