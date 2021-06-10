# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2,supperExceptions=True):
    pass


def main():
    # try to call the function without the keyword
    myFunction(1, 2, True)


if __name__ == "__main__":
    main()
