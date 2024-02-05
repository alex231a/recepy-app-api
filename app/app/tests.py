"""sample tests"""


from django.test import SimpleTestCase
from . import calc


class TestCalc(SimpleTestCase):

    def test_calc(self):
        res = calc.add(2, 4)
        self.assertEqual(res, 6)

    def test_subtract_numbers(self):
        res = calc.subrtact(10, 15)
        self.assertEqual(res, 5)
