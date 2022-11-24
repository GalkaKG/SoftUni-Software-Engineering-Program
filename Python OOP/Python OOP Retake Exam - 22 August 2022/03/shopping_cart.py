class ShoppingCart:
    def __init__(self, shop_name: str, budget: float):
        self.shop_name = shop_name
        self.budget = budget
        self.products = {}

    @property
    def shop_name(self):
        return self.__shop_name

    @shop_name.setter
    def shop_name(self, value: str):
        if not value[0].isupper() or not value.isalpha():
            raise ValueError("Shop must contain only letters and must start with capital letter!")
        self.__shop_name = value

    def add_to_cart(self, product_name: str, product_price: float):
        if product_price >= 100.0:
            raise ValueError(f"Product {product_name} cost too much!")
        self.products[product_name] = product_price
        return f"{product_name} product was successfully added to the cart!"

    def remove_from_cart(self, product_name: str):
        if product_name in self.products:
            del self.products[product_name]
            return f"Product {product_name} was successfully removed from the cart!"
        else:
            raise ValueError(f"No product with name {product_name} in the cart!")

    def __add__(self, other):  # other is another ShoppingCart instance
        new_shop_name = f"{self.shop_name}{other.shop_name}"
        new_budget = self.budget + other.budget
        new_shopping_cart = ShoppingCart(new_shop_name, new_budget)
        new_shopping_cart.products.update(**self.products)
        new_shopping_cart.products.update(**other.products)
        return new_shopping_cart

    def buy_products(self):
        total_sum = sum(self.products.values())
        if total_sum > self.budget:
            raise ValueError(f"Not enough money to buy the products! Over budget with {total_sum - self.budget:.2f}lv!")
        return f'Products were successfully bought! Total cost: {total_sum:.2f}lv.'
