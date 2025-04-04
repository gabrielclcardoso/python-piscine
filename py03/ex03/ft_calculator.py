class calculator:
    def __init__(self, lst: list):
        """Creates a calculator holding a copy of the array"""
        self.lst = lst.copy()

    def __str__(self):
        return str(self.lst)

    def __add__(self, object) -> None:
        self.lst = [i + object for i in self.lst]
        print(self.lst)

    def __mul__(self, object) -> None:
        self.lst = [i * object for i in self.lst]
        print(self.lst)

    def __sub__(self, object) -> None:
        self.lst = [i - object for i in self.lst]
        print(self.lst)

    def __truediv__(self, object) -> None:
        try:
            self.lst = [i / object for i in self.lst]
        except Exception as e:
            print(f"Error: {e}")
            return
        print(self.lst)


# def main():
#     v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v1 + 5
#     print("---")
#     v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v2 * 5
#     print("---")
#     v3 = calculator([10.0, 15.0, 20.0])
#     v3 - 5
#     v3 / 5
#     v4 = calculator([10.0, 15.0, 20.0])
#     v4 / 0
#
#
# if __name__ == "__main__":
#     main()
