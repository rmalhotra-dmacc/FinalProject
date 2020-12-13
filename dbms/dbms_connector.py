"""
Program: dbms_connector.py
Author: Rajiv Malhotra
Last Modified Date: 11/25/2020

Program to create DB and Employee table. It also has code to select & delete one or all employee records
"""

import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Create Connection to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):

    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS employee (
                                        ssn text PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL,
                                        age integer NOT NULL,
                                        start_dt date NOT NULL,
                                        contribution_pct decimal NOT NULL,
                                        account_balance decimal NOT NULL
                                ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create employee table
        create_table(conn, sql_create_employee_table)
    else:
        print("Unable to connect to " + str(database))


def create_employee(conn, employee):
    """Create a new employee for table
    :param conn: database connection
    :param employee: employee details
    :return: none
    """
    sql = ''' INSERT INTO employee(ssn, firstname, lastname, age, start_dt, contribution_pct, account_balance)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, employee)
 

def update_employee_contrib_pct(conn, employee):
    """Update contribution percentage of employee
    :param conn: database connection
    :param employee: employee details
    :return: none
    """
    sql = ''' UPDATE employee
              SET firstname = ? ,
                  lastname = ? ,
                  age = ? ,
                  start_dt = ? ,
                  contribution_pct = ? ,
                  account_balance = ?
              WHERE ssn = ?'''
    cur = conn.cursor()
    cur.execute(sql, employee)


def select_one_employee(conn, ssn):
    """Selects an employee based on ssn
    :param conn: database connection
    :param ssn: ssn of employee
    :return: employee details
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee WHERE ssn=?", (ssn,))
    rows = cur.fetchall()
    return rows  # return the rows


def select_all_employees(conn):
    """Query all rows of employee table
    :param conn: the connection object
    :return: list of all employees
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    return rows  # return the rows


def delete_employee(conn, ssn):
    """Delete an employee based on ssn
    :param conn: database connection
    :param ssn: ssn of employee
    :return: none
    """
    sql = 'DELETE FROM employee WHERE ssn=?'
    cur = conn.cursor()
    cur.execute(sql, (ssn,))


def delete_all_employees(conn):
    """Delete all employees from the table
    :param conn: database connection
    :return: none
    """
    sql = 'DELETE FROM employee'
    cur = conn.cursor()
    cur.execute(sql)


# driver
"""
if __name__ == '__main__':
    conn = create_connection("Employee401K.db") # Create DB Connection
    create_tables("Employee401K.db")  # Create Employee DB table
    with conn:
        employee = ("123-45-6789","Rajiv","Malhotra",34, '12/01/2011', 8.0, 275000.00)
        build_employee = create_employee(conn, employee)
        
        emp1 = "123-45-6789"
        print("Show details of one employee {}".format(emp1)) 
        rows = select_one_employee(conn, emp1)  # print all employees
        for row in rows:
            print(row)

        print("Show all Employee details") 
        rows = select_all_employees(conn)  # print all employees
        for row in rows:
            print(row)

        delete_employee(conn, emp1)
"""
