from math import sqrt

import pytest

from ray import Vec3, Point3, Color


def test_negation():
    v = Vec3(1, 3, 7)
    neg_v = -v
    assert neg_v.x == -1
    assert neg_v.y == -3
    assert neg_v.z == -7

    neg_neg_v = -neg_v
    assert neg_neg_v.x == 1
    assert neg_neg_v.y == 3
    assert neg_neg_v.z == 7


def test_add():
    a = Vec3(1, 2, 3)
    b = Vec3(3, 2, 1)
    c = a + b
    assert c != a
    assert c != b
    assert c.x == 4
    assert c.y == 4
    assert c.z == 4


def test_element_wise_multiplication():
    a = Vec3(1, 2, 3)
    b = Vec3(4, 5, 7)
    c = a * b

    assert c.x == 4
    assert c.y == 10
    assert c.z == 21


def test_scaling():
    v = Vec3(2, 5, 7)
    u = v * 5

    assert u.x == 10
    assert u.y == 25
    assert u.z == 35


def test_division():
    v = Vec3(3, 6, 9)
    u = v / 3
    assert u.x == 1
    assert u.y == 2
    assert u.z == 3


def test_element_wise_division():
    v = Vec3(4, 8, 12)
    w = Vec3(2, 4, 3)
    u = v / w
    assert u.x == 2
    assert u.y == 2
    assert u.z == 4


def test_subtract():
    a = Vec3(1, 2, 3)
    b = Vec3(3, 2, 1)
    c = a - b
    assert c != a
    assert c != b
    assert c.x == -2
    assert c.y == 0
    assert c.z == 2


def test_subscript():
    v = Vec3(-5, 7, 1)

    assert v[0] == v.x
    assert v[1] == v.y
    assert v[2] == v.z


def test_inplace_add():
    v = Vec3(-3, 11, -5.5)

    v += Vec3(1, 1, 1)

    assert v.x == -2
    assert v.y == 12
    assert v.z == -4.5


def test_inplace_subtract():
    v = Vec3(-3, 11, -5.5)

    v -= Vec3(1, 1, 1)

    assert v.x == -4
    assert v.y == 10
    assert v.z == -6.5


def test_inplace_multiplication():
    v = Vec3(-3, 11, -2)

    v *= 2

    assert v.x == -6
    assert v.y == 22
    assert v.z == -4


def test_inplace_division():
    v = Vec3(-3, 11, -2)

    v /= 2

    assert v.x == -1.5
    assert v.y == 5.5
    assert v.z == -1


def test_dot_product():
    v = Vec3(1, 2, 3)
    assert v.dot(v) == (1 * 1) + (2 * 2) + (3 * 3)


def test_cross_product():
    u = Vec3(2, 3, 4)
    v = Vec3(5, 6, 7)
    cross = u.cross(v)
    assert cross.x == -3
    assert cross.y == 6
    assert cross.z == -3


def test_unit_vector():
    u = Vec3(2, 4, 7)
    n = u.unit_vector()
    assert abs(n.x - 0.24077171) < 0.0000001
    assert abs(n.y - 0.48154341) < 0.0000001
    assert abs(n.z - 0.84270097) < 0.0000001


def test_length():
    v = Vec3(1, 1, 1)
    assert v.length() == sqrt(3)


def test_color():
    c = Color(255, 128, 64)

    assert c.r == 255
    assert c.g == 128
    assert c.b == 64


def test_point():
    c = Point3()

    assert c.x == 0
    assert c.y == 0
    assert c.z == 0
