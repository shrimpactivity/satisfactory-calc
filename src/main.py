import factory_builder
import recipe

# Use specified alternate recipes
USE_RECIPES = []
# Item to produce
ITEMS = ["smart_plating"]
# Rate to produce item (per minute)
RATES = [5]

def main():
    recipes = recipe.getRecipes(USE_RECIPES)
    factory = factory_builder.buildFactory(ITEMS, RATES, recipes)
    #factory_builder.scaleFactoryToIngredient("iron_plate", 180, factory)
    factory_builder.prettyPrintFactory(factory)

if __name__ == "__main__":
    main()