import datetime

class Item():

    def __init__(self, sku, name, price, taxable):
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

    def print_item(self):
        print(self.name + ("." * 36) + " $" + str(self.price) + str(self.taxable))


class Order():
    def __init__(self, items, order_number, purchase_date):
        self.items = []
        t = datetime.datetime.now()

    def add_item(self, i : Item):
        self.items.append(i)

    

x = Item (1, "bread", 5, True)

x.print_item()