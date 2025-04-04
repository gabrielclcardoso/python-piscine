class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints dot product between vectors"""

        print(f"Dot product is: {sum(float(i * j) for i, j in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Prints addition between vectors"""

        print(f"Add vector is: {[float(i + j) for i, j in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Prints subtracion between vectors"""

        print(f"Sous Vector is: {[float(i - j) for i, j in zip(V1, V2)]}")


# def main():
#     a = [5, 10, 2]
#     b = [2, 4, 3]
#     calculator.dotproduct(a, b)
#     calculator.add_vec(a, b)
#     calculator.sous_vec(a, b)
#
#
# if __name__ == "__main__":
#     main()
