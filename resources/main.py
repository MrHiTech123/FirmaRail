from alcs_n_russians_funcs import *

BOILER_METAL_COEFFICIENTS = {'wrought_iron': 2, 'steel': 1}
CONDUCTIVE_METALS = ['black_bronze', 'black_steel', 'brass', 'bronze', 'copper', 'gold', 'nickel', 'red_steel', 'rose_gold', 'silver', 'sterling_silver', 'zinc']
ALL_TRACK_KITS = ['transition', 'locking', 'buffer_stop', 'activator', 'booster', 'control', 'gated', 'detector', 'coupler', 'embarking', 'disembarking', 'dumping', 'launcher', 'one_way', 'whistle', 'locomotive', 'throttle', 'routing']


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
    for metal, metal_data in METALS.items():
        if 'tool' in metal_data.types:
            item_heat(rm, ('metal', 'crowbar', metal), f'firmarail:metal/crowbar/{metal}', metal_data.ingot_heat_capacity(), metal_data.melt_temperature, 50)
            item_heat(rm, ('metal', 'spike_maul', metal), f'firmarail:metal/spike_maul/{metal}', metal_data.ingot_heat_capacity(), metal_data.melt_temperature, 100)
            item_heat(rm, ('metal', 'spike_maul_head', metal), f'firmarail:metal/spike_maul_head/{metal}', metal_data.ingot_heat_capacity(), metal_data.melt_temperature, 100)
            item_heat(rm, ('metal', 'whistle_tuner', metal), f'firmarail:metal/whistle_tuner/{metal}', metal_data.ingot_heat_capacity(), metal_data.melt_temperature, 50)
        if 'part' in metal_data.types:
            item_heat(rm, ('metal', 'coil', metal), f'firmarail:metal/coil/{metal}', metal_data.ingot_heat_capacity(), metal_data.melt_temperature, 50)
def generate_size_data():
    print('\tGenerating size data...')
    item_size(rm, ('metal', 'quarter_boilers'), '#firmarail:quarter_boilers', Size.large, Weight.medium)
    item_size(rm, ('metal', 'half_boilers'), '#firmarail:half_boilers', Size.very_large, Weight.heavy)
    item_size(rm, ('metal', 'boilers'), '#firmarail:boilers', Size.huge, Weight.very_heavy)
    item_size(rm, ('metal', 'steam_locomotive'), 'railcraft:steam_locomotive', Size.huge, Weight.very_heavy)
    item_size(rm, ('metal', 'whistle_tuners'), '#firmarail:whistle_tuners', Size.large, Weight.medium)
    
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
    
    for metal, metal_data in METALS.items():
        if 'tool' in metal_data.types:
            rm.item_model(('metal', 'crowbar', metal), f'firmarail:item/metal/crowbar/{metal}', parent='minecraft:item/handheld').with_lang(lang(f'{metal} railworker\'s crowbar'))
            rm.item_model(('metal', 'spike_maul', metal), f'firmarail:item/metal/spike_maul/{metal}', parent='minecraft:item/handheld').with_lang(lang(f'{metal}_spike_maul'))
            rm.item_model(('metal', 'spike_maul_head', metal), f'firmarail:item/metal/spike_maul_head/{metal}').with_lang(lang(f'{metal}_spike_maul_head'))
            rm.item_model(('metal', 'whistle_tuner', metal), f'firmarail:item/metal/whistle_tuner/{metal}').with_lang(lang(f'{metal}_whistle_tuner'))
            
        if 'part' in metal_data.types:
            rm.item_model(('metal', 'coil', metal), f'firmarail:item/metal/coil/{metal}').with_lang(lang(f'{metal}_coil'))
    
def generate_models():
    print('Generating models...')
    generate_item_models()
    
