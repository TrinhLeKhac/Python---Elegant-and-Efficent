class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self) -> float:
        return self.price * self.quantity

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
        )

    def __eq__(self, other):
        if not isinstance(other, Product):
            #  don't attempt to compare against unrelated types
            return NotImplemented
        return (
                self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
        )


from dataclasses import dataclass


@dataclass  # AAlready implemented __eq__, __repr__
class ProductWithDataClass:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity


p1 = Product(name="Laptop", price=1000, quantity=3)
p2 = Product(name="Laptop", price=1000, quantity=3)

p3 = ProductWithDataClass(name="Laptop", price=1000, quantity=3)
p4 = ProductWithDataClass(name="Laptop", price=1000, quantity=3)

print(p1)
print(p1.total_cost())
print(p1 == p2)

print(p3)
print(p3 == p4)
