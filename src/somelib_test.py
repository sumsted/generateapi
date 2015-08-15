from unittest import TestCase
from somelib_client import *


class TestSomelib(TestCase):
    def test_mouse(self):
        cheese = 1
        trap = 2
        cat = 3
        self.assertEqual(mouse(cheese, trap, cat), 6)

    def test_dog(self):
        bone = 2
        self.assertEqual(dog(bone), 10)

