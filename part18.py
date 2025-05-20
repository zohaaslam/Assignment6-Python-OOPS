# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# Solve:


class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # getter method
    @property
    def price(self):
        return self._price

    # setter method
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Use the class
p = Product(1000)

# Get price using @property
print("Initial price:", p.price)

# Set price using @price.setter
p.price = 1500
print("Updated price:", p.price)

# Try setting negative price
p.price = -500  # This will give warning

# Delete price using @price.deleter
del p.price

