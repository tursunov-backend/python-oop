class Book:

    def __init__(self, title, author, is_read):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print(f'{self.title} Kitob oqilgan deb belgilandi')

    def status(self):
        if self.is_read:
            print("O'qilgan")
        else:
            print("O'qilmagan")

b1 = Book('Otgan kunlar', 'A.Qodiriy', True)  

b1.mark_as_read()
b1.status()