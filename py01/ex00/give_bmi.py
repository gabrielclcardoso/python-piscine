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
    elif any(not isinstance(i, float | int) for i in l1) or any(
            not isinstance(i, float | int) for i in l2):
        print("Error: list does not contain float or int")
        return False
    return True


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Given lists of BMI indices and a limit, the function will return a list
    of booleans with True for those above the limit. If an error occurs or the
    list is empy it returns an empty list
    """

    if not list_is_valid(bmi):
        return []
    else:
        return [i > limit for i in bmi]


def list_is_valid(lst: list[int | float]) -> bool:
    """Given a list, checks if it is processable by the apply_limit function"""

    if not isinstance(lst, list):
        print("Error: Arguments is not a list")
        return False
    elif len(lst) == 0:
        return False
    elif not isinstance(lst[0], int | float):
        print("Error: list does not contain float or int")
        return False
    return True


# def main():
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))
#     print()
#
#     height = [2.71, "error"]
#     weight = [165.3, "iminent"]
#
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))
#     print()
#
#     bmi = give_bmi([], [])
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))
#     print()
#
#     fake = ['a', 'b']
#     bmi = give_bmi(fake, height)
#     print()
#
#     bmi = give_bmi(None, height)
#     print()
#
#     bmi = give_bmi(height, None)
#     print()
#
#     print(apply_limit(bmi, 26))
#
#
# if __name__ == "__main__":
#     main()
