from date_functions import get_days_from_today
from random_function import get_numbers_ticket

if __name__ == "__main__":
    print("\n === Task 1. Test date functions: ===")
    print("*** With later, then today: 20.06 ***")
    print(get_days_from_today("2025-06-20"))
    print("*** With earlier, then today: 9.06 ***")
    print(get_days_from_today("2025-06-09"))

    print("\n === Task 2. Test random function === ")
    print("*** Numbers for ticket: ***")
    print(get_numbers_ticket(1, 49, 6))