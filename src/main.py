import os
import sys
import frepl


def main():
    try:
        user = os.getlogin()
        print(f"Hello {user}! This is Fabios programming language.")
    except FileNotFoundError as err:
        print("Error: ", err)
    print("Feel free to type in commands \n")
    frepl.start(sys.stdin, sys.stdout)


if __name__ == "__main__":
    main()
