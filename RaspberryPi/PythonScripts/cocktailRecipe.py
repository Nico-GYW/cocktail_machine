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