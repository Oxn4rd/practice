import random
import os


minimum_roll = 1
answers = {
    'a': 6,
    'b': 20
}


# Functions

# Clears screen in terminal.
def clear_shell():
    os.system('clear')


# Choosing out of suggested dices.
def choosing_dice():
    print("\nTell me which dice to roll:")
    print("a) 6 sides;")
    print("b) 20 sides;")
    user_answer = input("Enter answer: ")
    while user_answer != 'q':
        if user_answer in answers.keys():
            print("\nIt's settled!")
            print("Let the game begin.")
            return answers[user_answer]
        else:
            print("Well, I don't have such dices :(")
            choosing_dice()


# Rolls the dice.
def roll(minimum_roll, maximum_roll):
    result = random.randint(minimum_roll, maximum_roll)
    return result


# Game loop.
def game(minimum_roll, maximum_roll):
    restart = ''
    while restart != 'n':
        user_throw = roll(minimum_roll, maximum_roll)
        print("\nYou've got " + str(user_throw) + "!")

        tavern_throw = roll(minimum_roll, maximum_roll)
        print("Tavern keeper got " + str(tavern_throw) + "!")

        if user_throw > tavern_throw:
            print("Lucky you! Let me get you a beer.\n")
        elif user_throw < tavern_throw:
            print("Well, now you owe me 300$ ;)\n")
        else:
            print("It's a tie. That's boring.\n")

        restart = input("Wanna play again? (y/n): ")

# Main code
try:
    clear_shell()
    print("Hey there, stranger! You wanna play?")
    maximum_roll = choosing_dice()
    game(minimum_roll, maximum_roll)
    print("k bye.")
except KeyboardInterrupt:
    print("\n...")
    print("\nThat's rude of you, to quit like that.")
