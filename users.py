from malls import malls

users = {}


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    print("\nSelect Role:")
    print("1. Customer")
    print("2. Admin")
    print("3. Owner")

    role_choice = input("Choice: ")

    if role_choice == "1":
        role = "customer"
    elif role_choice == "2":
        role = "admin"
    elif role_choice == "3":
        role = "owner"
    else:
        print("Invalid role")
        return

    if username in users:
        print("User already exists")
        return

    mall_choice = None

    if role == "admin":
        print("\nAssign admin to a mall:")
        for key, mall in malls.items():
            print(f"{key}. {mall['name']}")

        mall_choice = input("Select mall: ")

        if mall_choice in malls:
            if malls[mall_choice]["admin"] is None:
                malls[mall_choice]["admin"] = username
            else:
                print("Mall already has an admin")
                return
        else:
            print("Invalid mall")
            return

    users[username] = {
        "password": password,
        "role": role,
        "mall": mall_choice
    }

    print("Registration successful")


def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        return username
    else:
        print("Invalid login")
        return None