""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util
from view.terminal import get_inputs

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

# def read_sales_data():
#     with open(DATAFILE, "r") as file:
#         return file.read()
def list_transactions():
    sales = data_manager.read_table_from_file(DATAFILE)
    return sales
#print(list_transactions())

def get_add_transaction(new_transaction):
    data = list_transactions()
    #new_transaction = get_inputs("Customer:\n", "Product:\n", "Price:\n", "Date:\n")
    new_id = util.generate_id()
    new_transaction.insert(0, new_id)
    data.append(new_transaction)
    data_manager.write_table_to_file(DATAFILE, data)

#print(add_transaction(new_transaction))

def check_id(ID):
    data = list_transactions()
    for i in data:
        if i[0] == ID:
            return ID
    return None
        
def replace_uptransaction(replace_item, option, user_id):
    data = list_transactions()
    for item in data:
        if item[0] == user_id:
            item[int(option)] = replace_item
    data_manager.write_table_to_file(DATAFILE, data)



def delete_transaction(id):
    # view.print_error_message("Not implemendef list_transactions():ted yet.")
    x=list_transactions()
    for index,line in enumerate(x):
        if line[0]==id:
            x.pop(index)
    data_manager.write_table_to_file(DATAFILE,x)


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    pass
