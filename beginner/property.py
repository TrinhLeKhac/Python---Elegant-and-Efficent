class Circle:
    def __init__(self, radius):
        # _ => convention for internal attributes
        # Python don't have access modifier like other language
        self._radius = radius

    @property
    def radius(self):
        """Get the radius of the circle."""
        print("Called me")
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle. Must be positive."""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @radius.deleter
    def radius(self):
        print("Deleted")
        del self._radius

    @property
    def diameter(self):
        """Get the diameter of the circle."""
        return self._radius * 2


# Usage
c = Circle(5)
print(c.radius)
print(c.diameter)

# print(c._radius)  # Can not call this attribute outside the class: error

c.radius = 10
print(c.radius)
print(c.diameter)

del c.radius  # Delete internal attribute c._radius
print(c.diameter)
