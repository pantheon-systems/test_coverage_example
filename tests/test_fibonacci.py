import unittest
from fibonacci import fibonacci


class fibonacciTestCase(unittest.TestCase):

    def setUp(self):
        self.f = fibonacci.Fibonacci()

    def tearDown(self):
        pass

    def test__fib_returns_array_of_integers(self):
        mock_sequence = self.f.fib(7)
        for i in mock_sequence:
            assert isinstance(i, int)

    def test__fib_returns_correct_array(self):
        mock_sequence = self.f.fib(7)
        actual_sequence = [1, 1, 2, 3, 5, 8, 13]
        self.assertEquals(mock_sequence, actual_sequence)

    def test__fib_returns_empty_array_for_negative(self):
        mock_sequence = self.f.fib(-4)
        actual_sequence = []
        self.assertEquals(mock_sequence, actual_sequence)

    def test__fib_throws_TypeError_for_strings(self):
        with self.assertRaises(TypeError):
            self.f.fib("pantheon")

if __name__ == "__main__":
    unittest.main()  # run all tests
