import pytest
import unittest

class Test(unittest.TestCase):

    def test_me(self):
        b = 1
        assert b == self.a
