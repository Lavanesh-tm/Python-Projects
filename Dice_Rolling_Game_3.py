import random

total=0
while True:
    dice = input("Roll the dice? Enter Y or N: ")
    if dice.lower() == "y":
        total+=1
        t = int(input("How many dice do you want to roll? "))
        m1 = [random.randint(1,6) for _ in range(t)]
        print(f"You rolled: {', '.join(map(str, m1))}")
    
    elif dice.lower() == "n":
        print("Thank you!")
        break
    
    else:
        print("Bye!")
        break
print(f"Total of {total} times the dice rolled");

