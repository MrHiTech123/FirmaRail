package net.mrhitech.firmarail.mixin;

import mods.railcraft.api.carts.Linkable;
import mods.railcraft.api.carts.NeedsFuel;
import mods.railcraft.api.carts.Paintable;
import mods.railcraft.api.carts.Routable;
import mods.railcraft.api.core.Lockable;
import mods.railcraft.world.entity.vehicle.Directional;
import mods.railcraft.world.entity.vehicle.RailcraftMinecart;
import mods.railcraft.world.entity.vehicle.locomotive.Locomotive;
import net.dries007.tfc.util.Helpers;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import net.mrhitech.firmarail.common.FirmaRailTags;
import net.mrhitech.firmarail.common.item.FirmaRailItems;
import net.mrhitech.firmarail.util.mixininterface.LocomotiveInterface;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

import java.util.logging.Logger;

@Mixin(value = Locomotive.class, remap = false)
public abstract class LocomotiveTFCCompat extends RailcraftMinecart implements Linkable, Directional, Lockable, Paintable, Routable, NeedsFuel, LocomotiveInterface {
    @Shadow
    private int whistleDelay;
    @Shadow
    private float whistlePitch;
    
    protected LocomotiveTFCCompat(EntityType<?> type, Level level) {
        super(type, level);
    }
    
    @Inject(method = "interact", at = @At("HEAD"), cancellable = true)
    public void injectInteract(Player player, InteractionHand hand, CallbackInfoReturnable<InteractionResult> info) {
        if (this.level().isClientSide()) {
            return;
        }
        var itemStack = player.getItemInHand(hand);
        if (!itemStack.isEmpty() && Helpers.isItem(itemStack, FirmaRailTags.Items.WHISTLE_TUNERS)) {
            
            if (this.whistleDelay <= 0) {
                this.whistlePitch = this.getNewWhistlePitch();
                this.whistle();
                itemStack.hurtAndBreak(1, (ServerPlayer) player,
                        serverPlayerEntity -> player.broadcastBreakEvent(hand));
            }
            info.setReturnValue(InteractionResult.sidedSuccess(this.level().isClientSide()));
            info.cancel();
        }

    }
    
}
