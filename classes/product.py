class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"