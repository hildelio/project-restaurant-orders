import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_data_from_csv(source_path)

    def load_data_from_csv(self, source_path: str) -> None:
        dish_mapping = {}

        with open(source_path, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                dish = dish_mapping.get(dish_name)

                if not dish:
                    dish = Dish(dish_name, price)
                    dish_mapping[dish_name] = dish
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)
