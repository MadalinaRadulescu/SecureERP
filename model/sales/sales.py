""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

# def read_sales_data():
#     with open(DATAFILE, "r") as file:
#         return file.read()
def list_transactions():
    sales = data_manager.read_table_from_file(DATAFILE)
    return sales

def add_transaction():
    new_id = util.generate_id()
    pass


def update_transaction():
    view.print_error_message("Not implemented yet.")


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
