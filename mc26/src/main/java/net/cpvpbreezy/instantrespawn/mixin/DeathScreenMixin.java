package net.cpvpbreezy.instantrespawn.mixin;

import net.minecraft.client.gui.screens.DeathScreen;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Vanilla disables the death screen buttons in init() and only enables them
 * once delayTicker reaches 20 (one second). This enables them right away.
 */
@Mixin(DeathScreen.class)
public abstract class DeathScreenMixin {
    @Shadow private int delayTicker;

    @Shadow protected abstract void setButtonsActive(boolean active);

    @Inject(method = "init", at = @At("TAIL"))
    private void instantrespawn$enableButtons(CallbackInfo ci) {
        // Skip past the vanilla one-second delay so tick() never toggles anything later.
        this.delayTicker = 20;
        this.setButtonsActive(true);
    }
}
