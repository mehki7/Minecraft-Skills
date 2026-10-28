# Obfuscation and name resolution

## Confirmed state

Every class in `legacy-0.1.0-SNAPSHOT-all-nomappings.jar` — both Lunar's
own mixin classes and (presumed) the vanilla game classes they target —
uses ProGuard-style obfuscated names: random uppercase letter sequences,
e.g. `IOOCCRIRHHROHIHRCHHRRIOICHIOIR`. There is no MCP name, no searge
name, nothing human-readable anywhere in this jar. This matches the
"`com.moonsworth.lunar.*` is ProGuard-obfuscated with a published mapping"
claim from the original research — confirmed on this actual build.

`lunar-platform-mappings-v1_8.jar` is presumed (not yet confirmed) to hold
the mapping table that lets Lunar's own crash reporter retrace these names
back to something readable. Inventory it before assuming its format:

```
jar tf lunar-platform-mappings-v1_8.jar
```
(run with no filter — a previous attempt filtering for "map" in filenames
turned up nothing, which only means the files inside aren't literally
named with that word, not that the jar is empty or irrelevant)

## Resolving a specific mixin's target class

Each mixin `.class` file carries an `@Mixin` annotation whose value names
the class it patches, buried in the compiled bytecode's constant pool.
Reading this by hand (extract with `jar xf`, inspect with `javap -p -v`,
scroll a dump looking for the annotation) is slow and error-prone over a
chat interface — don't do it that way again. Use
[`RECON/02-mine-mixin-targets.py`](../../../RECON/02-mine-mixin-targets.py)
instead: point it at the jar and a `mixins.*.json` config, and it extracts
every listed mixin class, runs javap, and writes a markdown table of
candidate target classes plus the raw evidence for each one.

Treat the script's output as a strong lead, not gospel — the constant-pool
heuristic can occasionally pick up an unrelated class reference. Always
check the raw javap dump included in the output before hardcoding a target
name into real mixin code.

## Promoting an entry from LIKELY/UNVERIFIED to VERIFIED

Once you've confirmed a specific mixin's target class (by reading the raw
javap evidence, not just trusting the script's guess), move that specific
row into TARGET.md's VERIFIED section with the evidence attached. Don't
bulk-promote the whole UNVERIFIED list off one or two resolved classes —
each mixin needs its own confirmation.
