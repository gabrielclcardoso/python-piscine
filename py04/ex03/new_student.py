import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student"""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Method called after init for generating the login"""
        self.login = self.name[0] + self.surname


# def main():
#     student = Student(name="Edward", surname="agle")
#     print(student)
#
#     print("------------------------------------------------------------------")
#     student = Student(name="Edward", surname="agle", id="toto")
#     print(student)
#
#
# if __name__ == "__main__":
#     main()
