package net.mrhitech.firmarail.mixin;

import mods.railcraft.api.carts.FluidTransferHandler;
import mods.railcraft.world.entity.vehicle.locomotive.BaseSteamLocomotive;
import mods.railcraft.world.entity.vehicle.locomotive.Locomotive;
import mods.railcraft.world.level.material.StandardTank;
import mods.railcraft.world.level.material.steam.SteamBoiler;
import mods.railcraft.world.level.material.steam.SteamConstants;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.material.Fluids;
import net.minecraftforge.fluids.FluidStack;
import net.minecraftforge.fluids.capability.IFluidHandler;
import net.mrhitech.firmarail.util.mixininterface.BaseSteamLocomotiveInterface;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@SuppressWarnings("all")
@Mixin(value = BaseSteamLocomotive.class, remap = false)
public abstract class BaseSteamLocomotiveTFCCompat extends Locomotive implements FluidTransferHandler, BaseSteamLocomotiveInterface {
    @Shadow
    private StandardTank steamTank;
    @Shadow
    private SteamBoiler boiler;
    boolean shutDown;
    int shutdownOldWater;
    
    
    public BaseSteamLocomotiveTFCCompat(EntityType<?> type, Level level) {
        super(type, level);
    }
    
    @Inject(method = "tick", at = @At("HEAD"))
    public void injectTick(CallbackInfo info) {
        shutDown = this.isShutDown();
        if (!(this.steamTank.getRemainingSpace() >= SteamConstants.STEAM_PER_UNIT_WATER
                || shutDown)) {
            
            int oldWater = this.boiler.getWaterTank().getFluidAmount();
            this.boiler.tick(1);
            int toFill = oldWater - this.boiler.getWaterTank().getFluidAmount();
            FluidStack waterStack = new FluidStack(Fluids.WATER, toFill);
            this.boiler.getWaterTank().fill(waterStack, IFluidHandler.FluidAction.EXECUTE);
            
            
            this.setSmoking(this.boiler.isBurning());
            
            if (!this.boiler.isBurning()) {
                this.ventSteam();
            }
        }
    }
    
    
    
}
