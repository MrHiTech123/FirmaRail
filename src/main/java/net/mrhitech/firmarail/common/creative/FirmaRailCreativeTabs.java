package net.mrhitech.firmarail.common.creative;

import net.dries007.tfc.common.TFCCreativeTabs;
import net.dries007.tfc.util.Metal;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;
import net.mrhitech.firmarail.FirmaRail;
import net.mrhitech.firmarail.common.item.BoilerMetal;
import net.mrhitech.firmarail.common.item.FirmaRailItems;
import net.mrhitech.firmarail.common.item.QuarterBoilerMetal;

import java.util.function.Supplier;

public class FirmaRailCreativeTabs {
    public static final DeferredRegister<CreativeModeTab> CREATIVE_TABS = DeferredRegister.create(Registries.CREATIVE_MODE_TAB, FirmaRail.MOD_ID);
    public static final RegistryObject<CreativeModeTab> FIRMARAIL = register("firmarail", 
            () -> new ItemStack(FirmaRailItems.CROWBARS.get(Metal.Default.BISMUTH_BRONZE).get()));
    
    private static RegistryObject<CreativeModeTab> register(String name, Supplier<ItemStack> icon) {
        return CREATIVE_TABS.register(name, () -> {
            return CreativeModeTab.builder().icon(icon).title(Component.translatable(FirmaRail.MOD_ID + ".creative_tab." + name)).build();
        });
        
    }
            
    public static void AddCreative(BuildCreativeModeTabContentsEvent event) {
        if (event.getTabKey() == FIRMARAIL.getKey()) {
            event.accept(FirmaRailItems.MINECART_WHEEL);
            event.accept(FirmaRailItems.LEATHER_STRAP);
            
            for (Metal.Default metal : Metal.Default.values()) {
                if (metal.hasTools()) {
                    event.accept(FirmaRailItems.CROWBARS.get(metal));
                    event.accept(FirmaRailItems.SPIKE_MAULS.get(metal));
                    event.accept(FirmaRailItems.SPIKE_MAUL_HEADS.get(metal));
                    event.accept(FirmaRailItems.WHISTLE_TUNERS.get(metal));
                }
                if (metal.hasParts()) {
                    event.accept(FirmaRailItems.METAL_COILS.get(metal));
                }
            }
            
            for (QuarterBoilerMetal metal : QuarterBoilerMetal.values()) {
                event.accept(FirmaRailItems.QUARTER_BOILERS.get(metal));
            }
            for (BoilerMetal metal : BoilerMetal.values()) {
                event.accept(FirmaRailItems.HALF_BOILERS.get(metal));
                event.accept(FirmaRailItems.BOILERS.get(metal));
            }
            
            
        }
    }
    
    public static void register(IEventBus bus)
    {
        CREATIVE_TABS.register(bus);
        
    }
}
