from alcs_n_russians_funcs import *

BOILER_METAL_COEFFICIENTS = {'wrought_iron': 2, 'steel': 1}

rm = ResourceManager('firmarail')

def melt_metal(name: str):
    metal = METALS[name]
    if metal.melt_metal is not None:
        name = metal.melt_metal
    return f'tfc:metal/{name}'

def generate_heat_data():
    print('\tGenerating heat data...')
    item_heat(rm, ('metal', 'quarter_boiler', 'wrought_iron'), 'firmarail:metal/quarter_boiler/wrought_iron', METALS['wrought_iron'].ingot_heat_capacity() * 4, METALS['wrought_iron'].melt_temperature, 400)    
    for metal, coefficient in BOILER_METAL_COEFFICIENTS.items():
        item_heat(rm, ('metal', 'half_boiler', metal), f'firmarail:metal/half_boiler/{metal}', METALS[metal].ingot_heat_capacity(), METALS[metal].melt_temperature, 400 * coefficient)
        item_heat(rm, ('metal', 'boiler', metal), f'firmarail:metal/boiler/{metal}', METALS[metal].ingot_heat_capacity(), METALS[metal].melt_temperature, 800 * coefficient)

def generate_size_data():
    print('\tGenerating size data...')
    item_size(rm, ('metal', 'quarter_boilers'), '#firmarail:quarter_boilers', Size.large, Weight.medium)
    item_size(rm, ('metal', 'half_boilers'), '#firmarail:half_boilers', Size.very_large, Weight.heavy)
    item_size(rm, ('metal', 'boilers'), '#firmarail:boilers', Size.huge, Weight.very_heavy)
    
    
def generate_data():
    print('Generating data...')
    generate_heat_data()
    generate_size_data()

def generate_item_models():
    print('\tGenerating item models...')
    rm.item_model(('metal', 'minecart_wheel'), 'firmarail:item/metal/minecart_wheel').with_lang(lang('minecart_wheel'))
    rm.item_model(('metal', 'quarter_boiler', 'wrought_iron'), 'firmarail:item/metal/quarter_boiler/wrought_iron').with_lang(lang('wrought_iron_quarter_boiler'))
    for metal in BOILER_METAL_COEFFICIENTS:
        rm.item_model(('metal', 'half_boiler', metal), f'firmarail:item/metal/half_boiler/{metal}').with_lang(lang(metal + '_half_boiler'))
        rm.item_model(('metal', 'boiler', metal), f'firmarail:item/metal/boiler/{metal}').with_lang(lang(metal + '_boiler'))
    
def generate_models():
    print('Generating models...')
    generate_item_models()
    
def generate_anvil_recipes():
    print('\tGenerating anvil recipes...')
    anvil_recipe(rm, ('metal', 'minecart_wheel_iron'), 'tfc:metal/ingot/wrought_iron', 'firmarail:metal/minecart_wheel', METALS['wrought_iron'].tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    anvil_recipe(rm, ('metal', 'minecart_wheel_steel'), 'tfc:metal/ingot/steel', (2, 'firmarail:metal/minecart_wheel'), METALS['steel'].tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    anvil_recipe(rm, ('metal', 'quarter_boiler', 'wrought_iron'), 'tfc:metal/double_sheet/wrought_iron', 'firmarail:metal/quarter_boiler/wrought_iron', METALS['wrought_iron'].tier, Rules.bend_third_last, Rules.bend_second_last, Rules.bend_last)
    anvil_recipe(rm, ('metal', 'half_boiler', 'steel'), 'tfc:metal/double_sheet/steel', 'firmarail:metal/half_boiler/steel', METALS['steel'].tier, Rules.bend_third_last, Rules.bend_second_last, Rules.bend_last)
    
    
    welding_recipe(rm, ('metal', 'half_boiler', 'wrought_iron'), 'firmarail:metal/quarter_boiler/wrought_iron', 'firmarail:metal/quarter_boiler/wrought_iron', 'firmarail:metal/half_boiler/wrought_iron', METALS['wrought_iron'].tier - 1)
    for metal in BOILER_METAL_COEFFICIENTS:
        welding_recipe(rm, ('metal', 'boiler', metal), f'firmarail:metal/half_boiler/{metal}', f'firmarail:metal/half_boiler/{metal}', f'firmarail:metal/boiler/{metal}', METALS[metal].tier - 1)

def generate_crafting_recipes():
    print('\tGenerating crafting recipes...')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/minecart')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/steel_minecart')
    
    
    rm.crafting_shaped(('crafting', 'metal', 'minecart'), ['S S', 'SSS', 'WRW'], {'S': 'tfc:metal/sheet/wrought_iron', 'W': 'firmarail:metal/minecart_wheel', 'R': '#firmarail:rods/metal'}, 'minecraft:minecart')
    rm.crafting_shaped(('crafting', 'metal', 'steel_minecart'), ['S S', 'SSS', 'WRW'], {'S': 'tfc:metal/sheet/steel', 'W': 'firmarail:metal/minecart_wheel', 'R': '#firmarail:rods/metal'}, (2, 'minecraft:minecart'))
    
    rm.crafting_shaped(('crafting', 'metal', 'steam_locomotive'), ['t  ', 'MB ', 'WRW'], {'t': '#tfc:tuyeres', 'M': 'tfc:brass_mechanisms', 'B': '#firmarail:boilers', 'W': 'firmarail:metal/minecart_wheel', 'R': '#firmarail:rods/metal'}, 'railcraft:steam_locomotive')
    disable_recipe(rm, 'railcraft:steam_locomotive')

def generate_heat_recipes():
    print('\tGenerating heat recipes...')
    heat_recipe(rm, ('metal', 'quarter_boiler', 'wrought_iron'), 'firmarail:metal/quarter_boiler/wrought_iron', METALS['wrought_iron'].melt_temperature, result_fluid='400 tfc:metal/wrought_iron')
    
    for metal, coefficient in BOILER_METAL_COEFFICIENTS.items():
        heat_recipe(rm, ('metal', 'half_boiler', metal), f'firmarail:metal/half_boiler/{metal}', METALS[metal].melt_temperature, result_fluid=f'{400 * coefficient} {melt_metal(metal)}')
        heat_recipe(rm, ('metal', 'boiler', metal), f'firmarail:metal/boiler/{metal}', METALS[metal].melt_temperature, result_fluid=f'{800 * coefficient} {melt_metal(metal)}')


def generate_recipes():
    print('Generating recipes...')
    generate_anvil_recipes()
    generate_crafting_recipes()
    generate_heat_recipes()
    
def generate_item_tags():
    print('\tGenerating item tags...')
    rm.item_tag('rods/metal', *[f'tfc:metal/rod/{metal}' for metal in METALS if 'utility' in METALS[metal].types])
    rm.item_tag('quarter_boilers', 'firmarail:metal/quarter_boiler/wrought_iron')
    rm.item_tag('half_boilers', *[f'firmarail:metal/half_boiler/{metal}' for metal in BOILER_METAL_COEFFICIENTS])
    rm.item_tag('boilers', *[f'firmarail:metal/boiler/{metal}' for metal in BOILER_METAL_COEFFICIENTS])
    


def generate_tags():
    print('Generating tags...')
    generate_item_tags()

def generate_all():
    generate_data()
    generate_models()
    generate_recipes()
    generate_tags()
    
    
    rm.flush()




generate_all()