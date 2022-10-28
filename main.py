
print("Welcome to Treasure Island. \n Your mission is to find the treasure. ")

first_choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n")

if first_choice == 'left':
    second_choice = input("You come to a lake. There is a island in the middle of the lake. Type 'wait' to wait for a "
                          "boat. Type 'swim' to swim across.\n")
    if second_choice == 'wait':
        third_choice = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, "
                             "and one blue. Which color do you choose?\n")
        if third_choice == 'yellow':
            print("You Win!")
        elif third_choice == 'blue':
            print("Game Over!")
        elif third_choice == 'red':
            print("Game Over!")
    else:
        print("Game Over.")

elif first_choice == "right":
    print("Game Over!")





