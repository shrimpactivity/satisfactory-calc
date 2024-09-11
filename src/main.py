import factory_builder
import recipe

# Use specified alternate recipes
USE_RECIPES = []
# Item to produce
ITEMS = ["smart_plating", "iron_plate"]
# Rate to produce item (per minute)
RATES = [60, 120]

def main():
    recipes = recipe.getRecipes(USE_RECIPES)
    factory = factory_builder.buildFactory(ITEMS, RATES, recipes)
    factory_builder.prettyPrintFactory(factory)

if __name__ == "__main__":
    main()