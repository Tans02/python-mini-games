import random

while True:  # outer loop for restarting the game
    count = 1
    computer = random.randint(1, 100)

    while True:  # inner loop for guessing
        try:
            user = int(input("Choose a number from 1 to 100: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if user > 100 or user < 1:
            print("Invalid input, try from 1 to 100.")
            continue

        if computer > user:
            print("Too low")
        elif computer < user:
            print("Too high")
        else:
            print(f"Correct! 🎯 You guessed it in {count} attempts.")
            break  # exits inner loop

        count += 1

    play_again = input("\nDo you want to play again? (yes/no)_").lower()
    if play_again!='yes':
        print('thanks for playing!")
        break
