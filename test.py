import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def tect_to_upper(self):
        name = "Satrunjay"
        up = to_upper(name)
        self.assertEqual(up, "SATRUNJAY")

if __name__ == "__main__":
    unittest.main()