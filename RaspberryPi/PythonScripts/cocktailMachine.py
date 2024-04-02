import json
import time
import os

from cocktailRecipe import CocktailRecipe
from bottle import Bottle, BottleHolder
# from commandMega import *
# from commandUno import *

TIME_FOR_STEPPER = 1
FLOW_RATE = 40 # flow rate of the eletrovanne in ml/s 

class CocktailMachine:
    """
    Represents a cocktail machine that can make various cocktails.

    Attributes:
        glass_bottle_holder (BottleHolder): The holder for glass bottles.
        soft_drink_bottle_holder (BottleHolder): The holder for soft drink bottles.
        stock_lemon (int): The quantity of lemon in stock.
        stock_ice (int): The quantity of ice in stock.
        cocktail_recipes (list): The list of stored cocktail recipes.
    """

    def __init__(self):
        """
        Initialize a CocktailMachine instance.
        """
        glass_bottles = [
            Bottle("Rhum", 1000, 1),
            Bottle("Gin", 1000, 2),
            Bottle("Tequila", 1000, 3),
            Bottle("Vodka", 1000, 4),
            Bottle("Whiskey", 1000, 5),
            Bottle("Sugar Syrup", 1000, 6),
            Bottle("Lime Juice", 1000, 7),
            Bottle("Triple Sec", 1000, 8),
        ]
        soft_drink_bottles = [
            Bottle("Eau pétillante", 1000, 1),
            Bottle("Sprite", 1000, 2),
            Bottle("Fanta", 1000, 3),
            Bottle("Ginger Ale", 1000, 4),
        ]
        self.glass_bottle_holder = BottleHolder(glass_bottles)
        self.soft_drink_bottle_holder = BottleHolder(soft_drink_bottles)
        self.stock_lemon = 1000
        self.stock_ice = 1000
        self.cocktail_recipes = []

    def check_ingredients(self, recipe):
        missing_ingredients = []

        # Vérifier les bouteilles en verre
        for ingredient, quantity in recipe.glass_bottles.items():
            if not self.check_single_ingredient(self.glass_bottle_holder, ingredient, quantity):
                missing_ingredients.append((ingredient, quantity))

        # Vérifier les soft drinks
        for ingredient, quantity in recipe.soft_drink_bottles.items():
            if not self.check_single_ingredient(self.soft_drink_bottle_holder, ingredient, quantity):
                missing_ingredients.append((ingredient, quantity))

        return missing_ingredients

    def check_single_ingredient(self, holder, ingredient, required_quantity):
        bottles = holder.get(ingredient)
        if not bottles:
            return False  # L'ingrédient n'est pas trouvé

        total_quantity = sum(bottle.quantity for bottle in bottles)
        if total_quantity < required_quantity:
            return False  # Quantité insuffisante

        return True  # L'ingrédient est disponible en quantité suffisante

    def use_ingredient(self, holder, bottle_position, quantity):

        bottle = holder.get_by_position(bottle_position)
        if bottle:
            # Use the ingredient from the bottle
            if bottle.quantity >= quantity:
                bottle.quantity -= quantity
                return True
            else:
                print("Not enough quantity in the bottle.")
        else:
            print("Invalid bottle position.")
        return False
    
    def fetch_bottles_for_ingredient(self, ingredient, bottle_type, required_quantity):
        """
        Fetch bottles based on the ingredient, bottle type, and required quantity.
        
        Args:
            ingredient (str): The name of the ingredient.
            bottle_type (str): The type of the bottle ('glass' or 'soft').
            required_quantity (int): The required quantity of the ingredient.
        
        Returns:
            list: A list of tuples, each containing the bottle's position, (X, Y) coordinates, and the quantity to use from that bottle.
        """
        bottle_holder = self.glass_bottle_holder if bottle_type == 'glass' else self.soft_drink_bottle_holder
        return bottle_holder.get_position_by_ingredient(ingredient, required_quantity)

    def make_cocktail(self, recipe: CocktailRecipe):


        # If all ingredients are available, then make the cocktail and update the stocks
        for ingredient, quantity in recipe.glass_bottles.items():
            bottle_position = self.glass_bottle_holder.get_position_by_name(ingredient)

            self.stepper.goto_glass_bottle(bottle_position+1)
            time.sleep((10-bottle_position)*TIME_FOR_STEPPER)

            full_shots, half_shot = divmod(quantity, 25)
            while full_shots > 0:
                self.alcoholDispenser.dispense(bottle_position+1, 1)
                full_shots -= 1
                time.sleep(6)
                
            if half_shot > 0:
                self.alcoholDispenser.dispense(bottle_position+1, 0.5)
                time.sleep(6)

            self.use_ingredient(self.soft_drink_bottle_holder, bottle_position, quantity)

        for ingredient, quantity in recipe.soft_drink_bottles.items():

            bottle_position = self.soft_drink_bottle_holder.get_by_name(ingredient)
            self.stepper.goto_soft_bottle(bottle_position)
            time.sleep(5)

            time_to_open = quantity / FLOW_RATE  # time in seconds
            print(time_to_open)
            print(bottle_position)
            self.valve.activate(bottle_position, time_to_open*1000)
            time.sleep(time_to_open)
            time.sleep(1)
            self.use_ingredient(self.soft_drink_bottle_holder, bottle_position, quantity)

        self.stock_lemon -= recipe.lemon
        self.stock_ice -= recipe.ice

        self.stepper.x_go_home()
        self.ledStrip.pulse(0xFFFFFF, 5, 5)

        print(f"Cocktail {recipe.name} is ready! Don't forget to add {recipe.comment}")


    def save_state(self):
        """
        Save the current state of the cocktail machine to a JSON file.
        """

        file_path = os.path.join(os.path.dirname(__file__), "machine_state.json")

        state = {
            "glass_bottles": self.glass_bottle_holder.to_dict(),
            "soft_drink_bottles": self.soft_drink_bottle_holder.to_dict(),
            "stock_lemon": self.stock_lemon,
            "stock_ice": self.stock_ice,
            "cocktail_recipes": [r.to_dict() for r in self.cocktail_recipes if r.save]
        }
        with open(file_path, "w") as f:
            json.dump(state, f)

    def load_state(self):
        """
        Load the saved state of the cocktail machine from a JSON file.
        """

        file_path = os.path.join(os.path.dirname(__file__), "machine_state.json")

        with open(file_path, "r") as f:
            state = json.load(f)
        self.glass_bottle_holder = BottleHolder.from_dict(state["glass_bottles"])
        self.soft_drink_bottle_holder = BottleHolder.from_dict(state["soft_drink_bottles"])
        self.stock_lemon = state["stock_lemon"]
        self.stock_ice = state["stock_ice"]
        self.cocktail_recipes = [CocktailRecipe(**recipe_dict) for recipe_dict in state["cocktail_recipes"]]

    def print_stock(self):
        """
        Print the current stock of glass bottles, soft drink bottles, lemon, and ice.
        """
        print("Glass Bottles:")
        for bottle in self.glass_bottle_holder.bottles:
            print(f"{bottle.name} (Position {bottle.position}): {bottle.quantity} ml")
        print("\nSoft Drink Bottles:")
        for bottle in self.soft_drink_bottle_holder.bottles:
            print(f"{bottle.name} (Position {bottle.position}): {bottle.quantity} ml")
        print(f"\nLemon: {self.stock_lemon}")
        print(f"Ice: {self.stock_ice}")

    def print_recipes(self):
        """
        Print all the stored cocktail recipes.
        """
        for recipe in self.cocktail_recipes:
            print(f"Recipe Name: {recipe.name}")
            print(f"Glass Bottles: {recipe.glass_bottles}")
            print(f"Soft Drink Bottles: {recipe.soft_drink_bottles}")
            print(f"Lemon: {recipe.lemon}")
            print(f"Ice: {recipe.ice}")
            print(f"Comment: {recipe.comment}")
            print()

    def change_bottle(self, bottle_type, position, new_name, new_quantity):
        """
        Change the name and quantity of a bottle in the specified holder.

        Args:
            bottle_type (str): The type of the bottle holder ("glass" or "soft").
            position (int): The position of the bottle to change.
            new_name (str): The new name of the bottle.
            new_quantity (int): The new quantity of the bottle.
        """
        if bottle_type not in ["glass", "soft"]:
            print("Invalid bottle type. Please specify either 'glass' or 'soft'.")
            return

        holder = self.glass_bottle_holder if bottle_type == "glass" else self.soft_drink_bottle_holder
        bottle = holder.get_by_position(position)

        if not bottle:
            print(f"No bottle found at position {position}.")
            return

        old_name = bottle.name
        holder.update_bottle(Bottle(new_name, new_quantity, position))

        print(f"{old_name} at position {position} has been replaced by {new_name} with a quantity of {new_quantity}.")

    def get_stock(self):
        """
        Get the current stock of the cocktail machine.

        Returns:
            tuple: A tuple containing the glass bottle holder, soft drink bottle holder, lemon quantity, and ice quantity.
        """
        return self.glass_bottle_holder, self.soft_drink_bottle_holder, self.stock_lemon, self.stock_ice

    def get_glass_bottles(self):
        return self.glass_bottle_holder.get_bottles()

    def get_glass_bottle_names(self):
        return [bottle.name for bottle in self.get_glass_bottles()]

    def get_soft_bottles(self):
        return self.soft_drink_bottle_holder.get_bottles()

    def get_soft_bottle_names(self):
        return [bottle.name for bottle in self.get_soft_bottles()]

    def get_recipe_by_name(self, name):
        """
        Get a recipe from the cocktail machine by its name.

        Args:
            name (str): The name of the recipe to retrieve.

        Returns:
            CocktailRecipe or None: The recipe with the specified name, or None if not found.
        """
        for recipe in self.cocktail_recipes:
            if recipe.name == name:
                return recipe
        return None

    def get_recipes(self):
        """
        Get all the stored cocktail recipes.

        Returns:
            list: The list of stored cocktail recipes.
        """
        return self.cocktail_recipes
    

    def get_bottle_list(self, is_glass=True):
        if is_glass:
            # Liste de noms d'alcool en bouteilles en verre
            bottle_list = [
                "Vodka",
                "Gin",
                "Rum",
                "Tequila",
                "Whiskey",
                "Brandy",
                "Cognac",
                "Absinthe"
            ]
        else:
            # Liste de noms de soft en bouteilles non en verre
            bottle_list = [
                "Soda",
                "Cola",
                "Lemonade",
                "Orange Juice",
                "Apple Juice",
                "Ginger Ale",
                "Tonic Water",
                "Iced Tea"
            ]
        return bottle_list

if __name__ == "__main__":
    # Create an instance of the cocktail machine
    machine = CocktailMachine()

    # Print the initial stock
    print("Initial Stock: \n")
    machine.load_state()
    machine.print_stock()
    print()

    # Create a cocktail recipe with missing alcohol and add the recipe to the machine
    recipe = CocktailRecipe("Mojito Black", {"Rhum Black": 50, "Lime Juice": 20}, {"Eau pétillante": 100}, 1, 200,
                            "Mint leaves")
    machine.cocktail_recipes.append(recipe)

    # Make the cocktail and generate an error
    recipe = machine.get_recipe_by_name("Mojito Black")
    print(f"Making {recipe.name}...")
    machine.make_cocktail(recipe)
    print()

    # Add the Black Rhum Bottle 
    machine.change_bottle("glass", 1, "Rhum Black", 1000)

    # Print the updated stock
    print("Updated Stock:")
    machine.print_stock()

    # Make the cocktail and generate an error
    recipe = machine.get_recipe_by_name("Mojito Black")
    print(f"Making {recipe.name}...")
    machine.make_cocktail(recipe)
    print()

    # Print the updated stock
    print("Updated Stock:")
    machine.print_stock()
