from tabulate import tabulate
from wsgiref import headers


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title+":")
    for index in range(len(list_options)):
        print(f"({index})  {list_options[index]}")
        


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(headers, table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    print(tabulate(table, headers, tablefmt = 'fancy_grid'))


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(label)
    


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    string_inputs = []
    for label in labels:
        string_inputs.append(input(label))
    return string_inputs



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)

def print_count_transaction(number):
    print(f"Number of transactions: {number}")

def print_sum_transaction(number):
    print(f"Sum of transactions: {number}")

def print_the_biggest_price(number):
    print(f"The biggest price: {number}")

def print_the_biggest_product(message):
    print("The biggest transaction product: " + message)

def print_average_age(number):
    print(f"The average age is {number}")

def print_oldest_youngest(name1, name2):
    print(f"{name1}           {name2}")

def print_subscribed_emails(list):
    print("These are the subscribed emails: ")
    for item in list:
        print(item)

def print_employees_with_clearance(clr, number):
    print(f"Employees with clearance level {clr}: {number}")

def print_employees_per_dep(dict):
    print(dict)
