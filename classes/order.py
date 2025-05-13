class Order:

    _total_orders = 0
    

    def __init__(self, products):
        self.products = products
        Order._total_orders += 1

   
    @classmethod
    def total_orders(cls):
        return cls._total_orders

    
    def total_price(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        return f"Заказ (Общая цена = {self.total_price()})"