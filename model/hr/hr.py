""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def list_employees():
    hr_table = data_manager.read_table_from_file(DATAFILE)
    return hr_table

def get_add_employee():
    hr_table = data_manager.read_table_from_file(DATAFILE)
    hr_table.insert(0, HEADERS)
    new_employee = []
    id = util.generate_id()
    name = input("Enter name: ")
    birthdate = input("Enter birthate [YYYY-MM-DD]: ")
    department = input("Enter department: ")
    clearence = input("Clearence level: ")
    
    new_employee.append(id)
    new_employee.append(name)
    new_employee.append(birthdate)
    new_employee.append(department)
    new_employee.append(clearence)
    hr_table.append(new_employee)
    data_manager.write_table_to_file(DATAFILE, hr_table)

#def update_employee():
    #hr_table = data_manager.read_table_from_file(DATAFILE)
    #hr_table.insert(0, HEADERS)
    #for employe in hr_table:
        #if employe[0] == id:


def delete_employee(id):
    hr_table = data_manager.read_table_from_file(DATAFILE)
    hr_table.insert(0, HEADERS)
    for index, employe in enumerate(hr_table):
        if employe [0] == id:
            hr_table.pop(index)
    data_manager.write_table_to_file(DATAFILE, hr_table)





    