from Item import Item
from Order import Order

Od = Order()
while True:
    sk = str(input("What is the sku of the item to add?"))
    na = str(input("What is the name of the item to add?"))
    co = float(input("How much does the item cost?"))
    while True:
        tx = str(input("Is the item taxable? (Y/N)"))
        if tx == "y" or tx == "Y":
            tx = True
            break
        elif tx == "n" or tx == "N":
            tx = False
            break
        else:
            print ("y or n please!")

    It = Item(sk, na, co, tx)

    Od.add_item(It)
    yn = str(input("Add another item? (Y/N)"))
    if yn == "n" or yn == "N":
        break


Od.generate_receipt(36)
