from date_functions import get_days_from_today
from random_function import get_numbers_ticket
from re_functions import normalize_phone

if __name__ == "__main__":
    print("\n === Task 1. Test date functions: ===")
    print("*** With later, then today: 20.06 ***")
    print(get_days_from_today("2025-06-20"))
    print("*** With earlier, then today: 9.06 ***")
    print(get_days_from_today("2025-06-09"))

    print("\n === Task 2. Test random function === ")
    print("*** Numbers for ticket: ***")
    print(get_numbers_ticket(1, 49, 6))

    print("\n === Task3. Test regexp functions == ")
    raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("\n Normalized telefon numbers for SMS:", sanitized_numbers)