import xml.etree.ElementTree as ET
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

DATA_FILE = "data/currency_history.json"
CHART_FILE = "static/charts/usd_eur_chart.png"

def parse_tcmb_xml(xml_content):
    root = ET.fromstring(xml_content)

    result = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "currencies": {}
    }

    for currency in root.findall("Currency"):
        code = currency.get("CurrencyCode")

        forex_buying = currency.findtext("ForexBuying")
        forex_selling = currency.findtext("ForexSelling")
        name = currency.findtext("Isim")

        if forex_buying and forex_selling:
            result["currencies"][code] = {
                "name": name,
                "forex_buying": float(forex_buying),
                "forex_selling": float(forex_selling)
            }

    return result


def save_currency_history(data):
    os.makedirs("data", exist_ok=True)

    history = []

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []

    history.append(data)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)


def load_history():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def create_currency_chart():
    os.makedirs("static/charts", exist_ok=True)

    history = load_history()

    dates = []
    usd_values = []
    eur_values = []

    for item in history:
        dates.append(item["date"])

        currencies = item.get("currencies", {})

        if "USD" in currencies:
            usd_values.append(currencies["USD"]["forex_buying"])
        else:
            usd_values.append(None)

        if "EUR" in currencies:
            eur_values.append(currencies["EUR"]["forex_buying"])
        else:
            eur_values.append(None)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, usd_values, marker="o", label="USD")
    plt.plot(dates, eur_values, marker="o", label="EUR")
    plt.xticks(rotation=45)
    plt.title("TCMB Döviz Kuru Geçmişi")
    plt.xlabel("Tarih")
    plt.ylabel("Alış Kuru")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FILE)
    plt.close()

    return CHART_FILE
