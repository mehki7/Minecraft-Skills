
**Added 2026-10-31 - GuiIngame inject results:**

- **`func_175183_b` (`showCrosshair`, `()Z`) - VERIFIED LIVE.** Inject fired:
  `[STDOUT]: [PORT-GUIINGAME] *** INJECT PASS -- showCrosshair fired ***`
  tsrg line: `    showCrosshair ()Z func_175183_b`
  This is the second distinct class proven, so the pipeline is not EntityRenderer-specific.

- **`func_175180_a` (`renderGameOverlay`, `(F)V`) - TAIL UNREACHABLE.** Inject registered cleanly (defaultRequire 1 would have thrown on a bad name) but never fired. `showCrosshair` is called from inside this method and it does fire, so the method runs - the TAIL is simply never reached. Cause is likely an early return or Lunar replacing the method body.
  **Rule: never inject at TAIL in Lunar's GuiIngame. Use HEAD or a specific call site.** HEAD test on this method pending.

- **Duplicate `@Inject` on one method is safe.** FuriahVisuals also injects `func_175183_b`; two `@Inject` callbacks both run, Mixin stacks them. Only `@Overwrite` or `@Redirect` on the same call actually collide. `showCrosshair` is usable as-is, no priority work needed.

- **`func_180475_a` (`renderScoreboard`) - LIKELY, not yet tested.** Not in tsrg yet - resolve with `findstr renderScoreboard` before use.
