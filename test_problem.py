
import unittest
from problem import Problemtwo

class TestAdd(unittest.TestCase):
    """
    Test the add function from the math library
    """
    def setUp(self):
        self.problem = Problemtwo()

    def test_greedy(self):
        """
        Test that the addition of two integers returns the correct total
        """
        l = [1, 10, 2]
        value = 23
        result = self.problem.coinproblem(value, l)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()