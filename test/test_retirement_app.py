import unittest
import os
from dbms import dbms_connector as db
from classes import Employee as emp

os.chdir('../dbms')
conn = db.create_connection("Employee401K.db")  # Create DB Connection


class MyTestCase(unittest.TestCase):

    def test_select_one_employee_found(self):
        self.assertEqual([('123-45-6789', 'Rajiv', 'Malhotra', 34, '12/01/2011', 8.0, 125000.00)],
                         db.select_one_employee(conn, "123-45-6789"))

    def test_select_one_employee_not_found(self):
        self.assertEqual([], db.select_one_employee(conn, '111-11-1111'))

    def setUp(self):
        self.employee = emp.Employee("123-45-6789", "Rajiv", "Malhotra", 34, "12/01/2011", 8.0, 125000.00)

    def tearDown(self):
        del self.employee

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.employee.ssn, '123-45-6789')
        self.assertEqual(self.employee.first_name, 'Rajiv')
        self.assertEqual(self.employee.last_name, 'Malhotra')
        self.assertEqual(self.employee.age, 34)
        self.assertEqual(self.employee.start_dt, "12/01/2011")
        self.assertEqual(self.employee.contrib_pct, 8.0)
        self.assertEqual(self.employee.acct_balance, 125000.00)

    def test_initial_all_attributes(self):
        employee = emp.Employee("123-45-6789", "Rajiv", "Malhotra", 34, "12/01/2011", 8.0, 125000.00)
        assert employee.ssn == '123-45-6789'
        assert employee.first_name == 'Rajiv'
        assert employee.last_name == 'Malhotra'
        assert employee.age == 34
        assert employee.start_dt == '12/01/2011'
        assert employee.contrib_pct == 8.0
        assert employee.acct_balance == 125000.00

    def test_employee_not_created_ssn_error(self):
        with self.assertRaises(ValueError):
            emp1 = emp.Employee("123-XX-6789", "Rajiv", "Malhotra", 34, "12/01/2011", 8.0, 125000.00)

    def test_employee_not_created_fname_error(self):
        with self.assertRaises(ValueError):
            emp1 = emp.Employee("123-45-6789", "123Rajiv", "Malhotra", 34, "12/01/2011", 8.0, 125000.00)

    def test_employee_not_created_lname_error(self):
        with self.assertRaises(ValueError):
            emp1 = emp.Employee("123-45-6789", "Rajiv", "%%Malhotra", 34, "12/01/2011", 8.0, 125000.00)

    def test_employee_not_created_age_error(self):
        with self.assertRaises(ValueError):
            emp1 = emp.Employee("123-45-6789", "Rajiv", "Malhotra", -15, "12/01/2011", 8.0, 125000.00)

    def test_employee_not_created_start_dt_error(self):
        with self.assertRaises(ValueError):
            emp1 = emp.Employee("123-45-6789", "Rajiv", "Malhotra", 34, "17/01/2011", 8.0, 125000.00)

    def test_employee_not_created_contrib_pct_error(self):
        with self.assertRaises(ValueError):
            emp1 = emp.Employee("123-45-6789", "Rajiv", "Malhotra", 34, "12/01/2011", 'xyz', 125000.00)

    def test_employee_not_created_acct_balance_error(self):
        with self.assertRaises(ValueError):
            emp1 = emp.Employee("123-45-6789", "Rajiv", "Malhotra", 34, "12/01/2011", 8.0, 'forty thousand')

    def test_calculate_retirement_balance(self):
        employee = emp.Employee("123-45-6789", "Rajiv", "Malhotra", 34, "12/01/2011", 8.0, 125000.00)
        assert employee.calculate_retirement_balance() == "589,037.53"


if __name__ == '__main__':
    unittest.main()
