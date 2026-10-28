# Package validation — Minecraft-SkillsMiwr (Mixed)

## Scope check

This package covers:
- Minecraft 1.8.9 (primary) — Lunar Client, OneClient, and plain Forge
- Minecraft 1.7.10 (secondary) — plain Forge only
- NO version newer than 1.8.9 is referenced
- 1.12.2 is explicitly excluded throughout all skills

## Structure check

Required files present:
- [x] `README.md`
- [x] `TARGET.md` — Lunar Client ABI pin
- [x] `VALIDATION.md`
- [x] `RECON/02-mine-mixin-targets.py`
- [x] `prompts/workflows.md`
- [x] `skills/minecraft-lunar-client/SKILL.md`
- [x] `skills/minecraft-lunar-client/references/` (7 reference files)
- [x] `skills/minecraft-oneclient/SKILL.md`
- [x] `skills/minecraft-oneclient/references/` (4 reference files)
- [x] `skills/minecraft-legacy-modding-189/SKILL.md`
- [x] `skills/minecraft-legacy-modding-189/references/` (7 reference files)
- [x] `skills/minecraft-legacy-modding-1710/SKILL.md`
- [x] `skills/minecraft-legacy-modding-1710/references/` (6 reference files)

## Client/launcher coverage

| Launcher | Skill | Java | Toolchain | Status |
|---|---|---|---|---|
| Lunar Client 1.8.9 | minecraft-lunar-client | 17 | No FG — Mixin only | Confirmed from real install |
| OneClient 1.8.9 | minecraft-oneclient | 8 | FG2.1 (Forge-based) | Partially confirmed — inventory install for hooks |
| Plain Forge 1.8.9 | minecraft-legacy-modding-189 | 8 | FG2.1, MCP stable_22 | Standard well-documented target |
| Plain Forge 1.7.10 | minecraft-legacy-modding-1710 | 7/8 | FG1.2, MCP stable_12 | Standard well-documented target |

## Gap analysis vs outdated template

Same as `Minecraft-SkillsLunar1_8Only/VALIDATION.md` for the gaps that are
intentionally excluded (Bedrock, interactive item ports, inventory UI ports, SFX).
The Miwr pack adds full 1.7.10 and OneClient coverage that the 1.8-only pack omits.

| Template reference | This pack | Notes |
|---|---|---|
| Loader/version selection | Per-skill toolchain refs + TARGET.md | Covered per launcher |
| Java version ports | version-diff-1710-189.md in both 189 and 1710 skills | 1.7.10 ↔ 1.8.9 only |
| Behavior recovery | behavior-recovery.md in both 189 and 1710 skills | Present |
| Mod implementation | legacy-189-api.md, legacy-1710-api.md | Both eras covered |
| Testing/release | testing-release.md + build-and-validate.md | All clients covered |
| Parameterized prompts | prompts/workflows.md | All four targets covered |
| Bedrock-to-Java | Not included | Out of scope |
| Rendering/SFX | Not included | Add when a specific task requires it |
