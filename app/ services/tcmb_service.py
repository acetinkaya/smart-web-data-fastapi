import requests
from app.utils.xml_parser import parse_tcmb_xml

TCMB_URL = "https://www.tcmb.gov.tr/kurlar/today.xml"

def get_tcmb_currency_data():
    response = requests.get(TCMB_URL, timeout=10)
    response.raise_for_status()

    return parse_tcmb_xml(response.content)
