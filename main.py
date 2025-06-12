from date_functions import get_days_from_today

if __name__ == "__main__":
    print(" === Task 1. Test date functions: ===")
    print("*** With later, then today: 20.06 ***")
    print(get_days_from_today("2025-06-20"))
    print("*** With earlier, then today: 9.06 ***")
    print(get_days_from_today("2025-06-09"))