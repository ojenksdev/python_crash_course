import unittest
from employee import Employee

class TestEmployeeCase(unittest.TestCase):
    """Testing the employee class for accuracy."""

    def setUp(self):
        """Builds out the instance for the test methods."""
        self.new_employee = Employee('john', 'doe', 60000)


    def test_give_default_raise(self):
        """Does this method give the default raise amount?"""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 65000)

    def test_give_custom_raise(self):
        """Does this method give a customized raise amount?"""
        self.new_employee.give_raise(10000)
        self.assertEqual(self.new_employee.salary, 70000)

unittest.main()
