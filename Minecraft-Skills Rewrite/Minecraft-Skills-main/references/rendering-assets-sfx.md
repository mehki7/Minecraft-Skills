# Models, rendering, assets and SFX

## Preserve geometry; validate appearance

Keep bone hierarchy, pivots, rotations, UVs, texture dimensions and material intent. Distinguish geometry scale, renderer scale, collision size, attack reach and rider placement. Source geometry can already contain scale; multiplying it again can distort a port.

ZillaCraft's [documented asset tools](evidence.md#zillacraft) generate geometry and textures together using texel positions in 3D and offer per-creature regeneration and previews. This is one inspectable workflow, not a guarantee of artistic quality. Review the output and diffs before regenerating assets; use copies when generator behavior is uncertain.

For the **inspected 26.2 / Forge 65.1.3** rendering path, BerthaCraft's source-verified notes describe deferred drawing, shared model instances, render-state animation and visibility. Populate per-frame state, derive pose/visibility at draw time, and explicitly reset both branches of visibility flags: `resetPose()` does not reset `visible`/`skipDraw` in that inspected API. Do not transfer these exact names/signatures to 1.20.1 or another loader without checking its sources. Historical Techne mirroring configured after box creation could have had no effect; activating it during translation changes the original mesh. [BerthaCraft rendering evidence](evidence.md#berthacraft).

## A practical preview ladder

This combined workflow is a **recommendation**, informed by reported project tools and rendering checks; no universal preview system was tested here.

1. Render neutral front/side/rear views with a scale reference and clear background. Inspect silhouette, feet placement, symmetry and UV/material seams.
2. Preview idle/walk/attack extremes, separate wings/accessories and glow/translucency. Inspect transforms at more than one pose.
3. Use the actual target Minecraft client for lighting, culling, animation, multi-entity shared-model state and resource reload.
4. Check inventory, first/third person and both hands where supported for held equipment. GUI hiding can also hide the first-person hand; confirm the capture setup before diagnosing missing geometry.
5. For oversized mobs, inspect camera-edge disappearance and multipart coverage during motion. ZillaCraft's standing/stride dumps and fitted hitbox tool report sampled coverage; that does not prove every possible animation pose.

Check that automation reaches gameplay and that the pixels show its intended subject. Mutant's first client harness encountered accessibility onboarding before the title screen; early gallery frames then looked away from registered entities because the client camera rotation had not been set. Correcting the harness produced seven reviewed neutral creature views per target. A non-null renderer and received entity are registration/network evidence, not proof of a visible pose. Its final combat frame did not demonstrate an attack pose even though a separate assertion observed synchronized attack animation. [Recorded source and limits](evidence.md#mutant-creatures).

Use [Bedrock material mapping](bedrock-to-java.md) where applicable. Emissive alpha encoding can be mistaken for transparency, but actual spirit translucency and transparent holes must survive. Alpha-blended glow layers also need a transparent background rather than an opaque black rectangle.

Portal Gun exposed two additional **1.20.1 / GeckoLib 4.8.4** failures: the source polygon representation could not load directly, and an item renderer captured its name before item initialization finished, producing `null` resource paths. A pack-specific mesh adapter retained polygons on animated bone transforms; lazy name lookup corrected initialization timing. Its captures also drove head-pivot, held-scale, icon-centering and scaled-menu input fixes. These are versioned solutions, not a universal GeckoLib converter. See [the failure/fix record](interactive-item-ports.md#failed-approaches-and-evidenced-fixes).

## Sound provenance, validity and quality are separate

| Question | Evidence needed |
|---|---|
| May this clip be used? | creator/license/source record or original synthesis provenance |
| Will it load? | actual audio decode, supported format and complete event/file mapping |
| Does it play correctly in game? | trigger, volume/pitch, attenuation, category, repeat/overlap and distance checks |
| Does it sound good? | listening comparison in context and user review |

Convert WAV with an actual audio encoder (for example, ffmpeg to Vorbis OGG); renaming an extension is insufficient. Check channel requirements for spatial effects against the target. Keep a sound inventory: event, file, provenance, conversion, missing references and review status. Report missing source clips—Legacy's absent references were not recoverable from pack data.

Portal Gun already supplied OGG audio: 17 sound events decoded in its resource checks, with listener quality still unreviewed. Its converter removed Bedrock sound/particle animation keyframes while Java gameplay owned the triggers, and corrected yellow-portal event selection. When adapting effects, assign trigger ownership explicitly to avoid duplicate playback and list any removed particle/choreography behavior; file validity is not listening evidence.

Distinguish sound-definition event IDs from each entry's file/event reference. Resolve entries with the target's namespace rules and distinguish `type: event` from a file before checking archive paths. Mutant's audit initially misclassified an unqualified vanilla illusioner clip as a missing mod-owned OGG; the corrected 1.21.1 resolver used the default `minecraft` namespace. The [NeoForge sounds guide](https://docs.neoforged.net/docs/1.21.1/resources/client/sounds/) documents the file/event forms. Forty custom OGG files decoded per target in that session, with listener quality still unverified because client audio was muted.

## Audit serialized resource bytes

Validate the packaged JSON as UTF-8, including locales not selected during the client run. Mutant's Forge Spanish locale contained a legacy encoding that an English client session did not exercise. Its known source encoding was converted deliberately and the final packaged JSON parsed successfully; that does not establish a Spanish-locale runtime check. Avoid silently treating every undecodable file as Latin-1. If a late fix changes resources only, recheck those resources and rebuild as needed; matching production class hashes alone says nothing about the changed resource bytes.

ZillaCraft and Sift document synthesized sounds. That establishes a source workflow, not access to a professional SFX library or user-approved fidelity. X-Men's report explicitly says audio was muted during automation despite decode/event checks. Do not call those sounds listener-verified.

When quality or library access is the obstacle, propose a small audible comparison set with the intended source/license, gain and in-game trigger. Review an isolated clip and its mix beside footsteps, music and attacks. Check clipping, harshness, overlap and near/far playback, then keep the selected source and settings reproducible. This listening workflow is proposed; no tested premium-library integration or universal sound generator is established by this inventory.
