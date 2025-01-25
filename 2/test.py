import unittest
from Decorator import Decorator

class TestDecorator(unittest.TestCase):
    def test_decorator(self):
         decorator = Decorator('test')
         self.assertEqual('<b><a>test</a></b>', str(decorator.tag('a').tag('b')), 'This mathematical expectation is wrong.')