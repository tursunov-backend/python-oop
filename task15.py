class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock
        

p1 = Product("iPhone 16", 1000, True)
p2 = Product("Sabzi", 3.99, False)
p3 = Product("Noutbuk", 850.5, True)
p4 = Product("Quloqchin", 45, True)
p5 = Product("Sut", 2.75, False)

products = [p1, p2, p3, p4, p5]

total_price = 0

for product in products:
    if product.in_stock:
        total_price += product.price

print(f"Ombordagi mahsulotlar narxi: {total_price:.2f}")
