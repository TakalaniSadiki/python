import time
from malls import malls, calculate_fee

parking_records = {}
parking_history = []
payment_history = []


def select_mall():
    print("\nSelect Mall:")
    for key, mall in malls.items():
        available = mall["capacity"] - mall["occupied"]
        print(f"{key}. {mall['name']} ({available} available)")

    choice = input("Choice: ")

    if choice in malls:
        if malls[choice]["occupied"] < malls[choice]["capacity"]:
            return choice
        else:
            print("Mall is full")
    else:
        print("Invalid choice")

    return None


def vehicle_entry(username):
    if username in parking_records:
        print("Already parked")
        return

    mall_id = select_mall()

    if mall_id:
        malls[mall_id]["occupied"] += 1

        parking_records[username] = {
            "entry_time": time.time(),
            "exit_time": None,
            "mall": mall_id
        }

        print("Vehicle parked successfully")


def vehicle_exit(username):
    if username in parking_records:
        record = parking_records[username]

        record["exit_time"] = time.time()

        fee = calculate_fee(
            record["mall"],
            record["entry_time"],
            record["exit_time"]
        )

        malls[record["mall"]]["occupied"] -= 1

        parking_history.append({
    "user": username,
    "mall": record["mall"],
    "entry": time.ctime(record["entry_time"]),
    "exit": time.ctime(record["exit_time"]),
    "fee": fee

        })

        print(f"Fee: R{fee}")
    else:
        print("No active parking")


def view_fee(username):
    if username in parking_records:
        record = parking_records[username]

        if record["exit_time"]:
            fee = calculate_fee(
                record["mall"],
                record["entry_time"],
                record["exit_time"]
            )
            print(f"Current fee: R{fee}")
        else:
            print("Exit first to calculate fee")
    else:
        print("No active record")


def make_payment(username):
    if username in parking_records:
        record = parking_records[username]

        if record["exit_time"]:
            fee = calculate_fee(
                record["mall"],
                record["entry_time"],
                record["exit_time"]
            )

            payment_history.append({
                "user": username,
                "amount": fee,
                "time": time.ctime()
            })

            print(f"Payment of R{fee} successful")
            del parking_records[username]
        else:
            print("Exit first")
    else:
        print("No payment due")


def view_history(username):
    print("\nParking History:")
    for record in parking_history:
        if record["user"] == username:
            print(record)

    print("\nPayment History:")
    for payment in payment_history:
        if payment["user"] == username:
            print(payment)