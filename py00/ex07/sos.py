import sys


def main():
    E_STR = "the arguments are bad"
    NESTED_MORSE = {
        ' ': '/ ', 'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
        'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ',
        'J': '.--- ', 'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ',
        'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ',
        'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ', '1': '.---- ', '2': '..--- ',
        '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ',
        '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ',
    }

    try:
        assert len(sys.argv) == 2, E_STR
        assert all(c.upper() in NESTED_MORSE.keys()
                   for c in sys.argv[1]), E_STR
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)

    morse = "".join((NESTED_MORSE[c.upper()] for c in sys.argv[1]))

    print(morse.rstrip())


if __name__ == "__main__":
    main()
