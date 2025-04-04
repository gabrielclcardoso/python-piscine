from S1E9 import Character


class Baratheon(Character):
    """Class representing the Baratheon family"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Calls base class init"""
        super().__init__(first_name, is_alive)

        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kills character"""

        self.is_alive = False

    def __str__(self):
        """String representation"""
        return f'{self.family_name}, {self.first_name}'

    def __repr__(self):
        """Object representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Class representing the Lanister family"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Calls base class init"""
        super().__init__(first_name, is_alive)

        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kills character"""

        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        return cls(first_name, is_alive)

    def __str__(self):
        """String representation"""
        return f'{self.family_name}, {self.first_name}'

    def __repr__(self):
        """Object representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
