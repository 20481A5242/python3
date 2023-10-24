import time

def delay_print(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def game_over():
    delay_print("Game Over. Would you like to play again? (yes/no)")
    return input().lower().strip() == 'yes'

def adventure_game():
    delay_print("Welcome to the Text-Based Adventure Game!")
    delay_print("You find yourself in a mysterious forest. Your goal is to find a hidden treasure.")

    while True:
        delay_print("You come across a fork in the path. Which way do you choose?")
        delay_print("1. Take the left path.")
        delay_print("2. Take the right path.")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            delay_print("You chose the left path.")
            left_path()
            break
        elif choice == '2':
            delay_print("You chose the right path.")
            right_path()
            break
        else:
            delay_print("Invalid choice. Please enter 1 or 2.")

def left_path():
    delay_print("You follow the left path and discover a hidden cave.")
    delay_print("Inside the cave, you find a sleeping dragon guarding a treasure chest.")

    while True:
        delay_print("What will you do?")
        delay_print("1. Try to sneak past the dragon.")
        delay_print("2. Attempt to wake up the dragon.")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            delay_print("You successfully sneak past the dragon and obtain the treasure!")
            win()
            break
        elif choice == '2':
            delay_print("Your attempt to wake the dragon fails, and it breathes fire on you. You're burned to a crisp.")
            if game_over():
                adventure_game()
            else:
                exit()
        else:
            delay_print("Invalid choice. Please enter 1 or 2.")

def right_path():
    delay_print("You follow the right path and encounter a group of friendly forest creatures.")
    delay_print("They offer to help you find the treasure.")

    while True:
        delay_print("What will you do?")
        delay_print("1. Accept their help.")
        delay_print("2. Decline their help and continue on your own.")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            delay_print("The forest creatures guide you to the treasure, and you find it together.")
            win()
            break
        elif choice == '2':
            delay_print("You decide to continue on your own but get lost in the forest.")
            if game_over():
                adventure_game()
            else:
                exit()
        else:
            delay_print("Invalid choice. Please enter 1 or 2.")

def win():
    delay_print("Congratulations! You've found the hidden treasure.")
    delay_print("You've successfully completed your adventure!")
    if game_over():
        adventure_game()
    else:
        exit()

if __name__ == "__main__":
    adventure_game()
