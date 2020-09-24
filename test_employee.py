import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for employee class"""

    @classmethod
    def setUpClass(cls):
        print('setUpclass')

    def setUp(self):
        print('setUp')
        self.levin = Employee('Levin', 'Batallones', 2000000)
        self.martin = Employee('Martin', 'Briceno', 1999999)
        self.alice = Employee('Alice', 'Huh', 1985)
        self.rome = Employee('Rome', 'Bell', '100000')

    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        self.assertEqual(self.levin.email, 'levin.batallones@sei713.com')
        self.assertEqual(self.martin.email, 'martin.briceno@sei713.com')
        self.assertEqual(self.alice.email, 'alice.huh@sei713.com')
        self.assertEqual(self.rome.email, 'rome.bell@sei713.com')
        

    def test_fullname(self):
        self.assertEqual(self.alice.fullname, 'Alice Huh')

    def test_raise_amount(self):
        self.rome.apply_raise()
        self.assertEqual(self.rome.pay, 115000)

if __name__ == '__main__':
    unittest.main()