def calculate_deal_score(truck):

    score = 100

    price = truck.get("price", 0)
    mileage = truck.get("mileage", 0)
    year = truck.get("year", 0)

    # price evaluation
    if price > 50000:
        score -= 30
    elif price > 40000:
        score -= 20
    elif price > 30000:
        score -= 10

    # mileage evaluation
    if mileage > 600000:
        score -= 25
    elif mileage > 400000:
        score -= 15
    elif mileage > 300000:
        score -= 5

    # year evaluation
    if year < 2015:
        score -= 20
    elif year < 2018:
        score -= 10

    return max(score, 0)


if __name__ == "__main__":

    sample_truck = {
        "brand": "MAN",
        "model": "TGX",
        "price": 32000,
        "year": 2019,
        "mileage": 420000
    }

    score = calculate_deal_score(sample_truck)

    print("Truck:", sample_truck)
    print("Deal Score:", score)
