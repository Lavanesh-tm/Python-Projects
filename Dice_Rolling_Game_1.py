import random;

#loop
dice=input("Roll the dice? Enter Y or N:");
if dice.lower() =="y":
 dice_1=random.randint(1,6);
 dice_2=random.randint(1,6);
 print(f"You rolled: {dice_1} and {dice_2}")
elif(dice.lower()=="n"):
 print("Thank you!");
 break;
else:
    print("Bye!");
