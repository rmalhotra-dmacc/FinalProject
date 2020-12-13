"""
Program: Employee.py
Author: Rajiv Malhotra
Last Modified Date: 11/25/2020

Program contains the Person and Employee class. It also validates the attributes of an Employee.
It also calculates the approx retirement balance for an employee.
"""

import re
import datetime


class Person:
    """Person class"""
    # Constructor
    def __init__(self, fname, lname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(fname) and name_characters.issuperset(lname)):
            raise ValueError
        self.first_name = fname
        self.last_name = lname

    def display(self):
        return self.first_name + ", " + self.last_name


class Employee(Person):
    """ Employee Class"""
    # Constructor
    def __init__(self, ssn, fname, lname, age, start_dt, contrib_pct, acct_balance):
        super().__init__(fname, lname)  # calls the base constructor
        self.ssn = ssn
        self.age = age
        self.start_dt = start_dt
        self.contrib_pct = contrib_pct
        self.acct_balance = acct_balance

    @property
    def ssn(self):
        return self._ssn

    @ssn.setter
    def ssn(self, value):
        ssn_format = re.compile('^\d{3}-\d{2}-\d{4}$')
        result = ssn_format.match(value)
        if result is None:
            raise ValueError("Incorrect SSN format, Please use xxx-xxx-xxxx")
        self._ssn = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            age_int = int(value)
        except:
            raise ValueError("Age must be an integer")
        else:
            if age_int < 15 or age_int > 75:
                raise ValueError("Employee age must be between 15 and 75")
            self._age = age_int


    @property
    def start_dt(self):
        return self._start_dt

    @start_dt.setter
    def start_dt(self, value):
        date_format = '%m/%d/%Y'
        try:
            validate_start_dt = datetime.datetime.strptime(value, date_format)
        except:
            raise ValueError("Incorrect Start date, should be in MM/DD/YYYY format")
        else:
            self._start_dt = value

    @property
    def contrib_pct(self):
        return self._contrib_pct

    @contrib_pct.setter
    def contrib_pct(self, value):
        try:
            value_float = float(value)
            self._contrib_pct = value
        except:
            raise ValueError("Contribution percentage should be a decimal")

    @property
    def acct_balance(self):
        return self._acct_balance

    @acct_balance.setter
    def acct_balance(self, value):
        try:
            value_float = float(value)
            self._acct_balance = value
        except:
            raise ValueError("Account Balance should be a decimal")

    def calculate_retirement_balance(self):
        """
        This function will return an approx retirement balance. It assumes a 60K annual salary and 5% rate of return per year
        :return: retirement balance
        """
        working_years_left = 65 - self.age
        contribution_per_year = 60000 * self.contrib_pct / 100
        retirement_balance = (self.acct_balance + contribution_per_year) * (1.05 ** working_years_left)
        return "{:,.2f}".format(retirement_balance)

    def display(self):
        return str(self.ssn) + ", " + Person.display(self) + ", " + str(self.age) + ", " + str(self.start_dt) + \
                ", " + str(self.contrib_pct) + ", $" + str(self.acct_balance)


# drivers
"""
try:
    emp1 = Employee("123-45-6789","Rajiv","Malhotra",39,'12/01/2011',8.0,125000.00)
    print(emp1.display())
    print(emp1.calculate_retirement_balance())
except ValueError as err:
    print(err)
"""
