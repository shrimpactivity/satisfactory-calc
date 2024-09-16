import json
import jsonschema
import recipe_schema

# Retrieves, validates, and parses json recipe data.
def getRecipesData():
    fp = "./data/recipes.json"
    with open(fp) as recipes_json:
        recipes = json.load(recipes_json)
        for recipe in recipes:
            try:
                jsonschema.validate(recipe, recipe_schema.schema)
            except jsonschema.ValidationError as e:
                print(e)
                break
        return recipes

# Transforms recipes into a dict mapping product items to their recipes.
# Filters recipe dict to either primary recipes, or alternates specified in USE RECIPES.
def getRecipes(use_recipes):
    recipes_data = getRecipesData()
    items_to_all_recipes = {}
    for recipe in recipes_data:
        for product in recipe["products"]:
            item = product["item"]
            if item in items_to_all_recipes:
                items_to_all_recipes[item].append(recipe)
            else:
                items_to_all_recipes[item] = [recipe]
    
    # Filter item recipes
    item_to_recipe = {}
    for item in items_to_all_recipes:
        primary_recipe = next((rcp for rcp in items_to_all_recipes[item] if rcp["primary"] == True), None)
        specified_recipe = next((rcp for rcp in items_to_all_recipes[item] if rcp["recipe_name"] in use_recipes), None)
        # Prioritize specified recipe over primary recipe
        item_to_recipe[item] = specified_recipe if specified_recipe else primary_recipe
        if not item_to_recipe[item]:
            raise Exception(f"No primary or specified recipe for {item}")
    
    return item_to_recipe