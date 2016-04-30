from unittest import TestCase
from BefungeInterpreter import BefungeInterpreter

class TestBefungeInterpreter(TestCase):
    def test_interpret(self):
        bi = BefungeInterpreter()
        result = bi.interpret('>987v>.v\nv456<  :\n>321 ^ _@')
        self.assertEqual(result, '123456789')
