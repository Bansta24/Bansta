import decimal
class road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass = self._length * self._width * 10   * 10 / 5000
        return mass


my_road = road(20, 5000)
print(decimal.Decimal(my_road.mass()),'тонн асфальта')
