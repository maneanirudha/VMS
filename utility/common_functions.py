import random
import string

def generate_random_string():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(5))

def generate_random_purchase_order_number():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(25))

