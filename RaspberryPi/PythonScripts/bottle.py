class Bottle:
    """
    Represents a bottle with a name, quantity, and position in the holder.

    Attributes:
        name (str): The name of the bottle.
        quantity (int): The quantity of liquid in the bottle.
        position (int): The position of the bottle in the holder.
    """

    def __init__(self, name, quantity, position):
        """
        Initialize a Bottle instance.

        Args:
            name (str): The name of the bottle.
            quantity (int): The quantity of liquid in the bottle.
            position (int): The position of the bottle in the holder.
        """
        self.name = name
        self.quantity = max(quantity, 0)  # ensure quantity is never less than 0
        self.position = position

    def decrease_quantity(self, quantity):
        """
        Decrease the quantity of liquid in the bottle by the specified amount.

        Args:
            quantity (int): The amount to decrease the quantity by.
        """
        self.quantity = max(self.quantity - quantity, 0)  # ensure quantity is never less than 0

    def __repr__(self):
        """
        Return a string representation of the Bottle instance.

        Returns:
            str: The string representation of the Bottle instance.
        """
        return f"Bottle(name={self.name}, quantity={self.quantity}, position={self.position})"

    def to_dict(self):
        """
        Convert the current state of the Bottle to a dictionary.

        Returns:
            dict: The dictionary representing the state of the Bottle.
        """
        return {
            "name": self.name,
            "quantity": self.quantity,
            "position": self.position,
        }


class BottleHolder:
    """
    Represents a holder for multiple bottles.

    Attributes:
        bottles (list): The list of bottles in the holder.
        bottle_names (dict): A dictionary mapping bottle names to a list of positions.
    """

    def __init__(self, bottles, position_mapping):
        """
        Initialize a BottleHolder instance.

        Args:
            bottles (list): The list of bottles in the holder.
        """
        self.bottles = sorted(bottles, key=lambda bottle: bottle.position)  # Sorted list of bottles
        self.bottle_names = {}  # Initialize an empty dictionary
        for bottle in bottles:  # Fill the dictionary with the correct positions
            if bottle.name not in self.bottle_names:
                self.bottle_names[bottle.name] = []
            self.bottle_names[bottle.name].append(bottle.position - 1)
        
        self.position_mapping = position_mapping
        #  fixed positions (X, Y) for each bottle position index

    def get(self, name):
        """
        Get a list of bottles with the specified name.

        Args:
            name (str): The name of the bottle to retrieve.

        Returns:
            list or None: A list of bottles with the specified name, or None if no bottles found.
        """
        indices = self.bottle_names.get(name, [])
        return [self.bottles[i] for i in indices] if indices else None

    def get_bottles(self):
        return self.bottles

    def __repr__(self):
        """
        Return a string representation of the BottleHolder instance.

        Returns:
            str: The string representation of the BottleHolder instance.
        """
        return f"BottleHolder(bottles={self.bottles})"

    def get_by_position(self, position):
        """
        Get the bottle at the specified position.

        Args:
            position (int): The position of the bottle to retrieve.

        Returns:
            Bottle or None: The bottle at the specified position, or None if no bottle found.
        """
        return self.bottles[position - 1] if 0 < position <= len(self.bottles) else None

    def get_position_by_ingredient(self, ingredient, required_quantity):
        """
        Find bottle positions and quantities to use for the required amount of the ingredient.
        
        Args:
            ingredient (str): The name of the ingredient.
            required_quantity (int): The required quantity of the ingredient.
        
        Returns:
            list: A list of tuples, each containing the bottle's (X, Y) position and the quantity to use from that bottle.
        """
        if ingredient not in self.bottle_names:
            return []  # L'ingrédient n'est pas trouvé
        
        total_quantity = 0
        bottles_to_fetch = []

        for position_index in self.bottle_names[ingredient]:
            if total_quantity >= required_quantity:
                break  # La quantité requise est atteinte
            
            print(position_index)
            bottle = self.bottles[position_index]
            available_quantity = bottle.quantity
            quantity_to_use = min(available_quantity, required_quantity - total_quantity)
            total_quantity += quantity_to_use
            
            print(self.position_mapping)
            position_xy = self.position_mapping[position_index]
            bottles_to_fetch.append((bottle.position, position_xy, quantity_to_use))
            
            if total_quantity >= required_quantity:
                break

        if total_quantity < required_quantity:
            return []  # Quantité insuffisant

        return bottles_to_fetch

    def update_bottle(self, bottle):
        """
        Update a bottle in the holder with a new bottle.

        Args:
            bottle (Bottle): The new bottle to update.

        Raises:
            ValueError: If there is no bottle at the specified position.
        """
        position = bottle.position - 1
        if not (0 <= position < len(self.bottles)):
            raise ValueError(f"No bottle at position {bottle.position}.")
        old_name = self.bottles[position].name
        self.bottles[position] = bottle
        self.bottle_names[old_name].remove(position)
        if not self.bottle_names[old_name]:
            del self.bottle_names[old_name]
        if bottle.name not in self.bottle_names:
            self.bottle_names[bottle.name] = []
        self.bottle_names[bottle.name].append(position)

    @classmethod
    def from_dict(cls, state, position_mapping=None):
        """
        Create a BottleHolder instance from a dictionary.

        Args:
            state (dict): The dictionary containing the state of the BottleHolder.
            position_mapping (list): Optional. The position mapping for the bottles.

        Returns:
            BottleHolder: The created BottleHolder instance.
        """
        bottles = [Bottle(**bottle_dict) for bottle_dict in state["bottles"]]
        if position_mapping is None:
            raise ValueError("position_mapping is required")
        return cls(bottles, position_mapping)

    def to_dict(self):
        """
        Convert the current state of the BottleHolder to a dictionary.

        Returns:
            dict: The dictionary representing the state of the BottleHolder.
        """
        return {
            "bottles": [bottle.to_dict() for bottle in self.bottles]
        }