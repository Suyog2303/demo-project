# Primitive arguments
def calculate_commission_py(volume):
    fee = 0.0
    bonus = 0.0

    if (volume > 200000):
        rate = 0.15
        bonus = 1000
    else:
        if volume > 100000:
            rate = 0.123
        else:
            if volume > 50000:
                rate = 0.1
            else:
                if volume > 10000:
                    rate = 0.075
                else:
                    if volume > 5000:
                        rate = 0.05
                    else:
                        if volume > 0:
                            rate = 0.025
                        else:
                            rate = 0
                            fee = 50.0
    commission = int(volume * rate * 100) / 100.0
    award = commission + bonus - fee
    return award

# Structured arguments
def get_client_age_generation_py(client):
    if client['age'] <= 18:
        return "Gen.Z"
    elif client.get("age") > 18 and client["age"] < 34:
        return "Gen.Y"
    elif client["age"] >= 34:
        return "Gen.X"
    else:
        return None


# Structured arguments with deep nesting
def get_client_score_py(client):
    if (client.get('name')['firstname'] is not None) and (client['name']['lastname'] is not None):
        amount_spend = 0
        dates = []
        for i in range(len(client["orders"])):
            if client["orders"][i]["order_id"] != -1 and client["orders"][i]["currency"] == "EUR":
                dates.append(client["orders"][i]["date"])
                amount_spend += client["orders"][i]["price"]
        return amount_spend / len(dates)
    else:
        return 0