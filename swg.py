import random

choices=['snake','water','gun']


while True:
    user=input("Choose snake,water,gun or exit: ").lower()
    if user=='exit':
        print("the game ended")
        break
        
    elif user not in choices:
        print("invalid input")
        continue

    computer=random.choice(choices)
    print("computer chose",computer)

    if computer==user:
        print("Its a tie")
        
    elif ((user=='snake' and computer=='water') or (user=='water' and computer=='gun') or (user=='gun' and computer=='snake')):
        print("You win")
    else:
        print("You lose")

    
