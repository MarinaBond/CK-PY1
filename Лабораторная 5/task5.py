import random
from random import sample
import string


def get_random_password(n=8) -> str:
    w = string.ascii_uppercase + string.digits + string.ascii_lowercase
    random_pass = ""
    x = random.sample(w, n)
    random_pass += ''.join(x)

    return random_pass


print(get_random_password())
