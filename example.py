# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.client import Client
from classes.discount import Discount


# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)


# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product1])

# Создаем клиентов
сlient1 = Client("Ivan", [order1])
client2 = Client("Semen", [order1, order2])
client3 = Client("Dima", [order2])



# Рассчитываем цену с учетом скидки
discounted_price = Discount.calculate_discounted_price(product1.price, 10)
print(f"Сниженная цена на {product1.name}: {discounted_price}")  

product1.price=discounted_price
order3 = Order([product2, product1])

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")  # Вывод: Всего заказов: 

# Выводим информацию о заказах
print(order1)  
print(order2)  
print(order3)  

client4 = Client("Dimon", [order3])

# Выводим общее количество клиентов
print(f"Всего клиентов: {Client.total_client()}")  # Вывод: Всего клиентов: 

# Выводим информацию о заказах
print(сlient1) 
print(client2)  
print(client3)
print(client4)

client3.add_order(order1)

print(client3)


