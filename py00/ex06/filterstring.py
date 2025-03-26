import sys
import string


def main():
    if len(sys.argv) != 3:
        print('AssertionError: the arguments are bad')
        exit(1)

    try:
        limit = int(sys.argv[2])
        if any(char in string.punctuation for char in sys.argv[1]):
            raise Exception()
        if any(char not in string.printable for char in sys.argv[1]):
            raise Exception()
    except Exception:
        print('AssertionError: the arguments are bad')
        exit(1)

    words = sys.argv[1].split(' ')
    filtered_words = [w for w in words if (lambda x: len(x) > limit)(w)]

    print(filtered_words)


if __name__ == '__main__':
    main()
