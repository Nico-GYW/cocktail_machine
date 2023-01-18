import json

class Bottle:
    def __init__(self, name, quantity, position):
        self.name = name
        self.quantity = quantity
        self.position = position
    
    def to_dict(self):
        return {"name": self.name, "quantity": self.quantity, "position": self.position}
    
class CocktailRecipe:
    def __init__(self, name, glass_bottles, soft_drink_bottles, lemon, ice, comment):
        self.name = name
        self.glass_bottles = glass_bottles
        self.soft_drink_bottles = soft_drink_bottles
        self.lemon = lemon
        self.ice = ice
        self.comment = comment
        
    def to_dict(self):
        return {'name': self.name, 'glass_bottles': self.glass_bottles, 'soft_drink_bottles': self.soft_drink_bottles, 'lemon': self.lemon, 'ice': self.ice, 'comment': self.comment}
    
    def check_ingredients_availability(self, machine):
        # Check if all the ingredients are available on the machine
        for bottle_name, quantity in self.glass_bottles.items():
            if bottle_name not in machine.glass_bottles:
                return f"{bottle_name} not found on the machine."
            if machine.glass_bottles[bottle_name].quantity < quantity:
                return f"Not enough {bottle_name} on the machine."
        for bottle_name, quantity in self.soft_drink_bottles.items():
            if bottle_name not in machine.soft_drink_bottles:
                return f"{bottle_name} not found on the machine."
            if machine.soft_drink_bottles[bottle_name].quantity < quantity:
                return f"Not enough {bottle_name} on the machine."
        if machine.stock_lemon < self.lemon:
            return "Not enough lemon on the machine."
        if machine.stock_ice < self.ice:
            return "Not enough ice on the machine."
        return "All ingredients are available."

