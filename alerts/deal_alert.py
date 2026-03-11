def check_for_alert(truck, score):

    ALERT_THRESHOLD = 85

    if score >= ALERT_THRESHOLD:

        alert = {
            "brand": truck.get("brand"),
            "model": truck.get("model"),
            "price": truck.get("price"),
            "year": truck.get("year"),
            "mileage": truck.get("mileage"),
            "score": score
        }

        return alert

    return None


if __name__ == "__main__":

    sample_truck = {
        "brand": "MAN",
        "model": "TGX",
        "price": 32000,
        "year": 2019,
        "mileage": 420000
    }

    sample_score = 90

    alert = check_for_alert(sample_truck, sample_score)

    if alert:
        print("ALERT:", alert)
    else:
        print("No good deal found")
