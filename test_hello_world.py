import unittest
from hello_world import main

class TestHelloWorld(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
