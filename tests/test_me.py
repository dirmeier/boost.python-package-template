import pytest
import unittest
import boostmodules


class Test(unittest.TestCase):
    def test_me(self):
        assert boostmodules.graph().get() == 1.0
