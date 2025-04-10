import sys


def is_int_convertible(string: str) -> bool:
    """Checks if a string can be converted to an integer."""
    try:
        int(string)
        return True
    except Exception:
        return False


if len(sys.argv) == 1:
    exit(1)

try:
    assert len(sys.argv) == 2, "more than one argument is provided"
except Exception as e:
    print(f"{type(e).__name__}: {e}")
    exit(1)

try:
    assert is_int_convertible(sys.argv[1]), "argument is not an integer"
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except Exception as e:
    print(f"{type(e).__name__}: {e}")
    exit(1)

# TESTER
# #!/bin/bash
#
# echo -e "\npython whatis.py 14"
# python whatis.py 14
#
# echo -e "\npython whatis.py -5"
# python whatis.py -5
#
# echo -e "\npython whatis.py"
# python whatis.py
#
# echo -e "\npython whatis.py Hi!"
# python whatis.py Hi!
#
# echo -e "\npython whatis.py 13 5"
# python whatis.py 13 5
########
