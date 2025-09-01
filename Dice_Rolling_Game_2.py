#Modify the program so the user can specify how many dice they want to roll


import random

while True:
    dice = input("Roll the dice? Enter Y or N: ")
    
    if dice.lower() == "y":
        t = int(input("How many dice do you want to roll? "))
        m1=[0 for i in range(t)]
        for i in range(len(m1)):
            m1[i]=random.randint(1,6)
        print(f"You rolled: {m1}")
    
    elif dice.lower() == "n":
        print("Thank you!")
        break
    
    else:
        print("Bye!")
        break

