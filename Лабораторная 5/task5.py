import random
from random import sample
import string


def get_random_password() -> str:
    w = string.ascii_uppercase + string.digits + string.ascii_lowercase
    random_pass = ""
    x = random.sample(w, 8)
    random_pass += ''.join(x)

    return random_pass


print(get_random_password())
