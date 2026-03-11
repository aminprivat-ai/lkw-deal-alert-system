import requests

def fetch_truck_listings():

    url = "https://api.example.com/trucks"

    try:
        response = requests.get(url)
        data = response.json()

        trucks = []

        for truck in data:

            truck_data = {
                "brand": truck.get("brand"),
                "model": truck.get("model"),
                "price": truck.get("price"),
                "year": truck.get("year"),
                "mileage": truck.get("mileage")
            }

            trucks.append(truck_data)

        return trucks

    except Exception as e:
        print("Error fetching trucks:", e)
        return []


if __name__ == "__main__":

    listings = fetch_truck_listings()

    for truck in listings:
        print(truck)
