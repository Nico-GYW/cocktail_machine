class CocktailRecipe:
    """
    Represents a cocktail recipe with various ingredients.

    Attributes:
        name (str): The name of the cocktail recipe.
        glass_bottles (dict): The dictionary of glass bottles required for the recipe.
        soft_drink_bottles (dict): The dictionary of soft drink bottles required for the recipe.
        lemon (int): The quantity of lemon required for the recipe.
        ice (int): The quantity of ice required for the recipe.
        comment (str): Additional comment or instructions for the recipe.
        image (str): The path to the image of the cocktail recipe.
    """

    def __init__(self, name, glass_bottles, soft_drink_bottles, lemon, ice, comment,
                 image="ressources/cocktail/default.png"):
        """
        Initialize a CocktailRecipe instance.

        Args:
            name (str): The name of the cocktail recipe.
            glass_bottles (dict): The dictionary of glass bottles required for the recipe.
            soft_drink_bottles (dict): The dictionary of soft drink bottles required for the recipe.
            lemon (int): The quantity of lemon required for the recipe.
            ice (int): The quantity of ice required for the recipe.
            comment (str): Additional comment or instructions for the recipe.
            image (str, optional): The path to the image of the cocktail recipe. Defaults to "ressources/cocktail/default.png".
        """
        self.name = name
        self.glass_bottles = glass_bottles
        self.soft_drink_bottles = soft_drink_bottles
        self.lemon = lemon
        self.ice = ice
        self.comment = comment
        self.image = image

    def to_dict(self):
        """
        Convert the CocktailRecipe instance to a dictionary.

        Returns:
            dict: The dictionary representation of the CocktailRecipe instance.
        """
        return {'name': self.name, 'glass_bottles': self.glass_bottles, 'soft_drink_bottles': self.soft_drink_bottles,
                'lemon': self.lemon, 'ice': self.ice, 'comment': self.comment, 'image': self.image}

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image
    
    def total_liquid_quantity(self):
        total = sum(self.glass_bottles.values()) + sum(self.soft_drink_bottles.values())
        return total

    def alcohol_percentage(self):
        # Supposons que chaque entrée dans glass_bottles est 40% d'alcool
        alcohol_volume = sum(self.glass_bottles.values()) * 0.4
        total_volume = self.total_liquid_quantity()
        return (alcohol_volume / total_volume) * 100 if total_volume > 0 else 0
    
    def add_bottle(self, bottle_name, quantity, is_glass=True):
        """
        Ajoute une bouteille dans la recette.

        Args:
            bottle_name (str): Nom de la bouteille à ajouter ou à mettre à jour.
            quantity (int): Quantité de la bouteille.
            is_glass (bool): True si la bouteille est en verre, False si c'est une bouteille soft.
        """
        bottle_dict = self.glass_bottles if is_glass else self.soft_drink_bottles
        if bottle_name in bottle_dict:
            # Si la bouteille existe déjà, met à jour la quantité
            bottle_dict[bottle_name] += quantity
        else:
            # Sinon, ajoute la bouteille avec la quantité spécifiée
            bottle_dict[bottle_name] = quantity

    def replace_bottle(self, old_bottle_name, new_bottle_name, quantity, is_glass=True):
        bottle_dict = self.glass_bottles if is_glass else self.soft_drink_bottles
        if old_bottle_name in bottle_dict:
            # Supprime l'ancienne bouteille
            del bottle_dict[old_bottle_name]
        # Ajoute la nouvelle bouteille avec la quantité spécifiée
        bottle_dict[new_bottle_name] = quantity

    def remove_bottle(self, bottle_name, is_glass=True):
        # Choix du dictionnaire approprié en fonction du type de bouteille
        bottle_dict = self.glass_bottles if is_glass else self.soft_drink_bottles

        # Vérifie si la bouteille à supprimer existe dans le dictionnaire
        if bottle_name in bottle_dict:
            # Supprime la bouteille du dictionnaire
            del bottle_dict[bottle_name]

