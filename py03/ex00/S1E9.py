from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for representing a character"""

    @abstractmethod
    def die(self):
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


# def main():
#     Ned = Stark("Ned")
#     print(Ned.__dict__)
#     print(Ned.is_alive)
#     Ned.die()
#     print(Ned.is_alive)
#     print(Ned.__doc__)
#     print(Ned.__init__.__doc__)
#     print(Ned.die.__doc__)
#     print("---")
#     Lyanna = Stark("Lyanna", False)
#     print(Lyanna.__dict__)
#     print()
#
#     try:
#         hodor = Character("hodor")
#         print(hodor)
#     except Exception as e:
#         print(f"Error: {e}")
#
#
# if __name__ == "__main__":
#     main()
