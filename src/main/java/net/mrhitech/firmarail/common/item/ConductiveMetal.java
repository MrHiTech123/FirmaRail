package net.mrhitech.firmarail.common.item;

import java.util.Locale;

public enum ConductiveMetal {
    BLACK_BRONZE,
    BLACK_STEEL,
    BRASS,
    BRONZE,
    COPPER,
    GOLD,
    NICKEL,
    RED_STEEL,
    ROSE_GOLD,
    SILVER,
    STERLING_SILVER,
    ZINC;
    private String id;
    
    ConductiveMetal() {
        this.id = this.name().toLowerCase(Locale.ROOT);
    }
    
    public String getId() {
        return id;
    }
}
