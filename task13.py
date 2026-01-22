class Book:

    def __init__(self, title, author, is_read):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print(f'{self.title} - Kitob oqilgan deb belgilandi')

    def status(self):
        if self.is_read:
            print(f"{self.title}: O'qilgan")
        else:
            print(f"{self.title}: O'qilmagan")

b1 = Book('Otgan kunlar', 'A.Qodiriy', False)  
b2 = Book('kecha va kunduz', 'Cho\'lpon', False)  
b3 = Book('odam bo\'lish qiyin', 'O\'.Umarbekov', False)  
b4 = Book('alvido bolalik', 'T.Malik', False)  

b1.mark_as_read()
b2.mark_as_read()
print("\nKitoblar holati:")
b1.status()
b2.status()
b3.status()
b4.status()