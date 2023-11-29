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
        self.assertGreater(circle.perimeter(88), 552)
        self.assertLess(circle.perimeter(88), 553)
    def test_CircleArea(self):
        self.assertGreater(circle.area(5), 78)
        self.assertLess(circle.area(5), 79)
        self.assertGreater(circle.area(524), 862605)
        self.assertLess(circle.area(524), 862606)
        self.assertGreater(circle.area(12), 452)
        self.assertLess(circle.area(12), 453)
    def test_RectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(2, 4), 12)
        self.assertEqual(rectangle.perimeter(7, 4), 22)
        self.assertEqual(rectangle.perimeter(100, 1), 202)
    def test_RectangleArea(self):
        self.assertEqual(rectangle.area(8, 10), 80)
        self.assertEqual(rectangle.area(34, 1), 34)
        self.assertEqual(rectangle.area(56, 13), 728)
    def test_SquarePerimeter(self):
        self.assertEqual(square.perimeter(3), 12)
        self.assertEqual(square.perimeter(1), 4)
        self.assertEqual(square.perimeter(23), 92)
    def test_SquareArea(self):
        self.assertEqual(square.area(4), 16)
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.area(15), 225)
    def test_TrianglePerimeter(self):
        self.assertEqual(triangle.perimeter(3, 7, 1), 11)
        self.assertEqual(triangle.perimeter(25, 99, 17), 141)
        self.assertEqual(triangle.perimeter(8, 1, 91), 100)
    def test_TriangleArea(self):
        self.assertEqual(triangle.area(4, 8), 16)
        self.assertEqual(triangle.area(345, 2), 335)
        self.assertEqual(triangle.area(20, 2), 20)

if __name__ == '_main_':
    unittest.main()
