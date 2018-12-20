class Item:

    last_sku_used = 0

    def __init__(self, name, price, taxable):
        self.sku = Item.last_sku_used + 1
        self.name = name
        self. price = price
        self.taxable = taxable

        Item.last_sku_used = self.sku

    @staticmethod
    def print_last_sku_used():
        print(Item.last_sku_used)

a1 = Item("first item", 2.00, True)

a2 = Item("Second item", 3.00, False)

print(a1.sku)
print(a2.sku)

Item.print_last_sku_used()