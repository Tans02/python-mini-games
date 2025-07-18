import random

emoji = {
    "stone": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}
choices=["stone","scissor","paper"]

rounds=3
user_score=0
computer_score=0
round_number=1

while round_number<=rounds:
    user=input("Choose from Stone,Paper,Scissor or type exit or quit to end the game: ").lower()
    if user=="exit" or user=="quit":
        break
    if user not in choices:
        print("Invalid input,Retry")
        continue
    
    computer=random.choice(choices)
    print("Computer chose for: ",emoji[computer])
    print("you chose",emoji[computer])

    if user==computer:
        print("Its a tie!")
    elif ((computer=='paper' and user=='stone') or(computer=='stone' and user=='scissor') or (computer=='scissor' and user=='paper') ):
        print("You lose")
        computer_score+=1
    else:
        print("You win")
        user_score+=1
    round_number += 1


print("Game Over!")
print(f"Your score {user_score}")
print(f"Computers Score {computer_score}")

if user_score>computer_score:
    print("You win,Woohoo")
elif user_score==computer_score:
    print("Its a tie")
else:
    print("Umm...You lose")
        
