# Debugging a Lunar mixin port

## First, turn on Mixin's own diagnostics

Launch with:
```
-Dmixin.debug=true -Dmixin.checks=true -Dmixin.verbose=true
```
This surfaces mixin application failures in the log instead of silently
no-op'ing or producing a confusing downstream error.

## Common failure shapes and what they usually mean here

- **"Target class not found" at mixin-apply time** — the obfuscated name
  you hardcoded doesn't exist in this exact build. Either the RECON
  extraction/guess was wrong, or (more likely if this worked before) the
  Lunar build has been auto-updated and the obfuscation mapping shifted.
  Re-run RECON against the current jar — see
  [canary-pinning.md](canary-pinning.md).
- **Crash referencing `com.moonsworth.lunar.*`, obfuscated garbage class
  names in the stack trace** — this is where
  `lunar-platform-mappings-v1_8.jar` (once inventoried) should let you
  retrace the obfuscated name back to something readable, the same way
  Lunar's own crash reporter does.
- **Mixin silently does nothing, no crash, no log entry** — check whether
  your config is actually being loaded at all (is it referenced anywhere
  Lunar's bootstrap reads from? See the open question in
  [external-mods.md](external-mods.md) about whether there's a real
  drop-in loading mechanism for custom configs on this lane).
- **A clean `./gradlew build` with no runtime verification** — this is
  explicitly called out as a non-answer in the original plan's
  "Definition of done." A successful compile only proves the Java is
  syntactically valid against your shimmed/hardcoded names — it says
  nothing about whether Mixin actually attached anything at runtime.
  Always do the in-game check with the debug flags above before calling a
  port finished.
