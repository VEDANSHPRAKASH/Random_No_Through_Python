import random

target=random.randint(1,100)

chance_no = int(input("Enter no.of chance:"))

while (chance_no > 0):
    print(f"You got {chance_no} chance to guess the number:")
    choice_no=input("Enter the number or Quit(Q) the game:")
    if(choice_no == "Q"):
        break
    
    choice_no=int(choice_no)
    if(choice_no == target):
        print("Correct no. is guessed")
        print("You Won!!!!!")
        break
    elif(choice_no<target):
        print("no. is small, enter larger no.")
    else:
        print("no. is big, enter small no.")
    
    chance_no = chance_no - 1

if(chance_no==0 and choice_no!=target):
        print("Sorry!!!!! You Loss!!!!!")
    
print("-----GAME-OVER-----")
