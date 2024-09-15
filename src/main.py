import factory_builder
import pretty_printer
import recipe
import config

def main():
    recipes = recipe.getRecipes(config.USE_RECIPES)
    factory = factory_builder.buildFactory(config.ITEMS_AND_RATES, recipes)

    # Scale factory by ingredient supply
    i = 0        
    for item in config.INGREDIENT_SUPPLY:
        item_consumption_rate = factory["item_totals"][item]
        # Always scale factory to first ingredient
        # Only scale factory by other items if it consumes more than supply
        if (i == 0 or item_consumption_rate > config.INGREDIENT_SUPPLY[item]):
            print(f'Scaling factory to fit {item} production...')
            factory_builder.scaleFactoryToIngredient(item, config.INGREDIENT_SUPPLY[item], factory)
        i += 1
        
    pretty_printer.prettyPrintFactory(factory)

if __name__ == "__main__":
    main()