from practise_1 import change_element, check, reader
import unittest


class Tests(unittest.TestCase):

    def test_check(self):
        self.assertTrue('Все числа в последовательности уникальны', check([2, 3, 4, 5, 6, 7]))

    def test_reader(self):
        self.assertTrue([2, 4, 6, 8], reader([2, 3, 4, 5, 6, 7, 8, 237], 237))

    def test_change(self):
        self.assertTrue('World Hello', change_element('Hello World'))


if __name__ == '__main__':
    unittest.main()
