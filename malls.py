import math

malls = {
    "1": {
        "name": "Gateway Theatre of Shopping",
        "capacity": 250,
        "occupied": 0,
        "admin": None,
        "pricing": "flat",
        "rate": 15
    },
    "2": {
        "name": "Pavilion Shopping Centre",
        "capacity": 180,
        "occupied": 0,
        "admin": None,
        "pricing": "hourly",
        "rate": 10
    },
    "3": {
        "name": "La Lucia Mall",
        "capacity": 150,
        "occupied": 0,
        "admin": None,
        "pricing": "capped",
        "rate": 12,
        "cap": 60
    }
}


def calculate_fee(mall_id, entry_time, exit_time):
    mall = malls[mall_id]

    if mall["pricing"] == "flat":
        return mall["rate"]

    elif mall["pricing"] == "hourly":
        hours = math.ceil((exit_time - entry_time) / 3600)
        return hours * mall["rate"]

    elif mall["pricing"] == "capped":
        hours = math.ceil((exit_time - entry_time) / 3600)
        fee = hours * mall["rate"]
        return min(fee, mall["cap"])