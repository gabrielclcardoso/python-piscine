import sys


def main():
    text = ""

    try:
        assert len(sys.argv) <= 2, "more than one argument are provided"
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)

    if len(sys.argv) == 1:
        text = get_text()
    else:
        text = sys.argv[1]

    count_text(text)


def get_text() -> str:
    """ Reads a line from stdin and returns it """

    print("What is the text to count?")
    text = sys.stdin.readline()
    return text


def count_text(text: str):
    """" Receives a string and prints the following data about it:
    -> Number of characters
    -> Number of upper case letters
    -> Number of lower case letters
    -> Number of punctuation marks
    -> Number of punctuation spaces
    -> Number of digits
    """

    counts = {
        'ucl': 0,
        'lcl':  0,
        'pm': 0,
        's': 0,
        'd': 0
    }

    for i in text:
        if i.isupper():
            counts['ucl'] += 1
        elif i.islower():
            counts['lcl'] += 1
        elif i.isspace():
            counts['s'] += 1
        elif i.isdecimal():
            counts['d'] += 1
        elif i.isprintable():
            counts['pm'] += 1

    print(
        f"""The text contains {len(text)} characters:
{counts['ucl']} upper letters
{counts['lcl']} lower letters
{counts['pm']} punctuation marks
{counts['s']} spaces
{counts['d']} digits"""
    )


if __name__ == '__main__':
    main()
