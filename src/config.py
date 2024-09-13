first_factory = {
    "concrete": 50,
    "steel_beam": 10,
    "cable": 25,
    "modular_frame": 5,
    "rotor": 10,
    "steel_pipe": 10,
    "reinforced_iron_plate": 40,
    "copper_sheet": 25
}

# Use specified alternate recipes
USE_RECIPES = []
# Item to produce and their rate (per min.)
ITEMS_AND_RATES = first_factory
# Scale factory based on ingredient availability
INGREDIENT_LIMITS = {

}

RAW_MATERIALS = ["iron_ore", "copper_ore", "limestone", "coal", "sulfur", "quartz"]