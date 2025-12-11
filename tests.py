import unittest

import math
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_unit(self):
        self.assertAlmostEqual(circle.area(1), math.pi, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5, places=7)

    def test_diameter(self):
        self.assertEqual(circle.diameter(3), 6)

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(rectangle.area(5, 5), 25)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 3), 10)

    def test_diagonal(self):
        self.assertAlmostEqual(rectangle.diagonal(3, 4), 5.0, places=7)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(4), 16)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(2.5), 10)

    def test_diagonal(self):
        self.assertAlmostEqual(square.diagonal(1), 2 ** 0.5, places=7)

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(4, 3), 6)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
