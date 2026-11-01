package com.porttest.mixin;

import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

// func_175183_b (showCrosshair, ()Z) -- VERIFIED LIVE
// func_175180_a (renderGameOverlay, (F)V) -- TAIL unreachable, HEAD under test
@Mixin(targets = "net.minecraft.client.gui.GuiIngame", remap = false)
public abstract class MixinGuiIngame {

    private static boolean pg$crosshair = false;
    private static boolean pg$overlayHead = false;

    @Inject(method = "func_175183_b", at = @At("HEAD"), remap = false)
    private void pg$onShowCrosshair(CallbackInfoReturnable cir) {
        if (!pg$crosshair) {
            pg$crosshair = true;
            System.out.println("[PORT-GUIINGAME] *** showCrosshair HEAD fired ***");
        }
    }

    @Inject(method = "func_175180_a", at = @At("HEAD"), remap = false)
    private void pg$onRenderGameOverlayHead(float partialTicks, CallbackInfo ci) {
        if (!pg$overlayHead) {
            pg$overlayHead = true;
            System.out.println("[PORT-GUIINGAME] *** renderGameOverlay HEAD fired ***");
        }
    }
}