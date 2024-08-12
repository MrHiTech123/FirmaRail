package net.mrhitech.firmarail.common.creative;

import net.dries007.tfc.common.TFCCreativeTabs;
import net.dries007.tfc.util.Metal;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.mrhitech.firmarail.common.item.BoilerMetal;
import net.mrhitech.firmarail.common.item.ConductiveMetal;
import net.mrhitech.firmarail.common.item.FirmaRailItems;
import net.mrhitech.firmarail.common.item.QuarterBoilerMetal;

public class FirmaRailCreativeTabs {
    public static void AddCreative(BuildCreativeModeTabContentsEvent event) {
        if (event.getTabKey() == TFCCreativeTabs.METAL.tab().getKey()) {
            for (QuarterBoilerMetal metal : QuarterBoilerMetal.values()) {
                event.accept(FirmaRailItems.QUARTER_BOILERS.get(metal));
            }
            for (BoilerMetal metal : BoilerMetal.values()) {
                event.accept(FirmaRailItems.HALF_BOILERS.get(metal));
                event.accept(FirmaRailItems.BOILERS.get(metal));
            }
            event.accept(FirmaRailItems.MINECART_WHEEL);
            
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
            
            
        }
    }
}
