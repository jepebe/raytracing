from math import sqrt
from typing import Union


class Vec3:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._e = [x, y, z]

    @property
    def x(self):
        return self._e[0]

    @property
    def y(self):
        return self._e[1]

    @property
    def z(self):
        return self._e[2]

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, t: Union['Vec3', float]):
        if isinstance(t, Vec3):
            return Vec3(self.x * t.x, self.y * t.y, self.z * t.z)
        else:
            return Vec3(self.x * t, self.y * t, self.z * t)

    def __truediv__(self, t: Union['Vec3', float]):
        if isinstance(t, Vec3):
            return self.__mul__(Vec3(1 / t.x, 1 / t.y, 1 / t.z))
        else:
            return self.__mul__(1 / t)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __getitem__(self, index):
        return self._e[index]

    def __iadd__(self, other):
        self._e[0] += other.x
        self._e[1] += other.y
        self._e[2] += other.z
        return self

    def __isub__(self, other):
        self._e[0] -= other.x
        self._e[1] -= other.y
        self._e[2] -= other.z
        return self

    def __imul__(self, t):
        self._e[0] *= t
        self._e[1] *= t
        self._e[2] *= t
        return self

    def __itruediv__(self, t):
        return self.__imul__(1 / t)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vec3(x, y, z)

    def length(self):
        return sqrt(self.squared_length())

    def squared_length(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def unit_vector(self):
        return self / self.length()

    def __str__(self):
        return f'{self.x} {self.y} {self.z}'


class Color(Vec3):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y, z)

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def rgb(self):
        return int(self.r * 255.999), int(self.g * 255.999), int(self.b * 255.999)

    def __str__(self):
        r = int(self.r * 255.999)
        g = int(self.g * 255.999)
        b = int(self.b * 255.999)
        return f'{r} {g} {b}'
