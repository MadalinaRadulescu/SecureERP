import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    list_char = []
    for i in range(number_of_small_letters):
        char_l = random.choice(string.ascii_lowercase)
        list_char.append(char_l)

    for x in range(number_of_capital_letters):
        char_u = random.choice(string.ascii_uppercase)
        list_char.append(char_u)

    for y in range(number_of_digits):
        number = random.randrange(0,9)
        list_char.append(number)
    
    for z in range(number_of_special_chars):
        special_char = random.choice(allowed_special_chars)
        list_char.append(special_char)

    random.shuffle(list_char)
    ID = "".join(str(elem) for elem in list_char)
    return ID

# print(generate_id(number_of_small_letters=4,
#             number_of_capital_letters=2,
#             number_of_digits=2,
#             number_of_special_chars=2,
#             allowed_special_chars=r"_+-!"))




