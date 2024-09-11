RAW_MATERIALS = ["iron_ore", "copper_ore", "limestone"]

# Generates a tree encoded as list [item, rate, [children]]
def factoryTree(item, rate, item_recipes):
    byproducts = {}

    def factoryTreeHelper(item, rate, item_recipes):
        # Base case
        if item not in item_recipes:
            if item not in RAW_MATERIALS:
                print(f"No recipe available for {item}")
            return [item, rate, []]
        # Base case in the event of looping recipe?
        if rate < 0.01:
            return [item, 0, []]

        recipe = item_recipes["item"]
        relevant_product = [p["item"] for p in recipe["products"] if p["item"] == item]
        byproducts = [p["item"] for p in recipe["products"] if p["item"] != item]
        item_rate = round(60 / recipe["duration"], 2)
        ingredient_items = [ingredient["item"] for ingredient in recipe["ingredients"]]
        return [item, rate, ]
    