import factory_builder
import recipe
import config


def main():
    recipes = recipe.getRecipes(config.USE_RECIPES)
    factory = factory_builder.buildFactory(config.ITEMS_AND_RATES, recipes)
    for item in config.INGREDIENT_LIMITS:
        item_consumption_rate = factory["ingredient_totals"][item]
        # Only scale factory if it consumes more than supply limit
        if (item_consumption_rate > config.INGREDIENT_LIMITS[item]):
            print(f'Scaling factory to fit {item} production...')
            factory_builder.scaleFactoryToIngredient(item, config.INGREDIENT_LIMITS[item], factory)
    factory_builder.prettyPrintFactory(factory)

if __name__ == "__main__":
    main()

# TODO: make factory builder accept dict of items to rates.