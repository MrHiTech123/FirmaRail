package net.mrhitech.firmarail.mixin;

import mods.railcraft.api.carts.FluidTransferHandler;
import mods.railcraft.world.entity.vehicle.locomotive.BaseSteamLocomotive;
import mods.railcraft.world.entity.vehicle.locomotive.Locomotive;
import mods.railcraft.world.level.material.StandardTank;
import mods.railcraft.world.level.material.steam.SteamBoiler;
import mods.railcraft.world.level.material.steam.SteamConstants;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.level.Level;
import net.mrhitech.firmarail.util.mixininterface.BaseSteamLocomotiveInterface;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

import java.time.Clock;

@SuppressWarnings("")
@Mixin(value = BaseSteamLocomotive.class, remap = false)
public abstract class BaseSteamLocomotiveTFCCompat extends Locomotive implements FluidTransferHandler, BaseSteamLocomotiveInterface {
    @Shadow
    private StandardTank steamTank;
    private SteamBoiler boiler;
    
    
    public BaseSteamLocomotiveTFCCompat(EntityType<?> type, Level level) {
        super(type, level);
    }
    
    @Inject(method = "tick", at = @At("HEAD"))
    public void injectTick(CallbackInfo info) {
        if (!(this.steamTank.getRemainingSpace() >= SteamConstants.STEAM_PER_UNIT_WATER
                || this.isShutdown())) {
            this.boiler.tick(1);
            
            this.setSmoking(this.boiler.isBurning());
            
            // TODO: make venting a toggleable thing (why autodump while train has no coal??)
            if (!this.boiler.isBurning()) {
                this.ventSteam();
            }
        }
    }
    
    
    
}
