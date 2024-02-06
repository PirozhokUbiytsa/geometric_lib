import unittest
import circle
import rectangle
import square
import triangle

class MyTests(unittest.TestCase):
    def test_CirclePerimeter(self):
        self.assertGreater(circle.perimeter(3), 18)
        self.assertLess(circle.perimeter(3), 19)
        self.assertGreater(circle.perimeter(13), 81)
        self.assertLess(circle.perimeter(13), 82)
        self.assertRaises(ValueError, circle.perimeter, -2)
    def test_CircleArea(self):
        self.assertGreater(circle.area(5), 78)
        self.assertLess(circle.area(5), 79)
        self.assertGreater(circle.area(524), 862605)
        self.assertLess(circle.area(524), 862606)
        self.assertGreater(circle.area(12), 452)
        self.assertLess(circle.area(12), 453)
        self.assertRaises(ValueError, circle.area, 0)
    def test_RectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(2, 4), 12)
        self.assertEqual(rectangle.perimeter(7, 4), 22)
        self.assertEqual(rectangle.perimeter(100, 1), 202)
        self.assertRaises(ValueError, rectangle.perimeter, -6, 0)
        self.assertEqual(rectangle.perimeter(0, 1), 1)
    def test_RectangleArea(self):
        self.assertEqual(rectangle.area(8, 10), 80)
        self.assertEqual(rectangle.area(34, 1), 34)
        self.assertEqual(rectangle.area(56, 13), 728)
        self.assertRaises(ValueError, rectangle.area, -1011, 5)
    def test_SquarePerimeter(self):
        self.assertEqual(square.perimeter(3), 12)
        self.assertEqual(square.perimeter(1), 4)
        self.assertEqual(square.perimeter(23), 92)
        self.assertRaises(ValueError, square.perimeter, -72)
    def test_SquareArea(self):
        self.assertEqual(square.area(4), 16)
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.area(15), 225)
        self.assertRaises(ValueError, square.area, -3)
    def test_TrianglePerimeter(self):
        self.assertEqual(triangle.perimeter(3, 7, 1), 11)
        self.assertEqual(triangle.perimeter(25, 99, 17), 141)
        self.assertEqual(triangle.perimeter(8, 1, 91), 100)
        self.assertRaises(ValueError, triangle.perimeter, -3, 3, 4)
    def test_TriangleArea(self):
        self.assertEqual(triangle.area(4, 8), 16)
        self.assertEqual(triangle.area(345, 2), 345)
        self.assertEqual(triangle.area(20, 2), 20)
        self.assertRaises(ValueError, triangle.area, -3, 4)

if __name__ == '_main_':
    unittest.main()
