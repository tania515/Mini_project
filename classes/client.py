class Client:
    
    _total_client = 0

    def __init__(self, name, orders):
        self.name = name 
        self.orders = orders 
        Client._total_client += 1
        
    @classmethod
    def total_client(cls):
        return cls._total_client

    
    def total_sum(self):
        return sum(order.total_price() for order in self.orders)

 
    def __str__(self):
        return f"Клиент {self.name}, (Общая сумма = {self.total_sum()})"
    
    def add_order(self, add_order):
        self.orders.append(add_order)


