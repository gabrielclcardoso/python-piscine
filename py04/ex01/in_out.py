def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count

        if count == 0:
            count = x

        count = function(count)
        return count

    return inner


# def main():
#     my_counter = outer(3, square)
#     print(my_counter())
#     print(my_counter())
#     print(my_counter())
#     print("---")
#     another_counter = outer(1.5, pow)
#     print(another_counter())
#     print(another_counter())
#     print(another_counter())
#
#
# if __name__ == "__main__":
#     main()
