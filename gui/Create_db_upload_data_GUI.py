"""
Program: Create_db_upload_data_GUI.py
Author: Rajiv Malhotra
Last Modified Date: 11/25/2020

GUI for the Retirement App. It has functionality to create DB & Table, Upload Employees from a file and Display all Employees
"""

import tkinter
import tkinter.font as tkFont
import os
from dbms import dbms_connector as db
from fileio import upload_employee_data_from_file as fl
database = 'Employee401K.db'


class create_db_upload_data_GUI:
    """ Class create_db_upload_data_GUI """
    def __init__(self, window):
        os.chdir('../dbms')
        self.conn = db.create_connection(database)
        window.title("Retirement App")
        window.geometry("500x500")
        # --------------------
        self.b_create_table = tkinter.Button(window, text="Create Table", command=lambda: self.create_table())
        self.b_create_table.pack()
        # --------------------
        self.b_build_employee = tkinter.Button(window, text="Upload Employee data from file", command=lambda: self.upload_from_file())
        self.b_build_employee.pack()
        # --------------------
        self.b_view_employee = tkinter.Button(window, text="View Employee", command=lambda: self.view_employee())
        self.b_view_employee.pack()
        # --------------------
        self.l_table_data = tkinter.Label(window, font=fontStyle)
        self.l_table_data.pack()
        # --------------------
        self.exit_button = tkinter.Button(window, text="Exit", command=app_window.destroy)
        self.exit_button.pack()
        # --------------------
        buttonexample1 = tkinter.Button(app_window, text="Increase", width=10, command=lambda: self.increase_label_font())
        buttonexample2 = tkinter.Button(app_window, text="Decrease", width=10, command=lambda: self.decrease_label_font())
        buttonexample1.pack(side=tkinter.RIGHT)
        buttonexample2.pack(side=tkinter.LEFT)

    def view_employee(self):
        """
        This function will select all employees from DB and display them
        """
        rows = db.select_all_employees(self.conn)
        text = ""
        for row in rows:
            for col in row:
                text += "{}   ".format(col)
            text += "\n"
        self.l_table_data.configure(text=text, foreground="blue")

    def increase_label_font(self):
        fontsize = fontStyle['size']
        labelExample['text'] = fontsize+2
        fontStyle.configure(size=fontsize+2)

    def decrease_label_font(self):
        fontsize = fontStyle['size']
        labelExample['text'] = fontsize-2
        fontStyle.configure(size=fontsize-2)

    def create_table(self):
        """
        This function will create the Employee401K database
        """
        os.chdir('../dbms')
        conn = db.create_connection("Employee401K.db")  # Create DB Connection
        db.create_tables("Employee401K.db")  # Create DB tables
        self.l_table_data.configure(text="Table Creation Completed Successfully!", foreground="red")

    def upload_from_file(self):
        """
        This function will call the upload_employee_data_from_file to create employee records.
        """
        os.chdir('../dbms')
        conn = db.create_connection("Employee401K.db")  # Create DB Connection
        clear_table = db.delete_all_employees(self.conn)  # Delete all records from Employee table before loading
        self.conn.commit()
        try:
            upload_employee = fl.upload_from_file()
            upload_employee1 = upload_employee.upload_employee_data_from_file()
        except ValueError as err:
            print(err)
        else:
            self.conn.commit()
            self.l_table_data.configure(text="Employee Data from file uploaded Successfully!", foreground="red")


# driver
app_window = tkinter.Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
labelExample = tkinter.Label(app_window, text="20", font=fontStyle)
dbms_app = create_db_upload_data_GUI(app_window)
app_window.mainloop()
