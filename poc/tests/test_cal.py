import unittest
import poc.app as ap


class Testcalc(unittest.TestCase):

    def setUp(self):
       self.x = 10
       self.y = 5
    
    def test_add(self):
        self.assertEqual(ap.add(self.x, self.y), 15)
        self.assertEqual(ap.add(2,3), 5)
        
    def test_sub(self):
        self.assertEqual(ap.subtract(self.x, self.y), 5)
        self.assertEqual(ap.subtract(2,3), -1)

    def test_multiply(self):
        self.assertEqual(ap.multiply(self.x, self.y), 50)
        self.assertEqual(ap.multiply(2,3), 6)

    def test_devide(self):
        self.assertEqual(ap.devide(self.x, self.y), 2)
        self.assertEqual(ap.devide(5, 2), 2.5)
        self.assertRaises(ValueError, app.devide, 10, 0)
        with self.assertRaises(ValueError):
           app.devide(10, 0)


if __name__ == '__main__':
    unittest.main()


#run coverage run test_cal.py
#coverage report    
