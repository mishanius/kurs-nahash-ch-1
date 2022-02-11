import unittest
from nahash_1 import excersise_1 as ex1

class MyTest(unittest.TestCase):
    def test(self): 
        self.assertEqual(ex1.hello_world("michael", "ptitsyn"), "hello michael ptitsyn")

if __name__ == '__main__':
    unittest.main()