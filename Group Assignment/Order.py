from Item import Item
import datetime
class Order:
    last_orderno_used = 0

    purchase_date = datetime.datetime.now()
    def __init__(self):
        self.orderno = Order.last_orderno_used + 1
        self.items = []

        self.purchase_date = datetime.datetime.now()

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

        for item in self.items:
            item.print_item(width)

    def generate_receipt(self, width):
        print("Order Number : " + str(self.orderno))
        print("Order Date : " + str(self.purchase_date.strftime("%Y-%m-%d %I:%M%p").lower()))

        for item in self.items:
            print(item.print_item(36))
        subtotal = self.get_total_price()
        total_gst = self.get_total_gst()
        total_qst = self.get_total_qst()
        total = subtotal + total_gst + total_qst

        print("Sub Total : $ {:0.2f}".format(float(subtotal)))
        print("Total GST : $ {:0.2f}".format(float(total_gst)))
        print("Total QST : $ {:0.2f}".format(float(total_qst)))
        print("Grand Total : $ {:0.2f}".format(float(subtotal)))