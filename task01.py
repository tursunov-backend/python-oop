class Car:

    def __init__(self, brand, model, year):
        self.brand = 'brand'
        self.model = 'model'
        self.year = year

    def info(self):
        return f"Car(brand='{self.brand}', model='{self.model}', year='{self.year}')"
    
c01 = Car('BMW', 'M5', 2023)
c02 = Car('GM', 'Damas', 2024)

print(c01.info())
print(c02.info())