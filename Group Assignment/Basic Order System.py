import datetime

class Item():

    def __init__(self, sku, name, price, taxable):
        self.name = name
        self.price = price
        self.taxable = taxable
        self.sku = sku

    def print_item(self):
        print(self.name + ("." * 36) + " $" + str(self.price) + str(self.taxable))

    # def get_item_base_price(self):
    #     return self.price
    #
    # def get_item_tax_price(self):
    #     if self.taxable == "Y":
    #
    #         #return Y/N
    #
    # def get_item_total(self):
    #     #use price and taxable to calculate and return


x = Item (1, "bread", 5, True)

x.print_item()