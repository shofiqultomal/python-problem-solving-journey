from solution import running_sum
import unittest


class TestRunningSum(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(running_sum([1,2,3,4]),
                         [1,3,6,10]
        )


    def test_example2(self):
        self.assertEqual(running_sum([1,2,3,4,5]),
                         [1,3,6,10,15]
        )

    def test_example3(self):
        self.assertEqual(running_sum([1,2,3,4,5,6]),
                         [1,3,6,10,15,21]
        )

if __name__ == "__main__":
    unittest.main()

