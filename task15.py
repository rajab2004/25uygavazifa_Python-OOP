class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

products = [
    Product("Powerbank", 99.99, True),
    Product("Mouse", 49.99, False),
    Product("Monitor", 249.50, True),
    Product("Charger", 29.99, True),
    Product("Headphones", 89.99, False)
]

total = 0
for p in products:
    if p.in_stock:
        total += p.price

print(f"Ombordagi mahsulotlar narxi: {total:.2f}")