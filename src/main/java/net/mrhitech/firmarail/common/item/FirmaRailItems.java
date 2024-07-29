package net.mrhitech.firmarail.common.item;

import net.minecraft.world.item.Item;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.mrhitech.firmarail.FirmaRail;

public class FirmaRailItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, FirmaRail.MOD_ID);
    
    
    
    
    public static void register(IEventBus bus) {
        ITEMS.register(bus);
        
    }
    
}
