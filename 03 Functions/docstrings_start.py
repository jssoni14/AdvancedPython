# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """myFunction(arg1,arg2=None) --> Doesn't really do anything, just print.
    Parameters:
    arg1: the first argument. Whatever you want to pass.
    arg2: second argument. Defaults to None
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
