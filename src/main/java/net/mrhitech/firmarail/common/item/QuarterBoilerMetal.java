package net.mrhitech.firmarail.common.item;

import java.util.Locale;

public enum QuarterBoilerMetal {
    WROUGHT_IRON;
    
    private String id;
    
    QuarterBoilerMetal() {
        this.id = this.name().toLowerCase(Locale.ROOT);
    }
    
    public String getId() {
        return id;
    }
}
