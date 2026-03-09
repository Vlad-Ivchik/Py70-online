# 3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов,
# поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.


class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price

    def show_products(self):
        for key, value in self.products.items():
            print(f"{key} - {value}$")

    def del_product(self, name):
        del self.products[name]

    def search_product(self, name):
        if name in self.products:
            return {name: self.products[name]}
        return None


store = Shop()
store.add_product('Apple', 15)
store.add_product('Xiaomi', 5)
store.add_product('Samsung', 10)
print(store.products)
store.show_products()
store.del_product('Xiaomi')
print(store.products)
print(store.search_product('Samsung'))
