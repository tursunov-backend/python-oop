class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
        

    def info(self):
        return f"Product(name='{self.name}', price='{self.price}', category='{self.category}', in_stock='{self.in_stock}')"
    
p01 = Product('olma', 13_990, 'fruit', True)
p02 = Product('sabzi', 3_990, 'sabzavot', False)

products = [p01, p02]
for product in products:
    print(f"Mahsulot: {product.name}, Narxi: {product.price}")
    