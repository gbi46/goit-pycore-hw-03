from datetime import datetime

def get_date_string(date):
    return datetime.strptime(date, "%Y-%m-%d")

def validate_date_format(date):
    try:
        date_str = bool(get_date_string(date))
    except ValueError:
        print("Incorrect date format")
        date_str = False

    return date_str

def string_to_date(date_str):
    return get_date_string(date_str).date()

def get_days_from_today(date):
    if validate_date_format(date):
        today = datetime.today().toordinal()
        inp_date = string_to_date(date).toordinal()

        return today - inp_date
    else:
        return "Error: date format must be YYYY-MM-DD"