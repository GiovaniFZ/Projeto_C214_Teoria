import unittest
from manager.manager import Manage

class TestClass(unittest.TestCase):
    
    # Positive tests
    def test_correct_age(self):
        name = 'Giovani'
        age = 12
        register = 123
        value = 12.50
        manager = Manage(name, age, register, value)
        self.assertEqual(manager.checkAge(), 12)
        
    def test_name(self):
        name = 'Giovani'
        age = 12
        register = 123
        value = 12.50
        manager = Manage(name, age, register, value)
        self.assertEqual(manager.checkName(), 'Giovani')

if __name__ == '__main__':
    unittest.main()