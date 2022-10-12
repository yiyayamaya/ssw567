"""it is a file."""
import unittest



def classify_triangle(side_a, side_b, side_c):
    """
    classify_triangle
    """

    res = ""
    for side in (side_a, side_b, side_c):
        if not isinstance(side, float, int):
            return "invalid input"

    input_list = [side_a, side_b, side_c]
    input_list.sort()
    side_a = input_list[0]
    side_b = input_list[1]
    side_c = input_list[2]

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        res = "invalid input"
    if side_a + side_b <= side_c:
        res = "NotATriangle"
    if side_a ** 2 + side_b ** 2 == side_c ** 2:
        res = 'Right'
    if side_a == side_b and side_b == side_c:
        res = 'Equilateral'
    if side_b in (side_a, side_c):
        res = "isosceles"
    res = "scalene"

    return res
class TestTriangles(unittest.TestCase):
    """
    TestTriangles
    """
    def test_right(self):
        """
        test_right
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')
        self.assertEqual(classify_triangle(3, 4, 5.1), 'Right')

    def test_not_a_triangle(self):
        """
        test_not_a_triangle
        """
        self.assertEqual(classify_triangle(1, 1, 3), 'NotATriangle')
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle')

    def test_invalid_input(self):
        """
        test_invalid_input
        """
        self.assertEqual(classify_triangle(0, 4, 5), 'invalid input')
        self.assertEqual(classify_triangle(-1, 3, 5), 'invalid input')
        self.assertEqual(classify_triangle("ss", 3, 5), 'invalid input')

    def test_equilateral(self):
        """
        test_equilateral
        """
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral')

    def test_isosceles(self):
        """
        test_isosceles
        """

        self.assertEqual(classify_triangle(3, 3, 4), 'isosceles')

    def test_scalene(self):
        """
        test_scalene
        """
        self.assertEqual(classify_triangle(3, 4, 4.5), 'scalene')


# This program summationoftwonumbers and displays their results
if __name__ == '__main__':
    unittest.main()
