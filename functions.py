import requests
import json

import streamlit

API_KEY = streamlit.secrets["api_key"]


def query(selected_option_base,selected_option_target):
    response = requests.get(
        f'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_wLXMisOVTwUxv4MIbt3cX4cplz70bPHkl00jfSeE&currencies={selected_option_target}&base_currency={selected_option_base}')
    response_data = json.loads(response.content)
    result = response_data['data'][selected_option_target]
    return result

def get_available_currencies():
    response = requests.get(f'https://api.freecurrencyapi.com/v1/currencies?apikey={API_KEY}&currencies=')
    response_data = json.loads(response.content)
    currency_codes = list(response_data['data'].keys())
    return currency_codes
