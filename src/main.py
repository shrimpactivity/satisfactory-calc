import factory
import recipe

# Use specified alternate recipes
USE_RECIPES = []
# Items with no recipes
RAW_MATERIALS = ["iron_ore", "copper_ore", "limestone"]
# Item to produce
ITEM = "smart_plating"
# Rate to produce item (per minute)
RATE = 120

def main():
    recipes = recipe.getRecipes(USE_RECIPES)
    print(factory.buildFactory(ITEM, RATE, recipes, RAW_MATERIALS))

if __name__ == "__main__":
    main()


