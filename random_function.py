import random

def validate_numbers(numbers):
    try:
        for is_num in numbers:
            int(is_num)
        return True
    except(ValueError, TypeError):
        return False

def get_rand_number(min, max):
    return random.randint(min, max)

def get_numbers_ticket(min, max, quantity):
    inp_numbers = [min, max, quantity]

    if not validate_numbers(inp_numbers):
        return "min, max, quanity must be integers"
    
    min = int(min)
    max = int(max)
    quantity = int(quantity)
    
    if 1 <= min <= max <= 1000 and (max - min) >= quantity - 1:
        rand_set = set()

        while len(rand_set) < quantity:
            rand_set.add(get_rand_number(min, max))

        return sorted(rand_set)
    else:
        return """Can not generate numbers:
    Range of values must be higher as quantity and max value must be lower or equal 1000"""
