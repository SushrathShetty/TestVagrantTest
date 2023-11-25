class Product:
    def __init__(self, name, unit_price, gst_per, quantity):
        self.name = name
        self.unit_price = unit_price
        self.gst_per = gst_per
        self.quantity = quantity

    def calculate_total_price(self):
        total_price = self.unit_price * self.quantity
        gst_amount = (total_price * self.gst_per) / 100
        total_price_with_gst = total_price + gst_amount
        return total_price_with_gst


def calculate_total_amount_with_discount(basket):
    total_amount = sum(product.calculate_total_price() for product in basket)
    return apply_discount(total_amount)


def apply_discount(amount):
    if amount >= 500:
        discount = 0.05 * amount
        amount -= discount
    return amount


leather_wallet = Product("Leather Wallet", 1100, 18, 1)
umbrella = Product("Umbrella", 900, 12, 4)
cigarette = Product("Cigarette", 200, 28, 3)
honey = Product("Honey", 100, 0, 2)


basket = [leather_wallet, umbrella, cigarette, honey]


max_gst_product = max(basket, key=lambda x: (x.unit_price * x.gst_per / 100) * x.quantity)
print(f"Product with maximum GST amount: {max_gst_product.name}")


total_amount_after_discount = calculate_total_amount_with_discount(basket)
print(f"Total amount to be paid (after discount): Rs. {total_amount_after_discount:.2f}")