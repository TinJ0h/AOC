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

        self.assertEquals(result, 3000, "Should be 000 calories")

    def test_sum_of_one_number(self):
        d = CalorieCounter()

        result = d.Sum([5000])

        self.assertEquals(result, 5000, "Should be 5000 calories")

    def test_sumofmany(self):
        d = CalorieCounter()

        result = d.Sum([1000,2000,3000,7000,7000])

        self.assertEquals(result, 20000, "Should be 6000 calories")

    def test_read_input(self): 
        d = CalorieCounter()

        d.ReadData("Test_tekst_1.txt")

        self.assertEquals(len(d.data),5,"length of test tekst")

    def test_pick_highest_calories(self): 
        d = CalorieCounter()

        d.ReadData("Test_tekst_1.txt")
        result = d.GetMaxCalories()

        self.assertEquals(result,24000,"Max total calories of one elf")


    def test_pick_highest_calories(self): 
        d = CalorieCounter()

        d.ReadData("day1.txt")
        result = d.GetMaxCalories()

        self.assertEquals(result,74198,"Max total calories of one elf")

    def test_sum_of_top_three_elf(self): 
        d = CalorieCounter()

        d.ReadData("Test_tekst_1.txt")
        result = d.GetTopThreeCalories()

        self.assertEquals(result,45000,"Total calories of top three calories")

        
    def test_sum_of_top_three_elf(self): 
        d = CalorieCounter()

        d.ReadData("day1.txt")
        result = d.GetTopThreeCalories()

        self.assertEquals(result, 209914,"Total calories of top three calories")