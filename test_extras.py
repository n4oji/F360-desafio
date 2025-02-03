import unittest
from extras import max_sum

class TestMaxSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_sum([]), 0)

    def test_small_positive(self):
        self.assertEqual(max_sum([1,2,3,4,5]), 15)
        self.assertEqual(max_sum([1,2,3]), 6)

    def test_small_negative(self):
        self.assertEqual(max_sum([-1,-2,-3,-4,-5]), -1)
        self.assertEqual(max_sum([-2,-3,-4,-5]), -2)

    def test_mixed(self):
        self.assertEqual(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sum([1, -2, -3, 4, 5, -6, 9, 10]), 22)

    def test_unique_element(self):
        self.assertEqual(max_sum([3]), 3)
        self.assertEqual(max_sum([0]), 0)
        self.assertEqual(max_sum([-10]), -10)

    def test_large_positive(self):
        large_list = [i for i in range(1, 1001)]
        self.assertEqual(max_sum(large_list), sum(large_list))

    def test_large_negative(self):
        large_negative_list = [i if i % 2 == 0 else -i for i in range(1, 1001)]
        self.assertEqual(max_sum(large_negative_list), 1000)


if __name__ == '__main__':
    unittest.main()