def generate_anvil_recipes():
    print('\tGenerating anvil recipes...')
    anvil_recipe(rm, ('metal', 'minecart_wheel_iron'), 'tfc:metal/ingot/wrought_iron', 'firmarail:metal/minecart_wheel', METALS['wrought_iron'].tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    anvil_recipe(rm, ('metal', 'minecart_wheel_steel'), 'tfc:metal/ingot/steel', (2, 'firmarail:metal/minecart_wheel'), METALS['steel'].tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    anvil_recipe(rm, ('metal', 'quarter_boiler', 'wrought_iron'), 'tfc:metal/double_sheet/wrought_iron', 'firmarail:metal/quarter_boiler/wrought_iron', METALS['wrought_iron'].tier, Rules.bend_third_last, Rules.bend_second_last, Rules.bend_last)
    anvil_recipe(rm, ('metal', 'half_boiler', 'steel'), 'tfc:metal/double_sheet/steel', 'firmarail:metal/half_boiler/steel', METALS['steel'].tier, Rules.bend_third_last, Rules.bend_second_last, Rules.bend_last)
    anvil_recipe(rm, ('metal', 'standard_rail_from_iron'), 'tfc:metal/rod/wrought_iron', 'railcraft:standard_rail', METALS['wrought_iron'].tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    anvil_recipe(rm, ('metal', 'standard_rail_from_steel'), 'tfc:metal/rod/steel', (2, 'railcraft:standard_rail'), METALS['steel'].tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    anvil_recipe(rm, ('metal', 'reinforced_rail'), 'tfc:metal/rod/black_steel', (2, 'railcraft:reinforced_rail'), METALS['black_steel'].tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    
    welding_recipe(rm, ('metal', 'half_boiler', 'wrought_iron'), 'firmarail:metal/quarter_boiler/wrought_iron', 'firmarail:metal/quarter_boiler/wrought_iron', 'firmarail:metal/half_boiler/wrought_iron', METALS['wrought_iron'].tier - 1)
    for metal in BOILER_METAL_COEFFICIENTS:
        welding_recipe(rm, ('metal', 'boiler', metal), f'firmarail:metal/half_boiler/{metal}', f'firmarail:metal/half_boiler/{metal}', f'firmarail:metal/boiler/{metal}', METALS[metal].tier - 1)
    
    for metal, metal_data in METALS.items():
        if 'tool' in metal_data.types:
            anvil_recipe(rm, ('metal', 'crowbar', metal), f'tfc:metal/rod/{metal}', f'firmarail:metal/crowbar/{metal}', metal_data.tier, Rules.punch_third_last, Rules.punch_second_last, Rules.punch_last, bonus=True)
            anvil_recipe(rm, ('metal', 'whistle_tuner', metal), f'tfc:metal/rod/{metal}', f'firmarail:metal/whistle_tuner/{metal}', metal_data.tier, Rules.punch_third_last, Rules.upset_second_last, Rules.draw_last, bonus=True)
            anvil_recipe(rm, ('metal', 'spike_maul_head', metal), f'tfc:metal/hammer_head/{metal}', f'firmarail:metal/spike_maul_head/{metal}', metal_data.tier, Rules.upset_not_last, Rules.upset_last, bonus=True)
        if 'part' in metal_data.types:
            anvil_recipe(rm, ('metal', 'coil', metal), f'tfc:metal/rod/{metal}', f'firmarail:metal/coil/{metal}', metal_data.tier, Rules.hit_third_last, Rules.hit_second_last, Rules.hit_last)
    
    

def generate_crafting_recipes():
    print('\tGenerating crafting recipes...')
    
    
    
    rm.crafting_shaped(('crafting', 'metal', 'minecart'), ['S S', 'SSS', 'WRW'], {'S': 'tfc:metal/sheet/wrought_iron', 'W': 'firmarail:metal/minecart_wheel', 'R': '#firmarail:rods/metal'}, 'minecraft:minecart')
    rm.crafting_shaped(('crafting', 'metal', 'steel_minecart'), ['S S', 'SSS', 'WRW'], {'S': 'tfc:metal/sheet/steel', 'W': 'firmarail:metal/minecart_wheel', 'R': '#firmarail:rods/metal'}, (2, 'minecraft:minecart'))
    rm.crafting_shaped(('crafting', 'metal', 'steam_locomotive'), ['t  ', 'MB ', 'WRW'], {'t': '#tfc:tuyeres', 'M': 'tfc:brass_mechanisms', 'B': '#firmarail:boilers', 'W': 'firmarail:metal/minecart_wheel', 'R': '#firmarail:rods/metal'}, 'railcraft:steam_locomotive')
    
    
    rm.crafting_shapeless(('crafting', 'track_kit', 'locking'), ('#minecraft:wooden_pressure_plates', 'minecraft:redstone_torch', '#firmarail:conductive_metal_coils', '#tfc:magnetic_rocks'), 'railcraft:locking_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'buffer_stop'), ('#minecraft:wooden_pressure_plates', '#firmarail:rods/metal', '#firmarail:rods/metal', '#firmarail:rods/metal'), 'railcraft:buffer_stop_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'activator'), ('#minecraft:wooden_pressure_plates', 'minecraft:redstone_torch'), 'railcraft:activator_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'gated'), ('#minecraft:wooden_pressure_plates', '#forge:fence_gates'), 'railcraft:gated_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'detector'), ('#minecraft:wooden_pressure_plates', '#firmarail:metal_coils', '#minecraft:wooden_pressure_plates', 'minecraft:redstone'), 'railcraft:detector_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'coupler'), ('#minecraft:wooden_pressure_plates', '#firmarail:chains', 'tfc:brass_mechanisms'), 'railcraft:coupler_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'dumping'), ('#minecraft:wooden_pressure_plates', 'minecraft:hopper'), 'railcraft:dumping_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'disembarking'), ('#minecraft:wooden_pressure_plates', 'minecraft:redstone', '#firmarail:conductive_metal_coils'), 'railcraft:disembarking_track_kit')
    rm.crafting_shapeless(('crafting', 'track_kit', 'whistle'), ('#minecraft:wooden_pressure_plates', '#firmarail:rods/metal'), 'railcraft:whistle_track_kit')
    for metal, metal_data in METALS.items():
        advanced_shaped(rm, ('crafting', 'metal', 'spike_maul', metal), ('H', 'R'), {'H': f'firmarail:metal/spike_maul_head/{metal}', 'R': '#forge:rods/wooden'}, item_stack_provider(f'firmarail:metal/spike_maul/{metal}', copy_forging=True), (0, 0))
    
    rm.crafting_shaped(('crafting', 'wooden_tie'), ('LLL',), {'L': '#tfc:lumber'}, (6, 'railcraft:wooden_tie'))
    rm.crafting_shaped(('crafting', 'wooden_tie_from_treated_lumber'), ('LLL',), {'L': 'firmalife:treated_lumber'}, (12, 'railcraft:wooden_tie'))
    rm.crafting_shaped(('crafting', 'stone_tie'), (' W ', 'AAA'), {'W': fluid_item_ingredient('1000 minecraft:water'), 'A': 'tfc:aggregate'}, (32, 'railcraft:stone_tie'))
    rm.crafting_shaped(('crafting', 'wooden_rail'), (' T ', 'TRT', ' T '), {'T': 'railcraft:wooden_tie', 'R': 'railcraft:standard_rail'}, (3, 'railcraft:wooden_rail'))
    
    
    
    
    
    
    
    
    
    
def generate_heat_recipes():
    print('\tGenerating heat recipes...')
    heat_recipe(rm, ('metal', 'quarter_boiler', 'wrought_iron'), 'firmarail:metal/quarter_boiler/wrought_iron', METALS['wrought_iron'].melt_temperature, result_fluid='400 tfc:metal/wrought_iron')
    
    for metal, coefficient in BOILER_METAL_COEFFICIENTS.items():
        heat_recipe(rm, ('metal', 'half_boiler', metal), f'firmarail:metal/half_boiler/{metal}', METALS[metal].melt_temperature, result_fluid=f'{400 * coefficient} {melt_metal(metal)}')
        heat_recipe(rm, ('metal', 'boiler', metal), f'firmarail:metal/boiler/{metal}', METALS[metal].melt_temperature, result_fluid=f'{800 * coefficient} {melt_metal(metal)}')
    for metal, metal_data in METALS.items():
        if 'tool' in metal_data.types:
            heat_recipe(rm, ('metal', 'crowbar', metal), f'firmarail:metal/crowbar/{metal}', metal_data.melt_temperature, result_fluid=f'50 {melt_metal(metal)}', use_durability=True)
            heat_recipe(rm, ('metal', 'spike_maul', metal), f'firmarail:metal/spike_maul/{metal}', metal_data.melt_temperature, result_fluid=f'100 {melt_metal(metal)}', use_durability=True)
            heat_recipe(rm, ('metal', 'spike_maul_head', metal), f'firmarail:metal/spike_maul_head/{metal}', metal_data.melt_temperature, result_fluid=f'100 {melt_metal(metal)}')
            heat_recipe(rm, ('metal', 'whistle_tuner', metal), f'firmarail:metal/whistle_tuner/{metal}', metal_data.melt_temperature, result_fluid=f'50 {melt_metal(metal)}', use_durability=True)
        if 'part' in metal_data.types:
            heat_recipe(rm, ('metal', 'coil', metal), f'firmarail:metal/coil/{metal}', metal_data.melt_temperature, result_fluid=f'50 {melt_metal(metal)}')
            
            
def disable_recipes():
    print('\tDisabling recipes...')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/minecart')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/steel_minecart')
    disable_recipe(rm, 'railcraft:steam_locomotive')
    disable_recipe(rm, 'railcraft:iron_crowbar')
    disable_recipe(rm, 'railcraft:steel_crowbar')
    disable_recipe(rm, 'railcraft:diamond_crowbar')
    disable_recipe(rm, 'railcraft:iron_spike_maul')
    disable_recipe(rm, 'railcraft:steel_spike_maul')
    disable_recipe(rm, 'railcraft:diamond_spike_maul')
    disable_recipe(rm, 'railcraft:whistle_tuner')
    disable_recipe(rm, 'railcraft:steel_sword')
    disable_recipe(rm, 'railcraft:steel_axe')
    disable_recipe(rm, 'railcraft:steel_pickaxe')
    disable_recipe(rm, 'railcraft:steel_shovel')
    disable_recipe(rm, 'railcraft:steel_hoe')
    disable_recipe(rm, 'railcraft:steel_helmet')
    disable_recipe(rm, 'railcraft:steel_chestplate')
    disable_recipe(rm, 'railcraft:steel_leggings')
    disable_recipe(rm, 'railcraft:steel_boots')
    disable_recipe(rm, 'railcraft:coke_oven_bricks')
    disable_recipe(rm, 'railcraft:charge_meter')
    disable_recipe(rm, 'railcraft:steel_anvil')
    disable_recipe(rm, 'railcraft:brass_ingot_crafted_with_ingots')
    disable_recipe(rm, 'railcraft:bronze_ingot_crafted_with_ingots')
    disable_recipe(rm, 'railcraft:invar_ingot_crafted_with_ingots')
    disable_recipe(rm, 'railcraft:bushing_gear_brass')
    disable_recipe(rm, 'railcraft:bushing_gear_bronze')
    disable_recipe(rm, 'railcraft:sheep_detector')
    disable_recipe(rm, 'railcraft:tank_detector')
    disable_recipe(rm, 'railcraft:villager_detector')
    disable_recipe(rm, 'railcraft:signal_block_surveyor')
    disable_recipe(rm, 'railcraft:overalls')
    disable_recipe(rm, 'railcraft:track_parts_steel_nugget')
    disable_recipe(rm, 'railcraft:track_parts_bronze_nugget')
    disable_recipe(rm, 'railcraft:track_parts_iron_nugget')
    disable_recipe(rm, 'railcraft:standard_rail_from_rail')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/rail')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/steel_rail')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/powered_rail')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/detector_rail')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/steel_detector_rail')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/activator_rail')
    disable_recipe(rm, 'tfc:crafting/vanilla/redstone/steel_activator_rail')
    disable_recipe(rm, 'minecraft:powered_rail')
    disable_recipe(rm, 'minecraft:detector_rail')
    disable_recipe(rm, 'minecraft:activator_rail')
    
    for kit in ALL_TRACK_KITS:
        disable_recipe(rm, f'railcraft:{kit}_track_kit')

def generate_recipes():
    print('Generating recipes...')
    generate_anvil_recipes()
    generate_crafting_recipes()
    generate_heat_recipes()
    
    disable_recipes()
    
def generate_item_tags():
    print('\tGenerating item tags...')
    rm.item_tag('rods/metal', *[f'tfc:metal/rod/{metal}' for metal, metal_data in METALS.items() if 'utility' in metal_data.types])
    rm.item_tag('chains', *[f'tfc:metal/chain/{metal}' for metal, metal_data in METALS.items() if 'utility' in metal_data.types])
    rm.item_tag('quarter_boilers', 'firmarail:metal/quarter_boiler/wrought_iron')
    rm.item_tag('half_boilers', *[f'firmarail:metal/half_boiler/{metal}' for metal in BOILER_METAL_COEFFICIENTS])
    rm.item_tag('boilers', *[f'firmarail:metal/boiler/{metal}' for metal in BOILER_METAL_COEFFICIENTS])
    rm.item_tag('metal_coils', *[f'firmarail:metal/coil/{metal}' for metal, metal_data in METALS.items() if 'part' in metal_data.types])
    rm.item_tag('conductive_metal_coils', *[f'firmarail:metal/coil/{metal}' for metal in CONDUCTIVE_METALS])
    rm.item_tag('tool_metal_coils', *[f'firmarail:metal/coil/{metal}' for metal, metal_data in METALS.items() if 'tool' in metal_data.types])
    rm.item_tag('steam_locomotive_fuel', '#minecraft:coals')
    rm.item_tag('whistle_tuners', *[f'firmarail:metal/whistle_tuner/{metal}' for metal, metal_data in METALS.items() if 'tool' in metal_data.types])
    
    

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