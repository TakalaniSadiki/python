from users import register, login, users
from utils import customer_menu, admin_menu, owner_menu


def main():
    while True:
        print("\nParking System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()

            if user:
                role = users[user]["role"]

                if role == "customer":
                    customer_menu(user)
                elif role == "admin":
                    admin_menu(user)
                elif role == "owner":
                    owner_menu()

        elif choice == "3":
            break


main()