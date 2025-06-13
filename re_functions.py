import re

def normalize_phone(phone_number):
    filtered_nummer = re.sub(r'[^\d+]', '', phone_number)

    if len(filtered_nummer) == 10:
        filtered_nummer = "+38" + filtered_nummer
    elif len(filtered_nummer) == 12:
        filtered_nummer = "+" + filtered_nummer
    
    return filtered_nummer 
