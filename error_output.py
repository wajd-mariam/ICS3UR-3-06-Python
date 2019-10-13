# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program gives more output whenever their is wrong input

import random


def main():

    random_number = random.randint(1, 10)

    # input
    guess = input("Can you guess the number the computer chose from 0 to 10?:")

    # process and output
    try:
        integer_as_int = int(guess)
        if random_number == integer_as_int:
            print("You guessed it :)")
        else:
            print("The correct number was {}".format(random_number))
    except Exception:
        print("This was not a valid entry")
    finally:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
