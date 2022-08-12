print("\t\t\tWellcome to Vending Machine".upper())

stock1 = 1000
# product and items are stored
items = [{'code': 1, 'category': 'ice_cream', 'name': ['mango', 'pista', 'orange', 'rainbow', 'vanilla'], 'qty': 40},
         {'code': 2, 'category': 'chocolates', 'name': ['dairy milk', 'perk', 'kitkat', 'twix', 'mars'], 'qty': 40},
         {'code': 3, 'category': "chips", 'name': ['lays', 'kurkure', 'asli baba', 'kurleez', 'wavy'], 'qty': 40},
         {'code': 4, 'category': 'coldrink', 'name': ['pepsi', 'marinda', '7up', 'deo', 'sprite'], 'qty': 40},
         {'code': 5, 'category': 'juice', 'name': ['slice', 'apple', 'red grapes', 'chounsa', 'orange'], 'qty': 40}
         ]

item = ''
while True:
    print(" '1' for ice cream", " '2' for chocolates", "'3' for chips", "'4' for colddrink", " '5' for juices")

    choice = int(input("Please Select Code for Buy "))
    for i in items:
        if choice == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
        continue
    else:
        print(f"Great, {item['category']} products are {item['name']} and each have quantity of {item['qty']} items")
        item_flavor = input(f"Which {item['category']}  do you want to buy? ")
        if item_flavor in item['name']:
            print(f"Thank you for buying {item_flavor} {item['category']} ")
        user_qty = int(input("Enter Quantity to buy: "))
        if 0 < user_qty <= 40:
            print(f"You got {item_flavor} {item['category']} and quantity is {user_qty}")
            ext = input("\nWant to buy Another -- Press 'Y' or Press any key to Exit ")
            if ext == 'y':
                pass
            else:
                break
        else:
            print("\nSorry ! Machine has only 40 items each ")
            continue
        break
