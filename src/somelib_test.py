from unittest import TestCase
from somelib_client import *


class TestSomelib(TestCase):
    def test_mouse(self):
        cheese = 1
        trap = 1
        cat = 1
        self.assertEqual(mouse(cheese, trap, cat), 3)

    def test_dog(self):
        bone = 1
        self.assertEqual(dog(bone), 5)

