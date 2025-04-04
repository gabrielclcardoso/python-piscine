from collections.abc import Iterable


def ft_filter(function, iterable):
    """Recreation of the built in function filter"""
    if not isinstance(iterable, Iterable):
        print("Error: did not receive iterable")
        return
    if function:
        sequence = [i for i in iterable if function(i)]
    else:
        sequence = [i for i in iterable if i]
    for i in sequence:
        yield i


# def main():
#     l1 = list[1, 2, 3, 4, 5]
#     l2 = list[0, 1, 0, 3, 0, 5, 0, 7, 0, 9]
#     string = " Hello, World! 42 ;)"
#
#     s1 = filter(None, l1)
#     s2 = ft_filter(None, l1)
#     is_same_sequence(s1, s2)
#
#     s1 = filter(None, l2)
#     s2 = ft_filter(None, l2)
#     is_same_sequence(s1, s2)
#
#     s1 = filter(str.isalpha, string)
#     s2 = ft_filter(str.isalpha, string)
#     is_same_sequence(s1, s2)
#
#
# def is_same_sequence(iter1, iter2):
#     for i, j in zip(iter1, iter2):
#         if i != j:
#             print("Test not ok, {i} != {j}")
#     print("Test ok")
#
#
# if __name__ == "__main__":
#     main()
