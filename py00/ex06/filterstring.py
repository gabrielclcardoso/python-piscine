import sys


def is_punctuation(c: str) -> bool:
    """Checks if a string is composed of punctuation chars"""

    if not (c.isupper() or c.islower() or c.isspace()
            or c.isdecimal()):
        return True
    return False


def is_int_convertible(string: str) -> bool:
    """Checks if a string can be converted to an integer."""

    try:
        int(string)
        return True
    except Exception:
        return False


def main():
    E_STR = "the arguments are bad"

    try:
        assert len(sys.argv) == 3, E_STR
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)

    try:
        assert is_int_convertible(sys.argv[2]), E_STR
        assert all(c.isprintable() for c in sys.argv[1]), E_STR
        assert all(not is_punctuation(c) for c in sys.argv[1]), E_STR
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)

    limit = int(sys.argv[2])
    words = sys.argv[1].split(' ')
    filtered_words = [w for w in words if (lambda x: len(x) > limit)(w)]

    print(filtered_words)


if __name__ == '__main__':
    main()
