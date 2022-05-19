from cProfile import label
from wsgiref import headers
from model.hr import hr
from view import terminal as view
import datetime


def list_employees():
    hr_table = hr.list_employees()
    headers = hr.HEADERS
    view.print_table(headers, hr_table)


def add_employee():
    new_employee = view.get_inputs(hr.HEADERS[1:])
    hr.get_add_employee(new_employee)


def update_employee():
    hr_table = hr.list_employees()
    id = view.get_input("ID or exit ")
    if id == 'exit':
        quit()
    else:
        while True:
            for item in hr_table:
                if item[0] == id:
                    update_employee_data = view.get_input("Choose what you want to update? 1: name | 2: date of birth | 3: department | 4: clearance | 0: Exit  >")
                    if update_employee_data == "1":
                        name = view.get_input("\nNew name: ")
                        item[1] = name
                    if update_employee_data == "2":
                        d_birth = view.get_input("\nNew date of birth: ")
                        item[2] = d_birth
                    if update_employee_data == "3":
                        depart = view.get_input("\nNew department: ")
                        item[3] = depart
                    if update_employee_data == "4":
                        clr = view.get_input("\nNew clearance: ")
                        item[4] = clr
                    if update_employee_data == "0":
                        display_menu()
            hr.get_update_employee(hr_table)
            new_update = view.get_input("\nUpdate again ? y/n : ")
            if new_update == "y":
                True
            else:
                break


def delete_employee():
    hr_table = hr.list_employees()
    id = view.get_input("ID or exit ")
    for item in hr_table:
        if item[0] == id:
            hr_table.remove(item)
        if id == "exit":
            display_menu
    hr.get_update_employee(hr_table)
    view.get_input('\nPress Enter for menu')


def get_oldest_and_youngest():
    hr_table = hr.list_employees()
    sorted_hr_table = sorted(hr_table, key = hr.take_second)
    old_young = [sorted_hr_table[0][1], sorted_hr_table[-1][1]]
    view.print_message('Oldest:       Youngest:')
    view.print_oldest_youngest(old_young[0], old_young[1])
    view.get_input('\nPress Enter for menu')


def get_average_age():
    now = datetime.datetime.now().year
    hr_table = hr.list_employees()
    dates = [int(date[2][0:4]) for date in hr_table]
    average_birth = sum(dates)//len(dates)
    average_age = now - average_birth
    view.print_average_age(average_age)
    view.get_input('\nPress Enter for menu')


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    clearance = view.get_input("Enter Clearance: ")
    x = hr.count_employees_with_clearance(clearance)
    view.print_employees_with_clearance(clearance, x)
    
    


def count_employees_per_department():
    employeer_per_dep = hr.count_employees_per_department()
    view.print_employees_per_dep(employeer_per_dep)



def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
