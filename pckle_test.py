import unittest
import pickler



#write a unit test that proves that if you assign a list to a variable, then pickle that list, then unpickle it to a second variable, the first and second variable will be equivalent

class PicklerTests(unittest.TestCase):
    
    def test_pickler(self):          
        data = [9,9,9]
        pickler.make_pickler(data, "save.p")
        result = pickler.unpickler("save.p")
        self.assertEqual(data, result)
    