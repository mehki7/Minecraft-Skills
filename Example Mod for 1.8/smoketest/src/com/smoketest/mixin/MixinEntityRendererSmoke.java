package com.smoketest.mixin;

import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

// tsrg evidence: updateLightmap (F)V func_78472_g
// inject PASS confirmed 2026-10-29 on profile 1.8-furiahvisuals
@Mixin(targets = "net.minecraft.client.renderer.EntityRenderer", remap = false)
public abstract class MixinEntityRendererSmoke {

    private static boolean st$fired = false;

    @Inject(method = "func_78472_g", at = @At("HEAD"), remap = false)
    private void st$lightmapInject(float partialTicks, CallbackInfo ci) {
        if (!st$fired) {
            st$fired = true;
            System.out.println("[SMOKETEST] *** INJECT PASS -- updateLightmap HEAD fired in net.minecraft.client.renderer.EntityRenderer ***");
        }
    }
}