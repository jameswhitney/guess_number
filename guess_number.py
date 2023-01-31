#!/usr/bin/env python


import random


# Create Guessing Game class that creates a random number
# between 0 and 10. Check if user input is equal to the
# random number. If not continue to ask user for a number
# until the input is equal to the randomly generated number.


class GuessingGame():

    # Create an __init__ method which will generate a random number upon instantiation of class
    def __init__(self):
        self.rand_num = random.randint(0, 20)
        print('\nInitial random number = {}'.format(self.rand_num))

    # Create class method to reset the __init__ method's random number with a new random number
    def reset_num(self):
        self.rand_num = random.randint(0, 20)
        print('\nNew number after reset = {}\n'.format(self.rand_num))

    # Create a class method that takes user input and compares it to the randomly generated number.
    # If the number entered does not equal the random number, ask user to input another number,
    # and let the user know if the correct number is higher or lower than randomly generated number.
    # Repeate this process until user enters a number equal to the randomly generated number.
    def guess(self):

        while True:

            try:
                user_guess = int(input('Please enter a number between 0 and 20: '))

            except ValueError:
                print('\nPlease enter whole numbers only. Please try again.\n')
                continue
            
            if user_guess == self.rand_num:
                print('\nHuzzah {} is the magic number'.format(self.rand_num))
                break

            elif user_guess < self.rand_num:
                print('Sorry you guessed incorrectly, try a higher number\n')
                continue

            else:
                print('\nSorry you guessed incorrectly, try a lower number\n')
                continue
            


# Create simple test function for the GuessingGame class

def test():
    g = GuessingGame()
    g.reset_num()
    g.guess()

test()

