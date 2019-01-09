import datetime

class Item():


    def __init__(self, sku, name, price : float, taxable) :

        self.name = name
        self.price = price
        self.taxable = taxable
        self.sku = sku


    def is_taxable(self):

         return self.taxable

    def get_item_base_price(self):
        return self.price

    def calculate_qst(self):
        if self.taxable:
            return self.price * 0.09975
        else:
            return 0

    def calculate_gst(self):
        if self.taxable:
            return self.price * 0.05
        else:
            return 0

    def get_total_price(self):
        return self.price + self.calculate_qst() + self.calculate_gst()

    def print_item(self, width):
        print(self.name + ("." * width) + " $" + str(self.price) + str(self.taxable))



class Order():
    last_orderno_used = 0

    purchase_date = datetime.datetime.now()
    def __init__(self):
        self.orderno = Order.last_orderno_used + 1
        self.items = []
        #count += 1
        self.purchase_date = datetime.datetime.now()
        #self.order_number = count
        Order.last_orderno_used = self.orderno

    def add_item(self, i : Item):
        self.items.append(i)

    #def remove_item(self):

    def get_item_count(self):
        return len(self.items)

    def get_total_gst(self):
        total_gst_price = 0
        for item in self.items:
            total_gst_price += item.calculate_gst()
        return total_gst_price

    def get_total_qst(self):
        total_pst_price = 0
        for item in self.items:
            total_pst_price += item.calculate_qst()
        return total_pst_price


    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += float(item.get_item_base_price())
        return total_price

    def print_items(self, width):
        width = 0
        for item in self.items:
            item.print_item(width)

    def generate_receipt(self, width):
        print("Order Number : " + str(self.orderno))
        #print("Item" + " " * 16 + "Price %5s" % "Tax?")
        #print("-" * 31)
        for item in self.items:
            print(item.print_item(36))
        subtotal = self.get_total_price()
        total_gst = self.get_total_gst()
        total_pst = self.get_total_qst()

        total = subtotal + total_gst + total_pst


#x = Item (1, "bread", 5, True)

#x.print_item()
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