class CocktailMachine:
    def __init__(self):
        # Initialize the glass bottles with a certain quantity
        self.glass_bottles = {
            "Rhum": Bottle("Rhum", 1000, 1),
            "Gin": Bottle("Gin", 1000, 2),
            "Tequilla": Bottle("Tequila", 1000, 3),
            "Vodka": Bottle("Vodka", 1000, 4),
            "Whiskey": Bottle("Whiskey", 1000, 5),
            "Sugar Syrup": Bottle("Sugar Syrup", 1000, 6),
            "Cointreau": Bottle("Lime Juice", 1000, 7),
            "Triple Sec": Bottle("Triple Sec", 1000, 8),
        }
        # Initialize the soft drink bottles with a certain quantity
        self.soft_drink_bottles = {
            "Eau pétillante": Bottle("Eau pétillante", 1000, 1),
            "Sprite": Bottle("Sprite", 1000, 2),
            "Fanta": Bottle("Fanta", 1000, 3),
            "Ginger Ale": Bottle("Ginger Ale", 1000, 4),
        }
        # Initialize the stock of lemon and ice
        self.stock_lemon = 1000
        self.stock_ice = 1000
        self.cocktail_recipes = []

    def make_cocktail(self, recipe):
        availability = recipe.check_ingredients_availability(self)
        if availability != "All ingredients are available.":
            print(availability)
            return
        # Make the cocktail
        for bottle_name, quantity in recipe.glass_bottles.items():
            self.glass_bottles[bottle_name].quantity -= quantity
        for bottle_name, quantity in recipe.soft_drink_bottles.items():
            self.soft_drink_bottles[bottle_name].quantity -= quantity
        self.stock_lemon -= recipe.lemon
        self.stock_ice -= recipe.ice
        print(f"Cocktail {recipe.name} is ready! Don't forget to add {recipe.comment}")
    
    def save_recipe(self, recipe):
        with open(f"{recipe.name}.json", "w") as f:
            json.dump(recipe.to_dict(), f)
    def load_recipe(self, recipe_name):
        with open(f"{recipe_name}.json", "r") as f:
            recipe_dict = json.load(f)
        recipe = CocktailRecipe(recipe_dict['name'], recipe_dict['glass_bottles'], recipe_dict['soft_drink_bottles'], recipe_dict['lemon'], recipe_dict['ice'], recipe_dict['comment'])
        self.cocktail_recipes.append(recipe)
    
    def save_state(self):
        # Save the current state of the machine
        state = {
            "glass_bottles": {k: v.to_dict() for k, v in self.glass_bottles.items()},
            "soft_drink_bottles": {k: v.to_dict() for k, v in self.soft_drink_bottles.items()},
            "stock_lemon": self.stock_lemon,
            "stock_ice": self.stock_ice,
            "cocktail_recipes": [r.to_dict() for r in self.cocktail_recipes]
        }
        with open("machine_state.json", "w") as f:
            json.dump(state, f)
    
    def load_state(self):
        # Load the previous state of the machine
        with open("machine_state.json", "r") as f:
            state = json.load(f)
        self.glass_bottles = {k: Bottle(**v) for k, v in state["glass_bottles"].items()}
        self.soft_drink_bottles = {k: Bottle(**v) for k, v in state["soft_drink_bottles"].items()}
        self.stock_lemon = state["stock_lemon"]
        self.stock_ice = state["stock_ice"]
        self.cocktail_recipes = [CocktailRecipe(**r) for r in state["cocktail_recipes"]]
        
    def print_recipes(self):
        # Print all the stored cocktail recipes
        for recipe in self.cocktail_recipes:
            print(f"Recipe Name: {recipe.name}")
            print(f"Glass Bottles: {recipe.glass_bottles}")
            print(f"Soft Drink Bottles: {recipe.soft_drink_bottles}")
            print(f"Lemon: {recipe.lemon}")
            print(f"Ice: {recipe.ice}")
            print(f"Comment: {recipe.comment}")
            print()
            
    def print_stock(self):
        # Print the current stock of the machine
        print("Glass Bottles:")
        for bottle in self.glass_bottles.values():
            print(f"{bottle.name} ({bottle.position}): {bottle.quantity}")
        print("Soft Drink Bottles:")
        for bottle in self.soft_drink_bottles.values():
            print(f"{bottle.name} ({bottle.position}): {bottle.quantity}")
        print(f"Lemon: {self.stock_lemon}")
        print(f"Ice: {self.stock_ice}")
        
    def get_recipe_by_name(self, name):
        for recipe in self.cocktail_recipes:
            if recipe.name == name:
                return recipe
        return None

    def change_bottle(self, bottle_type, position, new_name, new_quantity):
        if bottle_type == "glass":
            bottles = self.glass_bottles
        elif bottle_type == "soft":
            bottles = self.soft_drink_bottles
        else:
            print("Invalid bottle type. Please specify either 'glass' or 'soft'.")
            return

        found = False
        for name, bottle in bottles.items():
            if bottle.position == position:
                old_name = name
                found = True
                break
        if not found:
            print(f"No bottle found at position {position}.")
            return
        bottles[new_name] = Bottle(new_name, bottles[old_name].position, new_quantity)
        del bottles[old_name]
        print(f"{old_name} at position {position} has been replaced by {new_name} with a quantity of {new_quantity}.")


# Creating a new instance of the machine
machine = CocktailMachine()

# Creating a new recipe
mojito_recipe = CocktailRecipe("Mojito", {"Rhum": 50, "Sugar Syrup": 20}, {"Eau pétillante": 20}, 2, 5, "Mint leaves and lime wedges")
machine.cocktail_recipes.append(mojito_recipe)

# Loading the previous state of the machine
# machine.load_state()

# Making a cocktail
machine.make_cocktail(mojito_recipe)

# Saving the state of the machine
machine.save_state()

# Printing the current stock of the machine
machine.print_stock()

# Print all the stored cocktail recipes
machine.print_recipes()

# Making a cocktail by name
machine.make_cocktail(machine.get_recipe_by_name("Mojito"))

