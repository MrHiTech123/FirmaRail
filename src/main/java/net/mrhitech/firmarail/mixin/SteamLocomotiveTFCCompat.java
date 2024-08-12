package net.mrhitech.firmarail.mixin;

import mods.railcraft.util.fluids.FluidTools;
import mods.railcraft.world.entity.vehicle.locomotive.BaseSteamLocomotive;
import mods.railcraft.world.entity.vehicle.locomotive.SteamLocomotive;
import mods.railcraft.world.item.TicketItem;
import net.dries007.tfc.util.Helpers;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.material.Fluids;
import net.mrhitech.firmarail.common.FirmaRailTags;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Overwrite;
import org.spongepowered.asm.mixin.Shadow;


@Mixin(value = SteamLocomotive.class, remap = false)
public abstract class SteamLocomotiveTFCCompat extends BaseSteamLocomotive {
    
    @Shadow
    private static final int FUEL_SLOT = 3;
    @Shadow
    private static final int EXTRA_FUEL_SLOT_A = 4;
    @Shadow
    private static final int EXTRA_FUEL_SLOT_B = 5;
    @Shadow
    private static final int EXTRA_FUEL_SLOT_C = 6;
    @Shadow
    private static final int TICKET_SLOT = 7;
    
    
    public SteamLocomotiveTFCCompat(EntityType<?> type, Level level) {
        super(type, level);
    }
    
    @Overwrite
    public boolean canPlaceItem(int slot, ItemStack stack) {
        return switch (slot) {
            case FUEL_SLOT, EXTRA_FUEL_SLOT_A, EXTRA_FUEL_SLOT_B, EXTRA_FUEL_SLOT_C ->
                    Helpers.isItem(stack, FirmaRailTags.Items.STEAM_LOCOMOTIVE_FUEL);
            case SLOT_WATER_INPUT ->
                // if (FluidItemHelper.getFluidStackInContainer(stack)
                // .filter(fluidStack -> fluidStack.getAmount() > FluidTools.BUCKET_VOLUME).isPresent()) {
                // return false;
                // } we allow tanks instafilling.
                    FluidTools.containsFluid(stack, Fluids.WATER);
            case TICKET_SLOT -> TicketItem.FILTER.test(stack);
            default -> false;
        };
    }
    
    
}
