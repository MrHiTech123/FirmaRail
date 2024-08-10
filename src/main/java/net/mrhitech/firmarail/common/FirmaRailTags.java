package net.mrhitech.firmarail.common;

import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.tags.TagKey;
import net.minecraft.world.item.Item;
import net.mrhitech.firmarail.FirmaRail;

public class FirmaRailTags {
    public static class Items {
        public static TagKey<Item> STEAM_LOCOMOTIVE_FUEL = TagKey.create(Registries.ITEM, new ResourceLocation(FirmaRail.MOD_ID, "steam_locomotive_fuel"));
    }
}
