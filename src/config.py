<<<<<<< HEAD
phase_2 = {
=======
phase_2 = { 
>>>>>>> 2fc6af7214ec26cda6790afc93bf256b1de78ae3
    "smart_plating": 1000 / 180,
    "versatile_framework": 1000 / 180,
    "automated_wiring": 100 / 180,
    "steel_beam": 200 / 30,
    "steel_pipe": 200 / 30,
    "encased_industrial_beam": 50 / 30,
    "cable": 500 / 30,
    "modular_frame": 100 / 30,
    "concrete": 1000 / 30,
    "rotor": 200 / 30,
    "reinforced_iron_plate": 400 / 30,
    "copper_sheet": 500 / 30,
    "wire": 2000 / 30,
}

phase_3 = {
    "motor": 1,
    "plastic": 1,
    "rubber": 1,
    "heavy_modular_frame": 1,
}


# Item to produce and their rate (per min.)
ITEMS_AND_RATES = phase_3
# Use specified alternate recipes
USE_RECIPES = ["encased_industrial_pipe"]
# Scale factory based on ingredient availability
INGREDIENT_SUPPLY = {}

RAW_MATERIALS = ["iron_ore", "copper_ore", "limestone",
                 "coal", "sulfur", "raw_quartz", "sam", "crude_oil"]
