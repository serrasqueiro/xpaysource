# debug.py  (c)2021  Henrique Moreira

"""
Only debug functions
"""
# pylint: disable=missing-function-docstring, global-statement

DEBUG = 0

def bprint(*args) -> bool:
    if DEBUG <= 0:
        return False
    print(*args)
    return True

def set_debug(new_level: int):
    global DEBUG
    DEBUG = int(new_level)


# Only a module
if __name__ == "__main__":
    print("This is a module.")
    print()
    print("from payments.debug import bprint !")
