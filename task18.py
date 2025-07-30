class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"{self.name} narxi: {self.price}")

products = [
    Product("Laptop", 1399.99, "electronics"),
    Product("Smartphone", 899.99, "electronics"),
    Product("TV", 1499.99, "electronics"),
    Product("Tablet", 599.99, "electronics"),
    Product("Camera", 1199.99, "electronics"),
    Product("Headset", 249.99, "electronics")
]

most_expensive = products[0]
for p in products:
    if p.price > most_expensive.price:
        most_expensive = p

print(" Eng qimmat mahsulot:")
most_expensive.info()