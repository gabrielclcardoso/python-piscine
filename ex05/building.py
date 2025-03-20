import sys
import string


def main():
    text = ""

    if len(sys.argv) == 1:
        text = get_text()
    elif len(sys.argv) > 2:
        return 1
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
        if i in string.ascii_uppercase:
            counts['ucl'] += 1
        elif i in string.ascii_lowercase:
            counts['lcl'] += 1
        elif i in string.punctuation:
            counts['pm'] += 1
        elif i.isspace():
            counts['s'] += 1
        elif i in string.digits:
            counts['d'] += 1

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
