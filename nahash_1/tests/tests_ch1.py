import unittest
from nahash_1 import excersise_1 as ex1
from nahash_1 import excersise_2
from nahash_1 import excersise_3

class BasicTests(unittest.TestCase):
    def test1(self): 
        self.assertEqual(ex1.hello_world("michael", "ptitsyn"), "hello michael ptitsyn")
    
    def test2_1(self): 
        self.assertEqual(excersise_2.basic_if(5), 5)
    
    def test2_2(self): 
        self.assertEqual(excersise_2.basic_if(6), 6)

    def test2_3(self): 
        self.assertEqual(excersise_2.basic_if(-6), 5)
        
    def test3(self): 
        self.assertEqual(excersise_3.basic_loop([1,2,3,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()