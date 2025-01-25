from statistics import mean, variance
import unittest
import random
from lesson import m, d

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.rand_list=[]
        n=100
        for i in range(n):
            self.rand_list.append(random.randint(1, 100))

    def test_м(self):
        self.assertEqual(m(self.rand_list), mean(self.rand_list), 'This mathematical expectation is wrong.')

    def test_d(self):
        self.assertEqual(d(self.rand_list), variance(self.rand_list), 'This dispersion is wrong.')