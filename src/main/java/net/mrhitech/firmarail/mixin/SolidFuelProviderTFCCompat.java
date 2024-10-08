/*
Code taken from 1.20.x branch of Railcraft Reborn, found here.

https://github.com/railcraft-reborn/railcraft/tree/1.20.x
*/

package net.mrhitech.firmarail.mixin;


import mods.railcraft.util.container.ContainerTools;
import mods.railcraft.world.level.material.FuelProvider;
import mods.railcraft.world.level.material.steam.SolidFuelProvider;
import mods.railcraft.world.entity.vehicle.locomotive.SteamLocomotive;
import net.dries007.tfc.util.Fuel;
import net.minecraft.world.Container;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import org.apache.commons.lang3.ObjectUtils;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Overwrite;
import org.spongepowered.asm.mixin.Shadow;

import java.lang.annotation.Target;

// remap = false
@Mixin(value = SolidFuelProvider.class, priority = 100000, remap = false)
public abstract class SolidFuelProviderTFCCompat implements FuelProvider {
    @Shadow
    private final Container container;
    @Shadow
    private final int slot;
    @Shadow
    private Item lastItem;
    
    
    private SolidFuelProviderTFCCompat(Container container, int slot) {
        this.container = container;
        this.slot = slot;
    }
    
    @Overwrite
    public float consumeFuel() {
        ItemStack fuelItem = container.getItem(this.slot);
        Fuel fuel = Fuel.get(fuelItem);
        int burn;
        if (fuel == null) {
            burn = 0;
        }
        else {
            burn = fuel.getDuration();
        }

        if (burn > 0) {
            this.lastItem = fuelItem.getItem();
            this.container.setItem(this.slot, ContainerTools.depleteItem(fuelItem));
        }

        return (float)burn;

    }
}
