# Get production/consumption rate (per minute) based on recipe duration and item amount
def getRate(amount, duration, rounding=1):
    return round(60 / duration, rounding) * amount

# Generates a tree encoded as list [item, rate, [children]]
def buildFactory(items, rates, item_recipes):
    ingredient_totals = {}
    byproduct_totals = {}

    def buildFactoryHelper(item, rate):
        # Base case
        if item not in item_recipes:
            return [item, rate, []]
        # Base case in the event of looping recipe?
        if rate < 0.01:
            return [item, 0, []]

        recipe = item_recipes[item]
        product = [p for p in recipe["products"] if p["item"] == item][0]
        multiplier = round(rate / getRate(product["amount"], recipe["duration"], 5), 2)

        # Track byproducts and include in result
        byproducts = [p for p in recipe["products"] if p["item"] != item]
        for product in byproducts:
            byproduct_item = product["item"]
            byproduct_rate = getRate(product["amount"], recipe["duration"]) * multiplier
            if byproduct_item in byproduct_totals:
                byproduct_totals[byproduct_item] += byproduct_rate
            else:
                byproduct_totals[byproduct_item] = byproduct_rate
        
        children = []
        for ingredient in recipe["ingredients"]:
            ingredient_item = ingredient["item"]
            consumption_rate = getRate(ingredient["amount"], recipe["duration"]) * multiplier
            
            # Add to total ingredient count
            if ingredient_item in ingredient_totals:
                ingredient_totals[ingredient_item] += consumption_rate
            else:
                ingredient_totals[ingredient_item] = consumption_rate
            
            children.append(buildFactoryHelper(ingredient_item, consumption_rate))
        return [item, rate, children]
    
    trees = [buildFactoryHelper(items[i], rates[i]) for i in range(len(items))]

    return {
        "trees": trees,
        "ingredient_totals": ingredient_totals,
        "byproducts": byproduct_totals,
    }

RAW_MATERIALS = ["iron_ore", "copper_ore", "limestone", "coal"]

def prettyPrintFactory(factory, tabSize=4):

    def prettyPrintTreeHelper(tree, tabs=0):
        if (len(tree) == 0):
            return
        
        item = tree[0]
        rate = tree[1]
        children = tree[2]

        whitespace = " " * (tabs) * tabSize
        whitespace += "\u25D9" if tabs == 0 else "\u21B3"
        print(f" {whitespace} {item} - {rate}")
        for child in children:
            prettyPrintTreeHelper(child, tabs + 1)

    items_list = ' & '.join([x[0] for x in factory["trees"]])
    
    print("######\n")
    print("=== FACTORY ===")
    for tree in factory["trees"]:
        prettyPrintTreeHelper(tree)
    print("\n=== INGREDIENT TOTALS ===")
    for item in factory['ingredient_totals']:
        rate = factory['ingredient_totals'][item]
        print(f"- {item} - {rate}")
    print("\n=== RAW MATERIALS ===")
    for item in [x for x in factory['ingredient_totals'] if x in RAW_MATERIALS]:
        rate = factory['ingredient_totals'][item]
        print(f"- {item} - {rate}")
    print("\n=== BYPRODUCTS ===")
    for item in factory['byproducts']:
        rate = factory['byproducts'][item]
        print(f"- {item} - {rate}")
    print("\n######")