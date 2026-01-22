class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"Mahsulot: {self.name}, Narxi: {self.price}")


p1 = Product("iPhone 16", 1000, "Telefon")
p2 = Product("Sabzi", 3.99, "Sabzavot")
p3 = Product("Noutbuk", 850.5, "Texnika")
p4 = Product("Quloqchin", 45, "Aksessuar")
p5 = Product("Sut", 2.75, "Oziq-ovqat")
p6 = Product("Samsung TV", 980, "Texnika")

products = [p1, p2, p3, p4, p5, p6]

most_expensive = products[0]

for product in products:
    if product.price > most_expensive.price:
        most_expensive = product

print("Eng qimmat mahsulot:")
most_expensive.info()
