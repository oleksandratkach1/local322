import math


class Figure:
    """Base abstract class for all geometric figures."""

    def dimension(self):
        raise NotImplementedError

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}(volume={self.volume():.4f})"


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _is_valid(self):
        return (self.a > 0 and self.b > 0 and self.c > 0 and
                self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        if not self._is_valid():
            return 0.0
        s = self.perimeter() / 2
        val = s * (s - self.a) * (s - self.b) * (s - self.c)
        return math.sqrt(val) if val >= 0 else 0.0

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def _height(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        diff = a - b
        if abs(diff) < 1e-9:
            val = c ** 2 - 0
            return math.sqrt(max(val, 0))
        x = (diff ** 2 + c ** 2 - d ** 2) / (2 * diff)
        val = c ** 2 - x ** 2
        return math.sqrt(max(val, 0))

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        h = self._height()
        return (self.a + self.b) / 2 * h

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self._h = h

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self._h

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def volume(self):
        return self.square()


class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.r ** 2

    def squareBase(self):
        return None

    def height(self):
        return 2 * self.r

    def volume(self):
        return (4 / 3) * math.pi * self.r ** 3


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self._h = h

    def dimension(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareBase(self):
        return (math.sqrt(3) / 4) * self.a ** 2

    def squareSurface(self):
        a = self.a
        h = self._h
        apothem = math.sqrt(h ** 2 + (a / (2 * math.sqrt(3))) ** 2)
        return (3 / 2) * a * apothem

    def height(self):
        return self._h

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self._h = h

    def dimension(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareBase(self):
        return self.a * self.b

    def squareSurface(self):
        a, b, h = self.a, self.b, self._h
        sl1 = math.sqrt(h ** 2 + (b / 2) ** 2)
        sl2 = math.sqrt(h ** 2 + (a / 2) ** 2)
        return a * sl1 + b * sl2

    def height(self):
        return self._h

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareBase(self):
        return self.a * self.b

    def squareSurface(self):
        return 2 * (self.a * self.c + self.b * self.c)

    def height(self):
        return self.c

    def volume(self):
        return self.a * self.b * self.c


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = h

    def dimension(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareBase(self):
        return math.pi * self.r ** 2

    def squareSurface(self):
        l = math.sqrt(self.r ** 2 + self._h ** 2)
        return math.pi * self.r * l

    def height(self):
        return self._h

    def volume(self):
        return (1 / 3) * math.pi * self.r ** 2 * self._h


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self._h = h

    def dimension(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareBase(self):
        a, b, c = self.a, self.b, self.c
        if not (a > 0 and b > 0 and c > 0 and
                a + b > c and a + c > b and b + c > a):
            return 0.0
        s = (a + b + c) / 2
        val = s * (s - a) * (s - b) * (s - c)
        return math.sqrt(val) if val >= 0 else 0.0

    def squareSurface(self):
        return (self.a + self.b + self.c) * self._h

    def height(self):
        return self._h

    def volume(self):
        return self.squareBase() * self._h