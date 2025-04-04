def slice_me(family: list, start: int, end: int) -> list:
    """Receives a 2D array and returns a sliced version of it. An empty list is
    returned in the case of an error"""

    if not is_2d_array(family):
        return []
    elif not isinstance(start, int) or not isinstance(end, int):
        print("Error: expected int values for start and end variables")
        return []

    sliced = family[start:end]
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(sliced)}, {len(sliced[0])})")

    return sliced


def is_2d_array(arr: list) -> bool:
    """Checks if the list is processable by the slice_me function"""

    if not isinstance(arr, list):
        print("Error: argument received is not a list")
        return False
    elif len(arr) == 0:
        print("Error: received empty list")
        return False
    elif not isinstance(arr[0], list):
        print("Error: argument received is not a list of lists")
        return False
    elif len(arr[0]) == 0:
        print("Error: empty list inside of list")
        return False
    elif any(len(i) != len(arr[0]) for i in arr):
        print("Error: lists are of different sizes")
        return False

    return True


# def main():
#     family = [[1.80, 78.4],
#               [2.15, 102.7],
#               [2.10, 98.5],
#               [1.88, 75.2]]
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))
#
#     print()
#     error = [[]]
#     slice_me(error, 0, 0)
#     error = []
#     slice_me(error, 0, 0)
#     error = [[1], [2, 3]]
#     slice_me(error, 0, 0)
#     error = [1, 2]
#     slice_me(error, 0, 0)
#     error = 42
#     slice_me(error, 0, 0)
#     slice_me(family, 'a', 0)
#     slice_me(family, 0, 'a')
#
#
# if __name__ == "__main__":
#     main()
