package net.mrhitech.firmarail.mixin;

import mods.railcraft.world.level.material.steam.SteamBoiler;
import net.minecraft.nbt.CompoundTag;
import net.minecraftforge.common.util.INBTSerializable;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Overwrite;
import org.spongepowered.asm.mixin.Shadow;

@Mixin(value = SteamBoiler.class, remap = false)
@SuppressWarnings("all")
public abstract class SteamBoilerTFCCompat implements INBTSerializable<CompoundTag> {
    
    @Shadow
    private int ticksPerCycle;
    
    @Overwrite
    public float getFuelPerCycle(int numTanks) {
        return this.ticksPerCycle;
    }
}
