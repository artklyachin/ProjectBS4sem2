import unittest
from request import Request


class TemperatureTest(unittest.TestCase):

    def test_type(self):
        req = Request()
        temperature_list = req.get_temp()
        print(temperature_list)
        for elem in temperature_list:
            self.assertTrue(isinstance(elem, str))

    def test_num(self):
        req = Request()
        temperature_list = req.get_temp()
        for elem in temperature_list:
            if (elem[0] == '+' or elem[0] == '-'):
                degree = elem[1:-1]
            else:
                degree = elem[0:-1]
            self.assertTrue(degree.isdigit())


if __name__ == '__main__':
    unittest.main()
