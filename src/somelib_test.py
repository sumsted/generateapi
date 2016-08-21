from unittest import TestCase
from somelib_client import *


class TestSomelib(TestCase):
    def test_mouse(self):
        cheese = None
        trap = None
        cat = None
        self.assertEqual(mouse(cheese, trap, cat), None)

    def test_dog(self):
        bone = None
        self.assertEqual(dog(bone), None)

