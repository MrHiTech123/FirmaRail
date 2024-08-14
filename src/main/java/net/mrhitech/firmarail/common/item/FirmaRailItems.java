package net.mrhitech.firmarail.common.item;

import mods.railcraft.world.item.CrowbarItem;
import mods.railcraft.world.item.RailcraftItems;
import mods.railcraft.world.item.SpikeMaulItem;
import net.dries007.tfc.common.items.TFCItems;
import net.dries007.tfc.common.items.ToolItem;
import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.util.Metal;
import net.minecraft.world.item.Item;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.mrhitech.firmarail.FirmaRail;

import java.util.Map;

public class FirmaRailItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, FirmaRail.MOD_ID);
    
    public static final Map<QuarterBoilerMetal, RegistryObject<Item>> QUARTER_BOILERS = Helpers.mapOfKeys(QuarterBoilerMetal.class, metal ->
            ITEMS.register("metal/quarter_boiler/" + metal.getId(), () -> new Item(new Item.Properties())));
    public static final Map<BoilerMetal, RegistryObject<Item>> HALF_BOILERS = Helpers.mapOfKeys(BoilerMetal.class, metal ->
            ITEMS.register("metal/half_boiler/" + metal.getId(), () -> new Item(new Item.Properties())));
    public static final Map<BoilerMetal, RegistryObject<Item>> BOILERS = Helpers.mapOfKeys(BoilerMetal.class, metal ->
            ITEMS.register("metal/boiler/" + metal.getId(), () -> new Item(new Item.Properties())));
    
    public static final RegistryObject<Item> MINECART_WHEEL = ITEMS.register("metal/minecart_wheel", () -> new Item(new Item.Properties()));
    
    public static final Map<Metal.Default, RegistryObject<Item>> CROWBARS = Helpers.mapOfKeys(Metal.Default.class, Metal.Default::hasTools, metal -> 
            ITEMS.register("metal/crowbar/" + metal.getSerializedName(), () -> new CrowbarItem(ToolItem.calculateVanillaAttackDamage(0.75f, metal.toolTier()), -2.8f, metal.toolTier(), new Item.Properties())));
    
    public static final Map<Metal.Default, RegistryObject<Item>> SPIKE_MAULS = Helpers.mapOfKeys(Metal.Default.class, Metal.Default::hasTools, metal -> 
            ITEMS.register("metal/spike_maul/" + metal.getSerializedName(), () -> new SpikeMaulItem(ToolItem.calculateVanillaAttackDamage(1.0F, metal.toolTier()), -3.0F, metal.toolTier(), new Item.Properties())));
    
    public static final Map<Metal.Default, RegistryObject<Item>> SPIKE_MAUL_HEADS = Helpers.mapOfKeys(Metal.Default.class, Metal.Default::hasTools, metal ->
            ITEMS.register("metal/spike_maul_head/" + metal.getSerializedName(), () -> new Item(new Item.Properties())));
    
    public static final Map<Metal.Default, RegistryObject<Item>> WHISTLE_TUNERS = Helpers.mapOfKeys(Metal.Default.class, Metal.Default::hasTools, metal -> 
            ITEMS.register("metal/whistle_tuner/" + metal.getSerializedName(), () -> new Item(new Item.Properties().durability(metal.toolTier().getUses()))));
    
    public static final Map<Metal.Default, RegistryObject<Item>> METAL_COILS = Helpers.mapOfKeys(Metal.Default.class, Metal.Default::hasParts, metal -> 
            ITEMS.register("metal/coil/" + metal.getSerializedName(), () -> new Item(new Item.Properties())));
    
    public static final RegistryObject<Item> LEATHER_STRAP = ITEMS.register("leather_strap", () -> new Item(new Item.Properties()));
    
    public static void register(IEventBus bus) {
        ITEMS.register(bus);
        
        
    }
    
}
