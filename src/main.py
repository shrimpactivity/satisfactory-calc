import factory_builder
import recipe

# Use specified alternate recipes
USE_RECIPES = []
# Item to produce
ITEMS = ["versatile_framework"]
# Rate to produce item (per minute)
RATES = [1]

def main():
    recipes = recipe.getRecipes(USE_RECIPES)
    factory = factory_builder.buildFactory(ITEMS, RATES, recipes)
    #factory_builder.scaleFactoryToIngredient("iron_ore", 150, factory)
    factory_builder.prettyPrintFactory(factory)

if __name__ == "__main__":
    main()

# TODO: make factory builder accept dict of items to rates.