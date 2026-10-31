package com.porttest.mixin;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

// refmap-verified: showCrosshair -> func_175183_b, called every render frame
@Mixin(targets = "net.minecraft.client.gui.GuiIngame", remap = false)
public abstract class MixinGuiIngame {
    private static boolean pg$logged = false;

    @Inject(method = "func_175183_b", at = @At("HEAD"), remap = false)
    private void pg$onShowCrosshair(CallbackInfoReturnable<Boolean> cir) {
        if (!pg$logged) {
            pg$logged = true;
            System.out.println("[PORT-GUIINGAME] *** INJECT PASS -- showCrosshair fired ***");
        }
    }
}