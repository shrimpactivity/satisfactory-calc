phase_2 = {
    "factory": {
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
    },
    "recipes": [
        "encased_industrial_pipe"
    ]
}

early_quartz = {
    "factory": {
        "quartz_crystal": 1,
        "silica": 1
    },
    "recipes": []

}

# Use specified alternate recipes
USE_RECIPES = early_quartz["recipes"]
# Item to produce and their rate (per min.)
ITEMS_AND_RATES = early_quartz["factory"]
# Scale factory based on ingredient availability
INGREDIENT_SUPPLY = {
    "raw_quartz": 240
}

RAW_MATERIALS = ["iron_ore", "copper_ore",
                 "limestone", "coal", "sulfur", "raw_quartz"]
