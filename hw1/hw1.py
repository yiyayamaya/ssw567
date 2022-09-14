import unittest


def classifyTriangle(a, b, c):
    if not (isinstance(a, float) or isinstance(a, int)):
        return "invalid input"
    if not (isinstance(b, float) or isinstance(b, int)):
        return "invalid input"
    if not (isinstance(c, float) or isinstance(c, int)):
        return "invalid input"

    input_list = [a, b, c]
    input_list.sort()
    a = input_list[0]
    b = input_list[1]
    c = input_list[2]

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid input"
    if a + b <= c:
        return "NotATriangle"
    if a ** 2 + b ** 2 == c ** 2:
        return 'Right'
    if a == b and b == c:
        return 'Equilateral'
    if a == b or b == c:
        return "isosceles"
    return "scalene"


class TestTriangles(unittest.TestCase):
    def test_right(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
        self.assertEqual(classifyTriangle(3, 4, 5.1), 'Right')

    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle')
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def test_invalid_input(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'invalid input')
        self.assertEqual(classifyTriangle(-1, 3, 5), 'invalid input')
        self.assertEqual(classifyTriangle("ss", 3, 5), 'invalid input')

    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'isosceles')

    def test_scalene(self):
        self.assertEqual(classifyTriangle(3, 4, 4.5), 'scalene')


if __name__ == '__main__':
    unittest.main()
