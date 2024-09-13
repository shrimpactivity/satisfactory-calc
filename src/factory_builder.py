import math
import config

# Get production/consumption rate (per minute) based on recipe duration and item amount
def getRate(amount, duration):
    return 60 / duration * amount


def addToRunningTotal(dict, key, amount):
    if key in dict:
        dict[key] += amount
    else:
        dict[key] = amount


# Generates a tree encoded as list [item, rate, [children]]
def buildFactory(items_to_rates, item_recipes):
    ingredient_totals = {}
    machine_totals = {}
    byproduct_totals = {}

    def buildFactoryHelper(item, rate):
        # Base case
        if item not in item_recipes:
            return [item, rate, 0, []]
        # Base case in the event of looping recipe?
        if rate < 0.001:
            return [item, rate, 0, []]

        recipe = item_recipes[item]
        recipe_product = [p for p in recipe["products"] if p["item"] == item][0]
        machines = rate / getRate(recipe_product["amount"], recipe["duration"])
        
        addToRunningTotal(machine_totals, item, machines)

        # Add byproduct running totals
        byproducts = [p for p in recipe["products"] if p["item"] != item]
        for product in byproducts:
            byproduct_item = product["item"]
            byproduct_rate = getRate(product["amount"], recipe["duration"]) * machines
            addToRunningTotal(byproduct_totals, byproduct_item, byproduct_rate)

        # Recursive call on ingredient children
        children = []
        for ingredient in recipe["ingredients"]:
            ingredient_item = ingredient["item"]
            consumption_rate = getRate(ingredient["amount"], recipe["duration"]) * machines
            
            addToRunningTotal(ingredient_totals, ingredient_item, consumption_rate)
            
            children.append(buildFactoryHelper(ingredient_item, consumption_rate))
        
        return [item, rate, machines, children]
    
    trees = [buildFactoryHelper(item, items_to_rates[item]) for item in items_to_rates]

    return {
        "trees": trees,
        "ingredient_totals": ingredient_totals,
        "machine_totals": machine_totals,
        "byproducts": byproduct_totals,
    }


def scaleFactoryTree(tree, scale):
        if (len(tree)) == 0:
            return tree
        item = tree[0]
        amount = tree[1] * scale
        machines = tree[2] * scale
        children = [scaleFactoryTree(t,scale) for t in tree[3]]
        return [item, amount, machines, children]


def scaleFactory(factory, scale):
    trees = [scaleFactoryTree(t, scale) for t in factory['trees']]
    ingredient_totals = factory["ingredient_totals"]
    for ing in ingredient_totals:
        ingredient_totals[ing] = ingredient_totals[ing] * scale
    byproduct_totals = factory["byproducts"]
    for b in byproduct_totals:
        byproduct_totals[b] = byproduct_totals[b] * scale
    machine_totals = factory["machine_totals"]
    for m in machine_totals:
        machine_totals[m] = machine_totals[m] * scale
    factory["trees"] = trees
    factory["ingredient_totals"] = ingredient_totals
    factory["byproducts"] = byproduct_totals


def scaleFactoryToIngredient(ingredient, amount, factory):
    scale = amount / factory["ingredient_totals"][ingredient]
    scaleFactory(factory, scale)


def prettyPrintFactoryTree(tree, tabs=0, tabSize=3):
        # Base case
        if (len(tree) == 0):
            return
        
        item = tree[0]
        rate = round(tree[1], 2)
        machines = math.floor(tree[2] + 1)
        children = tree[3]

        whitespace = " " * (tabs) * tabSize
        whitespace += "\u25D9" if tabs == 0 else "\u21B3"
        machines_text = "" if machines <= 1 else f"({machines} machines)"
        print(f" {whitespace} {item} - {rate} {machines_text}")
        for child in children:
            prettyPrintFactoryTree(child, tabs + 1)


def prettyPrintFactory(factory):
    print("######\n")
    print("=== FACTORY ===")
    for tree in factory["trees"]:
        prettyPrintFactoryTree(tree)
    print("\n=== INGREDIENT TOTALS ===")
    for item in factory['ingredient_totals']:
        rate = round(factory['ingredient_totals'][item], 2)
        machines = 0 if item not in factory['machine_totals'] else math.floor(factory['machine_totals'][item] + 1)
        machines_text = "" if machines <= 0 else f"({machines} machines)"
        print(f"\u2022 {item} - {rate} {machines_text}")
    print("\n=== RAW MATERIALS ===")
    for item in [x for x in factory['ingredient_totals'] if x in config.RAW_MATERIALS]:
        rate = round(factory['ingredient_totals'][item], 2)
        print(f"\u2022 {item} - {rate}")
    print("\n=== BYPRODUCTS ===")
    for item in factory['byproducts']:
        rate = round(factory['byproducts'][item], 2)
        print(f"\u2022 {item} - {rate}")
    print("\n######")