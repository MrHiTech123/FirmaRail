package net.mrhitech.modname.common.item;

import net.minecraft.world.item.Item;
import net.minecraft.world.item.Items;
import net.minecraftforge.event.furnace.FurnaceFuelBurnTimeEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.mrhitech.modname.TerraFirmaRails;

public class TerraFirmaRailsItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, TerraFirmaRails.MOD_ID);
    
    
    
    
    
    public static void register(IEventBus bus) {
        ITEMS.register(bus);
    }
    
}
