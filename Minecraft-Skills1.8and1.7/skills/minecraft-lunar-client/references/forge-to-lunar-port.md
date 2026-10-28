# Porting a Forge 1.8.9 mod's source onto Lunar

## Two realistic routes

**Route A — rewrite as Mixin (default, recommended).**
Take the mod's actual logic (the parts that aren't `@Mod`/FML
boilerplate) and re-implement the hook points as `@Mixin` classes
targeting Lunar's obfuscated runtime names (resolved via RECON — see
[obf-and-retrace.md](obf-and-retrace.md)). You lose Forge's registry API
and event bus entirely; vanilla-style direct field/method access replaces
them. This is more work up front but matches how Lunar's own first-party
code is built, so it's the path with the least friction against Lunar's
internals.

**Route B — forge-shim package (cheaper, narrower).**
Build a small local package (the original plan estimated ~40 classes)
that reimplements just enough of `@Mod`, a minimal event bus, and
`GameRegistry` against vanilla 1.8.9 registries, so the original mod's
source compiles with minimal edits. This only gets you compiling source —
it does nothing by itself to hook into Lunar's client, since Lunar has no
FML lifecycle to receive your shimmed `@Mod` class's calls. You'd still
need Mixin glue to actually wire the shimmed registration calls into
something Lunar invokes. Worth it mainly if the mod's logic is large and
you want to preserve its original structure rather than rewrite the hook
layer by hand.

Given the actual confirmed jar layout (one bundled `legacy-...jar`, not a
hosted plugin API), Route A is the more honest match for how this client
actually works. Only reach for Route B if a specific mod's source is big
enough that minimal-edit compiling is worth the extra shim-maintenance
cost.

## Steps either way

1. Confirm the target class(es) via RECON before writing any mixin code —
   do not guess a name.
2. Write the mixin with `remap = false` for any Lunar-internal target.
3. Compile with `mixin.env.disableRefMap=true`.
4. Build, then verify in-game with `-Dmixin.debug=true
   -Dmixin.checks=true -Dmixin.verbose=true` — a clean compile proves
   nothing about whether the mixin attached correctly at runtime.
5. If it crashes, see [debugging.md](debugging.md).
