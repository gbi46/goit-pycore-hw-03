from datetime import datetime, timedelta

def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

def date_to_string(date):
    return date.strftime("%d.%m.%Y")

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    days_ahead += 7
    
    return start_date + timedelta(days=days_ahead)

def string_to_date(str):
    return datetime.strptime(str, "%Y.%m.%d").date()

def get_upcoming_birthdays(data, days=7):
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in data:
        if not user == None:
            birthday = string_to_date(user['birthday'])
            
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year = today.year+1)
            
            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year = adjust_for_weekend(birthday_this_year)
                
                congratulation_date_str = date_to_string(birthday_this_year)
                
                upcoming_birthdays.append({"name": user['name'], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays