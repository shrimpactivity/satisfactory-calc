import math

# Get production/consumption rate (per minute) based on recipe duration and item amount
def getRate(amount, duration):
    return 60 / duration * amount

# Generates a tree encoded as list [item, rate, [children]]
def buildFactory(items, rates, item_recipes):
    ingredient_totals = {}
    machine_totals = {}
    byproduct_totals = {}

    def buildFactoryHelper(item, rate):
        # Base case
        if item not in item_recipes:
            return [item, rate, 0, []]
        # Base case in the event of looping recipe?
        if rate < 0.01:
            return [item, 0, []]

        recipe = item_recipes[item]
        recipe_product = [p for p in recipe["products"] if p["item"] == item][0]
        machines = rate / getRate(recipe_product["amount"], recipe["duration"])
        if item in machine_totals:
            machine_totals[item] += machines
        else:
            machine_totals[item] = machines

        # Track byproducts and include in result
        byproducts = [p for p in recipe["products"] if p["item"] != item]
        for product in byproducts:
            byproduct_item = product["item"]
            byproduct_rate = getRate(product["amount"], recipe["duration"]) * machines
            byproduct_rate = round(byproduct_rate, 1)
            if byproduct_item in byproduct_totals:
                byproduct_totals[byproduct_item] += byproduct_rate
            else:
                byproduct_totals[byproduct_item] = byproduct_rate

        children = []
        for ingredient in recipe["ingredients"]:
            ingredient_item = ingredient["item"]
            consumption_rate = getRate(ingredient["amount"], recipe["duration"]) * machines
            consumption_rate = round(consumption_rate, 1)
            
            # Add to total ingredient count
            if ingredient_item in ingredient_totals:
                ingredient_totals[ingredient_item] += consumption_rate
            else:
                ingredient_totals[ingredient_item] = consumption_rate
            
            children.append(buildFactoryHelper(ingredient_item, consumption_rate))
        return [item, round(rate, 2), math.floor(machines + 1), children]
    
    trees = [buildFactoryHelper(items[i], rates[i]) for i in range(len(items))]

    return {
        "trees": trees,
        "ingredient_totals": ingredient_totals,
        "machine_totals": machine_totals,
        "byproducts": byproduct_totals,
    }

def scaleFactory(factory, scale):
    def scaleFactoryTree(tree):
        if (len(tree)) == 0:
            return tree
        item = tree[0]
        amount = round(tree[1] * scale, 2)
        machines = round(tree[1] * scale, 2)
        children = [scaleFactoryTree(t) for t in tree[2]]
        return [item, amount, machines, children]
    trees = [scaleFactoryTree(t) for t in factory['trees']]
    ingredient_totals = factory["ingredient_totals"]
    for ing in ingredient_totals:
        ingredient_totals[ing] = round(ingredient_totals[ing] * scale, 2)
    byproduct_totals = factory["byproducts"]
    for b in byproduct_totals:
        byproduct_totals[b] = round(byproduct_totals[b] * scale, 2)
    factory["trees"] = trees
    factory["ingredient_totals"] = ingredient_totals
    factory["byproducts"] = byproduct_totals

def scaleFactoryToIngredient(ingredient, amount, factory):
    scale = amount / factory["ingredient_totals"][ingredient]
    scaleFactory(factory, scale)

RAW_MATERIALS = ["iron_ore", "copper_ore", "limestone", "coal", "sulfur", "quartz"]

def prettyPrintFactory(factory, tabSize=4):

    def prettyPrintTreeHelper(tree, tabs=0):
        if (len(tree) == 0):
            return
        
        item = tree[0]
        rate = tree[1]
        machines = tree[2]
        children = tree[3]

        whitespace = " " * (tabs) * tabSize
        whitespace += "\u25D9" if tabs == 0 else "\u21B3"
        machines_text = "" if machines == 0 else f"({machines} machines)"
        print(f" {whitespace} {item} - {rate} {machines_text}")
        for child in children:
            prettyPrintTreeHelper(child, tabs + 1)
    
    print("######\n")
    print("=== FACTORY ===")
    for tree in factory["trees"]:
        prettyPrintTreeHelper(tree)
    print("\n=== INGREDIENT TOTALS ===")
    for item in factory['ingredient_totals']:
        rate = factory['ingredient_totals'][item]
        machines = 0 if item not in factory['machine_totals'] else factory['machine_totals'][item]
        machines_text = "" if machines == 0 else f"({machines} machines)"
        print(f"\u2022 {item} - {rate} {machines_text}")
    print("\n=== RAW MATERIALS ===")
    for item in [x for x in factory['ingredient_totals'] if x in RAW_MATERIALS]:
        rate = factory['ingredient_totals'][item]
        print(f"\u2022 {item} - {rate}")
    print("\n=== BYPRODUCTS ===")
    for item in factory['byproducts']:
        rate = factory['byproducts'][item]
        print(f"\u2022 {item} - {rate}")
    print("\n######")