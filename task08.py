class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
        

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} mahsuloti omborda bor")
        else:
            print(f"{self.name} mahsuloti omborda yo'q")
    
p01 = Product('iphone16', 1_000, 'phone', True)
p02 = Product('sabzi', 3_990, 'sabzavot', False)

products = [p01, p02]
for product in products:
    product.check_stock()