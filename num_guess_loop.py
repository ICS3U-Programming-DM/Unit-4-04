# Created by Dylan Melo
# Created on Jan 2022
# Program generates a random number and
# tells user if they guessed it right
# if guessed wrong it restarts.

import random


def main():
    # Creating a range to guess between
    # Having the correct number set to random number
    max_num = int(input("Enter the number range: "))
    correct_num = random.randint(1, max_num)
    while True:
        user_number = input("Guess a number between 1 and {}:".format(max_num))

    # Outputting the different possible outcomes
        try:
            user_int = int(user_number)
            if user_int > correct_num:
                print("Your guess is too high. Try again")

            elif user_int < correct_num:
                print("Your guess is too low. Try again")

            elif user_int == correct_num:
                print("You've guessed correctly!")
                break
        except Exception:
            print("Invalid input")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
