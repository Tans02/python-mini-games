import random
option=['even',"odd"]

while True:
    try:
        user=int(input("enter a number between 1  to 50: "))
    except ValueError:
        print("invalid input, please enter numbers bw 1 to 50")
        continue
  
    if user>50 or user<1:
        print("choose between 1 to 50")
        continue
   
    while True:
        guess=input(f"Guess ({option[0]}/{option[1]}): ").lower()
        if guess in option:
            break
        print("invalid guess, type even or odd")
            
    
    comp=random.randint(1,50)

    plus=(comp+user)
    print(f"computer chose {comp}, the sum is {plus}")

    if plus%2==0:
        print("that is even")
        result='even'
    else:
        print("that is odd")  
        result='odd'
    
    if guess==result:
        print("you guessed that right!")
    else:
        print("wrong guess!")  
          
    playagain=input("want to play again? type (yes/no)_")
    if playagain!='yes':
        print("thanks bye")
        break



