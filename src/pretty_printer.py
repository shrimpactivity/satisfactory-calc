import math
import config

def prettyPrintFactoryTree(tree, tabs=0, tabSize=3):
        # Base case
        if (len(tree) == 0):
            return
        
        item = tree[0]
        rate = round(tree[1], 1)
        machines = round(tree[2], 1)
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
    print("\n=== ITEM TOTALS ===")
    for item in sorted([item for item in factory['item_totals']]):
        rate = round(factory['item_totals'][item], 1)
        machines = 0 if item not in factory['machine_totals'] else round(factory['machine_totals'][item], 1)
        machines_text = "" if machines == 0 else f"({machines} machines)"
        print(f"\u2022 {item} - {rate} {machines_text}")
    print("\n=== RAW MATERIALS ===")
    for item in sorted([x for x in factory['item_totals'] if x in config.RAW_MATERIALS]):
        rate = round(factory['item_totals'][item], 1)
        print(f"\u2022 {item} - {rate}")
    print("\n=== BYPRODUCTS ===")
    for item in sorted([item for item in factory['byproducts']]):
        rate = round(factory['byproducts'][item], 1)
        print(f"\u2022 {item} - {rate}")
    print("\n######")