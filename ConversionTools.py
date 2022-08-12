# Convert Weight KG into Pounds
def weight_pound():
    weight = float(input("Enter Your Weight in Kgs "))
    weight = weight * 2.2
    print("Your weight is : ", round(weight, 3), 'pounds')


# Convert Height into inches
def height_inch():
    height = float(input("Enter Your height in feet "))
    height = height * 12
    print("Your height is : ", round(height, 3), 'Inches')


# convert Radian into Degree
def radian_degree():
    pi = 22 / 7  # Value of pi
    radian = float(input("Enter radians value: "))  # i Radian equals to 57.29
    degree = radian * (180 / pi)  # formula for conversion of radian into degree
    print("The value of Degree is: ", degree.__round__(3))


while True:
    user_choice = int(input("What Do you want to Convert? \n 1. KG into Pounds \n 2. Height into inches"
                            " \n 3. Radian into Degree \n Please Select: "))
    if user_choice == 1:
        weight_pound()
        ch = input("Do You want to Convert, PRESS 'Y' or Press any Key to EXIT ")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break
    elif user_choice == 2:
        height_inch()
        ch = input("Do You want to Convert, PRESS 'Y' or Press any Key to EXIT ")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break

    elif user_choice == 3:
        radian_degree()
        ch = input("Do You want to Convert, PRESS 'Y' or Press any Key to EXIT ")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break
    else:
        print("Something went wrong")
