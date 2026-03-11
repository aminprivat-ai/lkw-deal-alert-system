from scraper.truck_scraper import fetch_truck_listings
from analysis.deal_scoring import calculate_deal_score
from alerts.deal_alert import check_for_alert
from telegram.send_alert import send_telegram_alert


def run_system():

    trucks = fetch_truck_listings()

    for truck in trucks:

        score = calculate_deal_score(truck)

        alert = check_for_alert(truck, score)

        if alert:
            send_telegram_alert(alert)


if __name__ == "__main__":
    run_system()
