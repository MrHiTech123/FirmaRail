package net.mrhitech.firmarail.common.item;

import java.util.Locale;

public enum BoilerMetal {
    WROUGHT_IRON,
    STEEL;
    private String id;
    
    BoilerMetal() {
        this.id = this.name().toLowerCase(Locale.ROOT);
    }
    
    public String getId() {
        return id;
    }
    
}
