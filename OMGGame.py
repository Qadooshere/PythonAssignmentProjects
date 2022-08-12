# Imported Random
import random

print("\t\tWellcome to OMG Game ".upper())

# Added some info about Who are you
who = ["Don't forget you are King", "you are Millionaire by heart", "You are cute", "The beast, strong and mighty",
       "You are Sharp"]
# added Data for the color of your personality in List
color = ["Grey", "Gold", "Pink", "Brown", 'Yellow']
color_det = ["you are calm, refined and professional", "you are successful, talented, and elegant",
             "you are affectionate, compassionate, and sweet"]

# Make a list and add some info about Know the meaning of Name
name = ["Alone", "You are the protector", "Kind hearted", "Big dreamer", "Hard Worker", 'Coward', 'Strong']
while True:
    # To select an option to play game
    user_choice = int(input("1. Who are You? 2. Know the colour of personality? 3. Know the meaning behind your name?"
                            " \nEnter Your Choice: "))
    if user_choice == 1:
        user_name = input("Enter Your name ")       # User will insert his/her name
        print(user_name, ":", random.choice(who))    # it will display name and Random answer from Who list
        ch = input("Do You want to Play Again, PRESS 'Y' or Press any Key to EXIT ")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break

    if user_choice == 2:
        user_color = input("Enter color of your personality ")
        # it will convert into Title by User input - Color are listed in Title
        user_color = user_color.title()
        if user_color in color:
            print(user_color, ":", random.choice(color_det))
        else:
            while True:
                print("Please select colors from this list", color)
                ch = input("Enter Again Color of your personality ")
                ch = ch.title()
                if ch in color:

                    print(ch, ":", random.choice(color_det))
                    break
                else:
                    pass
        ch = input("Do You want to Play Again, PRESS 'Y' or Press any Key to EXIT ")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break
    if user_choice == 3:
        user_name = input("Enter Your name to know meaning ")
        print(user_name, ":", random.choice(who))
        ch = input("Do You want to Play Again, PRESS 'Y' or Press any Key to EXIT ")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break
