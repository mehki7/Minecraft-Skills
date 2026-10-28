# Minecraft-SkillsMiwr (Mixed — 1.8.9 + 1.7.10, Multiple Launchers)

Agent skill pack for modding Minecraft 1.8.9 and 1.7.10 across multiple
launchers and clients: Lunar Client (mixin lane), OneClient, and plain Forge.

## Version scope

| Version | Status |
|---|---|
| 1.8.9 | **Primary** — highest priority |
| 1.7.10 | Secondary |
| 1.12.2 and newer | **Explicitly excluded** |

## Launcher/client scope

| Launcher / Client | Skill to read |
|---|---|
| Lunar Client 1.8.9 (mixin lane) | `skills/minecraft-lunar-client/` |
| OneClient 1.8.9 | `skills/minecraft-oneclient/` |
| Plain Forge 1.8.9 | `skills/minecraft-legacy-modding-189/` |
| Plain Forge 1.7.10 | `skills/minecraft-legacy-modding-1710/` |

## Order of use

1. Read `TARGET.md` first — ABI pins and VERIFIED/UNVERIFIED status for Lunar.
2. Identify your launcher/client (see table above).
3. Load the matching skill's `SKILL.md`.
4. Read the relevant reference files under that skill's `references/` folder.
5. For Lunar-specific work: run `RECON/02-mine-mixin-targets.py` before writing
   any mixin code (required to resolve obfuscated class names).

## Why separate skills per launcher instead of one merged skill

Each launcher has meaningfully different constraints:
- **Lunar Client**: Java 17 toolchain, ProGuard-obfuscated classes, Mixin only, no FML.
- **OneClient**: Forge-based but with its own classloader quirks and potentially
  its own mixin/coremod layer. Read `minecraft-oneclient/SKILL.md` for specifics.
- **Plain Forge 1.8.9**: Java 8, ForgeGradle 2.1, FML lifecycle, MCP stable_22.
- **Plain Forge 1.7.10**: Java 7/8, ForgeGradle 1.2, FML lifecycle, MCP stable_12.

A single merged skill would force an agent to carry all four sets of assumptions
simultaneously and risk mixing them (e.g. applying Java 17 Lunar patterns to a
plain Forge 1.7.10 project). Separate skills with explicit routing is safer.

## Contents

- `TARGET.md` — Lunar Client ABI pin and verification status
- `VALIDATION.md` — structure and gap check
- `RECON/` — recon scripts for Lunar internals
- `prompts/workflows.md` — parameterized prompt templates for all four targets
- `skills/minecraft-lunar-client/` — Lunar Client 1.8.9 mixin lane
- `skills/minecraft-oneclient/` — OneClient 1.8.9
- `skills/minecraft-legacy-modding-189/` — plain Forge 1.8.9
- `skills/minecraft-legacy-modding-1710/` — plain Forge 1.7.10
