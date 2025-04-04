import math


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Docstring"""

    performed_operations = []

    for k, val in kwargs.items():
        if val in performed_operations:
            print("ERROR")
        elif val == "mean":
            print(get_mean(args))
            performed_operations.append(val)
        elif val == "median":
            print(get_median(args))
            performed_operations.append(val)
        elif val == "quartile":
            print(get_quartile(args))
            performed_operations.append(val)
        elif val == "std":
            print(get_std(args))
            performed_operations.append(val)
        elif val == "var":
            print(get_var(args))
            performed_operations.append(val)


def get_mean(iter) -> int | float | str:
    """Returns the mean"""

    try:
        return sum(iter)/len(iter)
    except Exception:
        return "ERROR"


def get_median(iter) -> int | float | str:
    """Returns the median"""

    try:
        lst = sorted(iter)
        length = len(lst)
        if length % 2 == 0:
            return (lst[int(length / 2)] + lst[(int(length / 2)) - 1]) / 2
        else:
            return lst[int(length / 2)]
    except Exception:
        return "ERROR"


def get_quartile(iter) -> list | str:
    """Returns quartiles 25% and 75% in a list"""

    try:
        lst = sorted(iter)
        quarter = (len(lst) + 1) / 4

        if quarter - int(quarter) != 0:
            simple = True
            quarter = int(quarter)
        else:
            simple = False

        if simple:
            return [float(lst[quarter]), float(lst[-(quarter + 1)])]
        else:
            q1 = (lst[int(quarter)] + lst[int(quarter) + 1]) / 2
            q2 = (lst[-int(quarter)] + lst[-int(quarter) + 1]) / 2
            return [float(q1), float(q2)]
    except Exception:
        return "ERROR"


def get_var(iter) -> float | str:
    """Returns variance"""

    try:
        mean = sum(iter) / len(iter)
        return sum((i - mean) ** 2 for i in iter) / len(iter)
    except Exception:
        return "ERROR"


def get_std(iter) -> float | str:
    """Returns quartiles 25% and 75% in string form"""

    try:
        var = get_var(iter)
        return math.sqrt(var)
    except Exception:
        return "ERROR"


# def main():
#     ft_statistics(1, 42, 360, 11, 64,
#                   toto="mean", tutu="median", tata="quartile")
#     print("-----")
#
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
#     print("-----")
#
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#                   ejfhhe="heheh", ejdjdejn="kdekem")
#     print("-----")
#
#     ft_statistics(toto="mean", tutu="median", tata="quartile")
#
#
# if __name__ == "__main__":
#     main()
