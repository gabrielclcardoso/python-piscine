import sys


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        exit(1)

    morse_code = {
        ' ': '/ ', 'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ',
        'e': '. ', 'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ',
        'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ',
        'o': '--- ', 'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ',
        't': '- ', 'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ',
        'y': '-.-- ', 'z': '--.. ', '1': '.---- ', '2': '..--- ',
        '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ',
        '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ',
    }

    if any(char.lower() not in morse_code.keys() for char in sys.argv[1]):
        print("AssertionError: the arguments are bad")
        exit(1)
    else:
        morse = "".join((morse_code[char.lower()] for char in sys.argv[1]))
    print(morse.rstrip())


if __name__ == "__main__":
    main()
