import requests


def send_telegram_alert(alert):

    TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
    TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

    message = f"""
🚛 DEAL FOUND

Brand: {alert['brand']}
Model: {alert['model']}
Price: {alert['price']} €
Year: {alert['year']}
Mileage: {alert['mileage']} km

Score: {alert['score']}
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, json=payload)
        print("Telegram alert sent")

    except Exception as e:
        print("Error sending Telegram alert:", e)


if __name__ == "__main__":

    sample_alert = {
        "brand": "MAN",
        "model": "TGX",
        "price": 32000,
        "year": 2019,
        "mileage": 420000,
        "score": 92
    }

    send_telegram_alert(sample_alert)
