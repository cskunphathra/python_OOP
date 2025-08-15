class Cashier:
    def __init__(self, products):
        self.products = products

    def recommend(self):
        product_names = " ".join(self.products)
        print(f"We have {product_names}.")