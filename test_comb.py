import unittest
from function_for_comb import wrapper


class TestStringMethods(unittest.TestCase):

    def test_wrapper_correct_args(self):
        self.assertEqual(wrapper(10, 5), 252)

    def test_wrapper_incorrect_args(self):
        with self.assertRaises(TypeError):
            wrapper("Andrey", -2.3)

    def test_wrapper_without_args(self):
        with self.assertRaises(TypeError):
            wrapper()


if __name__ == '__main__':
    unittest.main()
