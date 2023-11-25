class Product:
    def __init__(self, name, unit_price, gst_percentage, quantity):
        self.name = name
        self.unit_price = unit_price
        self.gst_percentage = gst_percentage
        self.quantity = quantity

    def calculate_total_price(self):
        total_price = self.unit_price * self.quantity
        gst_amount = (total_price * self.gst_percentage) / 100
        total_price_with_gst = total_price + gst_amount
        return total_price_with_gst

def apply_discount(product):
    if product.unit_price >= 500:
        discount = 0.05 * product.calculate_total_price()
        return product, product.calculate_total_price() - discount
    else:
        return product, product.calculate_total_price()


leather_wallet = Product("Leather Wallet", 1100, 18, 1)
umbrella = Product("Umbrella", 900, 12, 4)
cigarette = Product("Cigarette", 200, 28, 3)
honey = Product("Honey", 100, 0, 2)


basket = [leather_wallet, umbrella, cigarette, honey]


print("Entered products with discount:")
for product in basket:
    product_with_discount, total_price_with_discount = apply_discount(product)
    print(f"{product_with_discount.name}, Total Price with Discount: Rs. {total_price_with_discount:.2f}")

max_gst_product = max(basket, key=lambda x: (x.unit_price * x.gst_percentage / 100) * x.quantity)
print(f"\nProduct with maximum GST amount: {max_gst_product.name}")

total_amount = sum(apply_discount(product)[1] for product in basket)
print(f"\nTotal amount to be paid (after discount): Rs. {total_amount:.2f}")

