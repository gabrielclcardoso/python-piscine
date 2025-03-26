def lists_are_valid(l1, l2) -> bool:
    """Checks if the lists can be processed by the give_bmi function"""

    if not isinstance(l1, list) or not isinstance(l2, list):
        print("Error: one of the arguments is not a list")
        return False
    elif len(l1) != len(l2):
        print("Error: lists are of diferent sizes")
        return False
    elif len(l1) == 0:
        return True
    elif not isinstance(l1[0], float | int) or not isinstance(
            l2[0], float | int):
        print("Error: list does not contain float or int")
        return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Given lists of height and size of the same length, the function will
    return a list with the BMI index for each pair. If the lists have different
    sizes or are not comprised of int or float the function will print an error
    and return an empty list
    """

    if not lists_are_valid(height, weight) or len(height) == 0:
        return []
    return [(w / (h ** 2)) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    pass


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
