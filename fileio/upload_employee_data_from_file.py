"""
Program: upload_employee_data_from_file.py
Author: Rajiv Malhotra
Last Modified Date: 11/25/2020

Program reads from a file and populates the Employee database table. Any invalid records are written to Employee_Errors.txt file
"""

import os
import csv
from dbms import dbms_connector as db
from classes import Employee as emp

ERROR_FILE = "Employee_Errors.txt"
IOERROR_MSG = 'Cannot open file on file system'


class upload_from_file:

    def __init__(self):
        """Constructor"""
        pass

    def write_errors_to_file(self, *args):
        """
        Function accepts a tuple to be added to the end of a file
        :param args: tuple
        :return: None
        """
        f = open(ERROR_FILE, "a")
        for arg in args:
            f.write("{}\t".format(arg))
        f.write("\n")
        f.close()

    def upload_employee_data_from_file(self):
        """Reads data from file and uploads to Database"""
        os.chdir('../dbms')
        conn = db.create_connection("Employee401K.db")  # Create DB Connection

        with open('../data/EmployeeFile.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                try:
                    employee_object = emp.Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                except ValueError as err:
                    self.write_errors_to_file(row[0], row[1], row[2], row[3], row[4], row[5], row[6], err)
                else:
                    employee_detail = (employee_object.ssn, employee_object.first_name, employee_object.last_name,
                                       employee_object.age, employee_object.start_dt, employee_object.contrib_pct,
                                       employee_object.acct_balance)
                    db.create_employee(conn, employee_detail)
            conn.commit()


# drivers
"""
upload_employee = upload_from_file()
os.chdir('../dbms')
conn = db.create_connection("Employee401K.db")
db.create_tables("Employee401K.db")  # Create DB tables
upload_employee1 = upload_employee.upload_employee_data_from_file()

with conn:
    rows = db.select_all_employees(conn)  # print all employees
    for row in rows:
        print(row)
"""
