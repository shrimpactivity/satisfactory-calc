import json
import jsonschema
import recipe_schema
import sys

use_recipes = []
product = []
resources = ["iron_ore", "copper_ore", "limestone"]

def getRecipes():
    fp = "./data/recipes.json"
    with open(fp) as recipes_json:
        recipes = json.load(recipes_json)
        for recipe in recipes:
            try:
                jsonschema.validate(recipe, recipe_schema.schema)
            except jsonschema.ValidationError as e:
                print(e)
        return recipes

def getRecipeDict(recipes):
    itemToRecipe = {}
    for recipe in recipes:
        for product in recipe["products"]:
            if product["item"] in itemToRecipe:
                itemToRecipe[product["item"]].append(recipe)
            else: 
                itemToRecipe[product["item"]] = [recipe]
    return itemToRecipe

def factoryTree(item, rate, items_to_recipes, use_recipes):
    requirements = []
    if (product) not in resources:
        item_recipes = items_to_recipes[item]
        if (len(use_recipes) > 0):
            item_recipes = [r for r in item_recipes if]
    
    return {
        item: item,
        rate: rate,
        requires: 
    }
    


def main():
    recipes = getRecipes()
    print(getRecipeDict(recipes))

if __name__ == "__main__":
    main()


