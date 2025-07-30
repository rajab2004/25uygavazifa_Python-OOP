class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        print(f"{self.title}: {'Oqilgan' if self.is_read else 'Oqilmagan'}")


books = [
    Book("Oq kema", "Chingiz Aytmatov"),
    Book("Chol va dengiz", "Ernest Hemingway"),
    Book("Samarqand", "Amin Maalouf"),
    Book("Dunyoning ishlari", "O'tkir Hoshimov"),
    Book("Alkimyogar", "Paulo Coelho")
]

books[0].mark_as_read()
books[4].mark_as_read()

print("Barcha kitoblar holati:")
for book in books:
    book.status()
