import factory
import recipe

USE_RECIPES = []
RAW_MATERIALS = ["iron_ore", "copper_ore", "limestone"]
product = []

def main():
    recipes = recipe.getRecipes(USE_RECIPES)
    print(recipes["rotor"])

if __name__ == "__main__":
    main()


