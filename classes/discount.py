class Discount:
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    def __str__(self):
        return f"Скидка (описание скидки={self.description}, процент скидки={self.discount_percent})"
    
    @staticmethod
    def calculate_discounted_price(price, discount):
        return price * (1 - discount / 100)
