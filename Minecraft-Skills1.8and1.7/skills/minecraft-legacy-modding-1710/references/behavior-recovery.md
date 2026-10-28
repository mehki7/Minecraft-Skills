# Behavior recovery and reference comparisons — 1.8.9 / 1.7.10

Use when the goal is faithfulness to an older mod version, not an independently
designed remake. Adapted from the main minecraft-modding skill's behavior-recovery
guide, scoped to 1.7.10/1.8.9 targets only.

## Establish the reference

Identify the exact supplied version and hash. Inspect its manifest, registrations,
assets, config defaults, data schema, and relevant call graph. Use legally available
source or authorized local binary inspection as reference material. Preserve original
inputs; do not ship recovered third-party code or assets as part of a documentation
package.

Write a behavior contract using concrete triggers and outcomes: input state, mutation
sequence, return/exception, resource spending, RNG calls, and externally visible
effects. Compare executable behavior with guide text and explain disagreements. An
adaptation can be reasonable, but must not be called original parity.

An upstream branch near the supplied binary's era is a separate reference, not proof
of that binary's exact source revision.

## Coverage map format

| Feature | Source behavior | Target implementation | Status | Behavior difference |
|---|---|---|---|---|
| (system) | (trigger → outcome) | (how you implemented it) | implemented/adapted/omitted | (explicit delta) |

Use `implemented`, `adapted`, `omitted`, `blocked`, or `unverified`. Keep inherited
behavior, newly restored mechanics, and original omissions separate. Do not call
something `implemented` if only the compile passes — verify the actual in-game
trigger → outcome chain.

## Comparing behavior across versions (1.7.10 ↔ 1.8.9)

When recovering behavior from a 1.7.10 source into a 1.8.9 target (or vice versa),
the rendering system difference (see legacy-1710-diffs.md) means visual behavior
cannot be ported 1:1 — document the adaptation explicitly. Game logic (damage,
inventory, entity state, RNG) is generally more portable, but always verify with
the actual pinned Forge versions rather than assuming API compatibility.

## Make the comparison independent

Where practical, run an original method or bounded original service graph as an oracle,
then feed the target the same scenarios. Do not generate both expected results and
candidate code from the candidate logic. Record which helpers are original, simulated,
stubbed, or native.

Choose vectors that expose ordering and boundary behavior:
- Numeric representation: signed bytes, integer overflow, float thresholds
- Branches: early guards, Creative/Survival, player/NPC, absent targets
- State: nondefault prior values, repeated calls, save/reload, stale caches
- Failure: malformed tuples, null/index failures
- RNG: fixed seeds and the continuation after the operation

Do not silently "clean up" a source quirk required for fidelity. If it must change,
state the new behavior and reason.

## Compose into the game

Bind recovered logic to native saved state, entities, inventory, damage, and packets.
Verify each bridge's semantics. Then exercise ordinary activation paths: player tick,
attack/hurt, death/respawn, login/logout. A manual fixture that calls an adapter
directly is evidence for that adapter, not automatic hook activation.
