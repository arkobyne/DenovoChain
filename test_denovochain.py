# test_denovochain.py
"""
Tests for DenovoChain module.
"""

import unittest
from denovochain import DenovoChain

class TestDenovoChain(unittest.TestCase):
    """Test cases for DenovoChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DenovoChain()
        self.assertIsInstance(instance, DenovoChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DenovoChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
