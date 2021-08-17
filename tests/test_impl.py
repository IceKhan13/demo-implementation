"""Docstring."""
import unittest

from qlib import Impl


class TestImpl(unittest.TestCase):
    """Tests Impl class implementation."""

    def test_run(self):
        """Tests run method implementation."""
        impl = Impl()

        self.assertEqual(impl.run(2), 4)
