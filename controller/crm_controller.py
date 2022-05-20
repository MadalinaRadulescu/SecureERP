from model.crm import crm
from view import terminal as view


def list_customers():
    data = crm.list_customers()
    view.print_table(crm.HEADERS, data)


def add_customer():
    new_customer = view.get_inputs(crm.HEADERS[1:])
    crm.get_add_customer(new_customer)


def update_customer():
    while True:
        ID = view.get_input("enter ID: ")
        user_id = crm.check_id(ID)
        if user_id == None:
            view.print_error_message("Not a valid ID")
        option = view.get_input("Choose what you want to modify: \n1. Name\n2. Email\n3.Subscribed\n")
        if option == "1" or option == "2" or option == "3": 
            replace_item = view.get_input("Enter replacement: ")
            crm.replace_updatecustomer(replace_item, option, user_id) 
            break
        else:
            view.print_message("Not a valid option")


def delete_customer():
    entry_id = view.get_input("Enter ID: ")
    id = crm.check_id(entry_id)
    if id == None:
        view.print_error_message("Not a valid id.")
    crm.delete_customer(id)


def get_subscribed_emails():
    list_emails = crm.get_subscribed_emails()
    view.print_subscribed_emails(list_emails)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation\n")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
