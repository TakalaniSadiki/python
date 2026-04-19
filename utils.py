from parking import (
    vehicle_entry,
    vehicle_exit,
    view_fee,
    make_payment,
    view_history,
    parking_records,
    parking_history
)
from malls import malls
from users import users


def customer_menu(username):
    while True:
        print("\n1. Entry")
        print("2. Exit")
        print("3. View Fee")
        print("4. Pay")
        print("5. View History")
        print("6. Logout")

        choice = input("Choice: ")

        if choice == "1":
            vehicle_entry(username)
        elif choice == "2":
            vehicle_exit(username)
        elif choice == "3":
            view_fee(username)
        elif choice == "4":
            make_payment(username)
        elif choice == "5":
            view_history(username)
        elif choice == "6":
            break


def admin_menu(username):
    mall_id = users[username]["mall"]

    while True:
        print("\n1. View Parked Cars")
        print("2. Capacity")
        print("3. Daily Activity")
        print("4. Logout")

        choice = input("Choice: ")

        if choice == "1":
            for user, record in parking_records.items():
                if record["mall"] == mall_id and record["exit_time"] is None:
                    print(user)

        elif choice == "2":
            mall = malls[mall_id]
            print(f"{mall['occupied']}/{mall['capacity']} occupied")

        elif choice == "3":
            for record in parking_history:
                if record["mall"] == mall_id:
                    print(record)

        elif choice == "4":
            break


def owner_menu():
    while True:
        print("\n1. View Malls")
        print("2. View Users")
        print("3. View Records")
        print("4. Logout")

        choice = input("Choice: ")

        if choice == "1":
            for mall in malls.values():
                available = mall["capacity"] - mall["occupied"]
                print(f"{mall['name']} | Available: {available}/{mall['capacity']}")

        elif choice == "2":
            for user, data in users.items():
                print(user, data)

        elif choice == "3":
            for record in parking_history:
                print(record)

        elif choice == "4":
            break