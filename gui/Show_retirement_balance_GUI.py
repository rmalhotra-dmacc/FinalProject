"""
Program: Show_retirement_balance_GUI.py
Author: Rajiv Malhotra
Last Modified Date: 11/25/2020

GUI to display Employee record details including total account balance at retirement.
"""

import tkinter
import tkinter.font as tkfont
import os
from dbms import dbms_connector as db
from classes import Employee as emp

database = 'Employee401K.db'


class show_retirement_acct_balance_GUI:
    """ Class dbmsGUI """

    def __init__(self, window):
        os.chdir('../dbms')
        self.conn = db.create_connection(database)
        window.title("Show Retirement account Balance GUI")
        window.geometry("500x500")
        self.valid_employee = False
        # --------------------
        self.show_retirement_record = tkinter.Button(window, state=tkinter.DISABLED, text="Enter Employee SSN")
        self.show_retirement_record.pack()
        self.e_ssn = tkinter.Entry(window)
        self.e_ssn.pack()
        # --------------------
        self.b_view_employee = tkinter.Button(window, text="View Employee", command=lambda: self.show_employee_record())
        self.b_view_employee.pack()
        # --------------------
        self.l_table_data = tkinter.Label(window, font=fontStyle)
        self.l_table_data.pack()
        # --------------------
        self.b_view_retirement_bal = tkinter.Button(window, text="Calculate Retirement Balance",
                                                    command=lambda: self.calculate_retirement_bal())
        self.b_view_retirement_bal.pack()
        # --------------------
        self.l_retirement_bal_data = tkinter.Label(window, font=fontStyle)
        self.l_retirement_bal_data.pack()
        # --------------------
        self.exit_button = tkinter.Button(window, text="Exit", command=app_window.destroy)
        self.exit_button.pack()
        # --------------------
        buttonexample1 = tkinter.Button(app_window, text="Increase", width=10,
                                        command=lambda: self.increase_label_font())
        buttonexample2 = tkinter.Button(app_window, text="Decrease", width=10,
                                        command=lambda: self.decrease_label_font())
        buttonexample1.pack(side=tkinter.RIGHT)
        buttonexample2.pack(side=tkinter.LEFT)

    def show_employee_record(self):
        """
        Function will show the employee record details
        """
        employee_ssn = (self.e_ssn.get())
        if employee_ssn == "":
            self.l_table_data.configure(text="Employee SSN can not be empty", foreground="red")
        else:
            row = db.select_one_employee(self.conn, employee_ssn)
            if row == []:
                self.l_table_data.configure(text="No results found for this employee", foreground="red")
            else:
                self.valid_employee = True
                emp_data = row[0]
                text = ""
                for col in emp_data:
                    text += "{}   ".format(col)
                text += "\n"
                self.l_table_data.configure(text=text, foreground="blue")

    def calculate_retirement_bal(self):
        """
        Function will show the approx employee account balance at retirement
        """
        employee_ssn = (self.e_ssn.get())
        if self.valid_employee != True:
            self.l_retirement_bal_data.configure(text="Employee record incorrect or not found", foreground="red")
        else:
            row = db.select_one_employee(self.conn, employee_ssn)
            emp_data = row[0]
            emp1 = emp.Employee(emp_data[0], emp_data[1], emp_data[2], emp_data[3], emp_data[4], emp_data[5],
                                emp_data[6])
            retirement_balance = emp1.calculate_retirement_balance()
            retirement_bal_text = "Your estimated Total Account Balance at Retirement will be ${}\n".format(
                retirement_balance)
            self.l_retirement_bal_data.configure(text=retirement_bal_text, foreground="blue")

    def increase_label_font(self):
        fontsize = fontStyle['size']
        labelExample['text'] = fontsize + 2
        fontStyle.configure(size=fontsize + 2)

    def decrease_label_font(self):
        fontsize = fontStyle['size']
        labelExample['text'] = fontsize - 2
        fontStyle.configure(size=fontsize - 2)


# driver
app_window = tkinter.Tk()
fontStyle = tkfont.Font(family="Lucida Grande", size=10)
labelExample = tkinter.Label(app_window, text="20", font=fontStyle)
dbms_app = show_retirement_acct_balance_GUI(app_window)
app_window.mainloop()
