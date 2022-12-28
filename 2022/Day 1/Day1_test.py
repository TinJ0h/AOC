import unittest

from Day1 import CalorieCounter

class Day1_test(unittest.TestCase):
    def test_init(self):
        d = CalorieCounter()
        self.assertIsNotNone(d)
        
    def test_test2(self):
        self.assertTrue(True, "Should be True")

    def test_sum(self):
        d = CalorieCounter()

        result = d.Sum([1000,2000,3000])

        self.assertEquals(result, 6000, "Should be 6000 calories")

    def test_sum_of_two_numbwers(self):
        d = CalorieCounter()

        result = d.Sum([1000,2000])

        self.assertEquals(result, 3000, "Should be 3000 calories")
