""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
import datetime

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def list_employees():
    hr_table = data_manager.read_table_from_file(DATAFILE)
    return hr_table

def get_add_employee(new_employee):
    hr_table = list_employees()
    id = util.generate_id()
    new_employee.insert(0, id)
    hr_table.append(new_employee)
    data_manager.write_table_to_file(DATAFILE, hr_table)

def get_update_employee(hr_table):
    data_manager.write_table_to_file(DATAFILE, hr_table)

# def delete_employee(id):
#     hr_table = data_manager.read_table_from_file(DATAFILE)
#     hr_table.insert(0, HEADERS)
#     for index, employe in enumerate(hr_table):
#         if employe [0] == id:
#             hr_table.pop(index)
#     data_manager.write_table_to_file(DATAFILE, hr_table)
#     pass
def take_second(elem):
    return elem[2]

def next_birthdays():
    hr_table = data_manager.read_table_from_file(DATAFILE)
    birthdays = []
    for item in hr_table:
        birthdays.append(item[2])
    return birthdays

def count_employees_with_clearance(clr):
    data = list_employees()
    count_clr = 0
    for item in data:
        if int(item[4]) >= int(clr):
            count_clr+=1
    return count_clr

def count_employees_per_department():
    data = list_employees()
    y = []
    for elem in data:
        y.append(elem[3])
    x =[0]
    dict_employees_per_department = dict(zip(y, x))
    # list_keys_for_dict = get_departament_list()
    for item in y:
        if item in dict_employees_per_department:
            dict_employees_per_department[item] += 1
        else:
            dict_employees_per_department[item] = 1
    return dict_employees_per_department
   






    