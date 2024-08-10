package net.mrhitech.firmarail.util.mixininterface;

import mods.railcraft.world.entity.vehicle.locomotive.Locomotive;

public interface BaseSteamLocomotiveInterface {
    boolean isShutDown();
    void setSmoking(boolean smoke);
    void ventSteam();
    
    
}
