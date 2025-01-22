from statistics import mean, variance
import unittest
import random
from lesson import m, d

class TestCalculations(unittest.TestCase):

    def test_м(self):
        arr = self.rand()
        self.assertEqual(m(arr), mean(arr), 'This mathematical expectation is wrong.')

    def test_d(self):
        arr = self.rand()
        self.assertEqual(d(arr), variance(arr), 'This dispersion is wrong.')

    def rand(self):
        rand_list=[]
        n=100
        for i in range(n):
            rand_list.append(random.randint(1, 100))
