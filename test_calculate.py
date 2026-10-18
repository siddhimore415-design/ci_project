import unittest

def add(a, b):
    return a + b

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 10)
        

if __name__ == "__main__":
    unittest.main()
