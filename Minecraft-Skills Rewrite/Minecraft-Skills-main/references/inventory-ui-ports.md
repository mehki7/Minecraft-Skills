# Inventory browsers, screens and utility ports

Use when porting an item/recipe browser, an inventory editor or a client UI with server actions. The [NEI session](evidence.md#not-enough-items) provides two tested modern adaptations; it does not establish a complete legacy port or a universal JEI integration template.

## Choose the adaptation deliberately

Separate the original mod's features from a replacement library's features. In NEI, JEI supplied item search, recipes, usages, bookmarks and supported recipe transfer; the new mod supplied inventory/world tools. This introduced a required client dependency and changed the subset UI, configuration and add-on API. Explain those tradeoffs when they materially change the requested product. A working successor library does not itself satisfy a request for a faithful or self-contained port.

Keep the complete original feature map visible, including omissions. The NEI result left Creative+, spawner editing, the block tooltip HUD, old permission/locking configuration and binary add-on compatibility unimplemented. Passing the modern utility tests did not close those gaps. A prerelease label describes delivery status; it does not restore missing scope.

For each game version, pin a compatible library artifact and inspect its metadata, API and nested dependencies. The observed JEI 15/19 artifacts included MezzConfig internally; that is not evidence that every future dependency is bundled. Deliver the exact required JARs and preserve their licenses. Distinguish a mod-only download from a bundle that includes dependencies.

## Keep shared behavior behind small target adapters

The NEI projects shared utility commands, screens and behavior checks. Target-specific adapters handled item serialization, enchantment registries, GUI property accessors and render-event types. This avoided treating a Java version change as the whole Minecraft port.

| Boundary observed in the pinned targets | Implementation consequence |
|---|---|
| 1.20.1 NBT-era stacks versus 1.21.1 data components | Use native registry-aware item serialization for the target. Preserve count, enchantments and potion effects; do not reconstruct snapshots from item ID/count alone. |
| Static 1.20.1 enchantments versus dynamic 1.21.1 world registry | Populate the editor from the connected world's registry; validate the selected identifier on the server. |
| JEI 15 `IGuiProperties.getGuiLeft()`-style methods versus JEI 19 `guiLeft()`-style methods | Compile separate adapters against the actual dependency versions. Do not assume one interface signature across targets. |
| Forge render-stage pose types differ | Inspect the target event and transform the overlay with its actual pose/camera API; a compile-only check does not establish correct world placement. |

These boundaries are observed in NEI's pinned builds, not a complete API migration matrix. See [the target tuples](loader-version.md#observed-project-tuples-not-universal-defaults).

## Treat GUI lifecycle and caches as behavior

Registering a JEI plugin and receiving its runtime did not prove that its item panel was visible. The custom tools screen was first queried before initialization, with zero dimensions. Returning a properties object that referenced the mutable Screen also made JEI's previous and current values appear equal after the dimensions changed; its invalid-screen cache persisted.

The evidenced repair returned no GUI properties until dimensions were valid, then captured primitive position/size values in a new immutable snapshot. This lets value comparisons observe initialization and later changes. Keep the actual panel bounds separate from the full screen dimensions, declare exclusion areas for added controls and use the target's normal background/render lifecycle. Calling the background method alone was not the cache fix.

Exercise the ordinary inventory button through the Screen mouse handler, then separately assert that JEI's list is displayed. Inspect the frame and search/recipe interactions. The NEI client regression now checks panel visibility in addition to screen type and server effects. Other GUI scales, resizing and arbitrary modded container layouts remain proposed checks rather than established coverage.

## Validate the input path and the resulting state

Client-side disabled buttons are not permission enforcement. NEI's server commands gate inventory/world mutation at permission level 2, while save-only commands remain available without that permission. Its negative tests execute the registered command tree with a non-operator source and assert that rejected operations do not change inventory. A packet-based port needs equivalent checks in its server handler; adopting commands is an implementation option, not a universal requirement.

Brigadier's unquoted word parser did not accept the namespaced comma-separated potion effect list. The screen appeared to work while no potion was given. The repair used a quoted string argument for that list and quoted the outgoing value. A typed resource-location argument remained appropriate for a single enchantment ID. Include a parser/dispatch regression with the real namespaced input; calling the potion factory directly had missed this bug.

Check stack counts and data after load/delete/undo, including armor, offhand and cursor. Apply/remove an enchantment and create multiple potion effects through the real UI/connection, then inspect native server state. A serialization roundtrip does not prove death/relog or cross-version save migration. A magnet toggle flag does not prove attraction: the connected NEI test waited for normal player ticks and verified collection of three dropped ingots before disabling it.

## Failures and bounded fixes

| Observed failure | Repair / verification | Limit |
|---|---|---|
| Forge 52.1.0 compiled but found zero entrypoints in the resource directory | Retained the exact MDK's merged class/resource output; mod loading then passed | Specific template/runtime requirement; do not impose it on every loader |
| 1.21.1 GameTest filtering selected no functions after prefixing changes | Set the intended batch explicitly and require selected required tests to pass | Check the exact target's annotations and filter semantics |
| 1.20.1 native mock-player connection had a null channel | Used Forge FakePlayer for nonnetwork checks; tested real packets separately | FakePlayer is not ordinary player-tick evidence |
| Custom tools screen loaded with no JEI item panel | Deferred uninitialized properties and used immutable dimension snapshots; added a visibility assertion | One exercised client layout, not every container/scale |
| Potion factory worked, but its UI command produced no item | Quoted namespaced effect list plus production command regression and connected item check | Other command payloads need their own argument model |

The 1.21.1 fixture used Minecraft's mock server player with an embedded connection; the 1.20.1 helper/Forge FakePlayer assumptions were not copied across. The GameTest and packaging details are also in [testing and releases](testing-release.md).
