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

    def __init__(self, bottles):
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

    def get_by_name(self, name):
        # Check if the name exists in the dictionary
        if name in self.bottle_names:
            # If it does, return the first value for that key
            return self.bottle_names[name][0]
        else:
            # If it doesn't, return None or any appropriate value
            return None


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
    def from_dict(cls, state):
        """
        Create a BottleHolder instance from a dictionary.

        Args:
            state (dict): The dictionary containing the state of the BottleHolder.

        Returns:
            BottleHolder: The created BottleHolder instance.
        """
        bottles = [Bottle(**bottle_dict) for bottle_dict in state["bottles"]]
        return cls(bottles)

    def to_dict(self):
        """
        Convert the current state of the BottleHolder to a dictionary.

        Returns:
            dict: The dictionary representing the state of the BottleHolder.
        """
        return {
            "bottles": [bottle.to_dict() for bottle in self.bottles]
        }