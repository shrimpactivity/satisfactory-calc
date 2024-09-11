# Get production/consumption rate (per minute) based on recipe duration and item amount
def getRate(amount, duration, rounding=1):
    return round(60 / duration, rounding) * amount

# Generates a tree encoded as list [item, rate, [children]]
def buildFactory(item, rate, item_recipes, raw_materials):
    byproduct_totals = {}
    raw_material_totals = {}

    def buildFactoryHelper(item, rate):
        # Base case
        if item not in item_recipes:
            if item not in raw_materials:
                print(f"No recipe available for {item}")
            if item in raw_material_totals:
                raw_material_totals[item] += rate
            else:
                raw_material_totals[item] = rate
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
            consumption_rate = getRate(ingredient["amount"], recipe["duration"]) * multiplier
            children.append(buildFactoryHelper(ingredient["item"], consumption_rate))
        return [item, rate, children]
    
    return {
        "tree": buildFactoryHelper(item, rate), 
        "byproducts": byproduct_totals,
        "raw_materials": raw_material_totals
    }

def prettyPrintTree(tree, tabSize=2):
    def prettyPrintTreeHelper(tree, tabs):
        if (len(tree) == 0):
            return
        whitespace = "  "
        print("")