class AreaCalculator:
    def area(self, a, b=None):
        if b is None:
            return 3.14 * a * a  # Circle
        return a * b  # Rectangle

# Usage
calc = AreaCalculator()
print(calc.area(5))        # Circle with radius 5
print(calc.area(4, 6))     # Rectangle 4x6
