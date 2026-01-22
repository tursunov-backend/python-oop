class Book:

    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
       
    def status(self):
        if self.is_read:
            print(f"{self.title}: O'qilgan")
        else:
            print(f"{self.title}: O'qilmagan")


b1 = Book("O'tkan kunlar", "A. Qodiriy")
b2 = Book("Kecha va kunduz", "Cho'lpon")
b3 = Book("Odam bo'lish qiyin", "O'. Umarbekov")
b4 = Book("Alvido bolalik", "T. Malik")
b5 = Book("Navoiy", "Oybek")

books = [b1, b2, b3, b4, b5]

b1.mark_as_read()
b3.mark_as_read()

for book in books:
    book.status()

print("\nO'qilgan kitoblar:")
for book in books:
    if book.is_read:
        print(f"- {book.title}")