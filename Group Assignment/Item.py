
class Item:


    def __init__(self, sku, name, price : float, taxable) :

        self.name = name
        self.price = price
        self.taxable = taxable
        self.sku = sku


    def is_taxable(self):
        if self.taxable == True:
            return "T"

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

        self.item_description = ("{} {} ${:0,.2f} {} {}".format(self.name,
                                                                ("." * (20 - len(self.name))),
                                                                self.price,
                                                                (" " * (7 - len(str(self.price)))),
                                                                "T" * (self.taxable)))
        return self.item_description
