"""Практика 3: магазин с товарами, корзиной и заказами."""


class Product:
    """Товар с ценой, количеством и категорией."""

    def __init__(self, name, price, amount, category):
        """Создаёт товар."""
        self.name = name
        self.price = price
        self.amount = amount
        self.category = category


class Order:
    """Заказ с учётом скидки и налога."""

    nalog = 0.22

    def __init__(self, cart, discount=0.0):
        """Создаёт заказ из корзины со скидкой."""
        self.cart = cart
        self.discount = discount

    def total(self):
        """Возвращает итоговую цену со скидкой и налогом."""
        price = 0
        for product, quantity in self.cart.items.items():
            price = price + product.price * quantity
        price = price * (1 - self.discount)
        price = price * (1 + self.nalog)
        return price


class Customer:
    """Покупатель со списком заказов."""

    def __init__(self, name):
        """Создаёт покупателя без заказов."""
        self.name = name
        self.orders = []

    def make_order(self, cart):
        """Создаёт заказ из корзины и сохраняет его."""
        order = Order(cart)
        self.orders.append(order)
        return order


class ShoppingCart:
    """Корзина с товарами и их количеством."""

    def __init__(self):
        """Создаёт пустую корзину."""
        self.items = {}

    def add(self, product, quantity):
        """Добавляет товар в корзину."""
        self.items[product] = self.items.get(product, 0) + quantity

    def remove(self, product):
        """Удаляет товар из корзины."""
        del self.items[product]

    def update(self, product, quantity):
        """Меняет количество товара в корзине."""
        self.items[product] = quantity


phone = Product("Телефон", 20000, 10, "Электроника")
chech = Product("Чечевица", 100, 100, "Бакалея")

customer = Customer("Обама")
cart = ShoppingCart()
cart.add(phone, 1)
cart.add(chech, 3)
cart.remove(phone)
cart.update(chech, 203)

order = customer.make_order(cart)
print(order.total())
