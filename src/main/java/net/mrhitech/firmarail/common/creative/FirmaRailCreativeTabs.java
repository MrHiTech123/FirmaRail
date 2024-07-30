package net.mrhitech.firmarail.common.creative;

import net.dries007.tfc.common.TFCCreativeTabs;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.mrhitech.firmarail.common.item.BoilerMetal;
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
        }
    }
}
