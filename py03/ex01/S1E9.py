from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for representing a character"""

    @abstractmethod
    def die(self):
        """Abstract method to ensure every character can die"""
        pass

    def __init__(self, first_name: str, is_alive: bool = True):
        """Creates characters and asigns its name and status"""

        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """Class representing Stark characters from GOT"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Calls base class init"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kills character"""

        if self.is_alive:
            self.is_alive = False
