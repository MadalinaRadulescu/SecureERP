from dataclasses import dataclass
from model.crm.crm import HEADERS
from model.sales import sales
from view import terminal as view


def list_transactions():
    data = sales.list_transactions()
    view.print_table(sales.HEADERS, data)


def add_transaction():
    new_transaction = view.get_inputs(sales.HEADERS[1:])
    sales.get_add_transaction(new_transaction)
    


def update_transaction():
    while True:
        ID = view.get_input("enter ID: ")
        user_id = sales.check_id(ID)
        if user_id == None:
            view.print_error_message("Not a valid ID")
        option = view.get_input("Choose what you want to modify: \n1. Customer\n2. Product\n3.Price\n4. Date ")
        if option == "1" or option == "2" or option == "3" or option == "4": 
            replace_item = view.get_input("Enter replacement: ")
            sales.replace_uptransaction(replace_item, option, user_id) 
            break
        else:
            view.print_message("Not a valid option")

        


def delete_transaction():
    entry_id = view.get_input("Enter ID: ")
    id = sales.check_id(entry_id)
    if id == None:
        view.print_error_message("Not a valid id.")
    sales.delete_transaction(id)
    
    

def get_biggest_revenue_transaction():
    #list_transactions()
    x = sales.get_biggest_revenue_transaction()
    view.print_the_biggest_price(x)


def get_biggest_revenue_product():
    #list_transactions() 
    x = sales.get_biggest_revenue_product()
    view.print_the_biggest_product(x)


def count_transactions_between():
    year1 = view.get_input("Enter first year: ")
    year2 = view.get_input("Enter second year: ")
    number_transaction = sales.count_transactions_between(year1, year2)
    view.print_count_transaction(number_transaction)


def sum_transactions_between():
    year1 = view.get_input("Enter first year: ")
    year2 = view.get_input("Enter second year: ")
    sum_transaction = sales.sum_transactions_between(year1, year2)
    view.print_sum_transaction(sum_transaction)


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
