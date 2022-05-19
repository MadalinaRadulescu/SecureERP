""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["Id", "Name", "Email", "Subscribed"]

def list_customers():
    data = data_manager.read_table_from_file(DATAFILE)
    return data

def get_add_customer(new_customer):
    data = list_customers()
    new_id = util.generate_id()
    new_customer.insert(0, new_id)
    data.append(new_customer)
    data_manager.write_table_to_file(DATAFILE, data)

def replace_updatecustomer(replace_item, option, user_id):
    data = list_customers()
    for item in data:
        if item[0] == user_id:
            item[int(option)] = replace_item
    data_manager.write_table_to_file(DATAFILE, data)

def check_id(ID):
    data = list_customers()
    for i in data:
        if i[0] == ID:
            return ID
    return None


def delete_customer(id):
    x = list_customers()
    for index,line in enumerate(x):
        if line[0]==id:
            x.pop(index)
    data_manager.write_table_to_file(DATAFILE, x)


def get_subscribed_emails():
    data = list_customers()
    list_emails = []
    for item in data:
        if item[3] == "1":
            list_emails.append(item[2])
    return list_emails