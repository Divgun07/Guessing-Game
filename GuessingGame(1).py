import random
print("Number Guessing Game")
number = random.randint(1,9)
chances=0
while chances < 5:
    guess=int(input("Enter the number: "))
    if guess == number:
        print("Congratulations! YOU WON!!")
        break
    elif guess<number:
        print("Your number is too low. Assign a higher number")
    else:
        print("Your guess was too high. Assign a lower number")
chances+=1

 
if not chances < 5:
    print("YOU LOSE! The number is: ",number)

