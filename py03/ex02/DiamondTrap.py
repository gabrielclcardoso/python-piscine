from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Fake king class"""

    def __init__(self, name: str, is_alive: bool = True):
        """Initializes fake king"""
        super().__init__(name, is_alive)

    def set_eyes(self, color: str):
        """Set new eye color"""

        self.eyes = color

    def set_hairs(self, color: str):
        """Set new hair color"""

        self.hairs = color

    def get_eyes(self):
        """Returns eye color"""

        return self.eyes

    def get_hairs(self):
        """Returns hair color"""

        return self.hairs


# def main():
#     Joffrey = King("Joffrey")
#     print(Joffrey.__dict__)
#     Joffrey.set_eyes("blue")
#     Joffrey.set_hairs("light")
#     print(Joffrey.get_eyes())
#     print(Joffrey.get_hairs())
#     print(Joffrey.__dict__)
#
#
# if __name__ == "__main__":
#     main()
