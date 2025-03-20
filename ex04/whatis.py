import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    exit(1)
elif len(sys.argv) == 1:
    exit(1)

try:
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except Exception:
    print("AssertionError: argument is not an integer")
    exit(1)
