import requests
from typing import Dict

API_KEY = "Ep720eRvs8yJteFPDlHpw0F5dB43"
ENDPOINT = "https://sandbox.tradier.com/v1/markets/history"

class StockIngester:
    """
    Class setting up methods for grabbing data fromm Covid API
    """
    def get_past_days(self, ticker, start_date, end_date) -> Dict[str, int] :
        """
        Get closing Apple stock prices for last 5 days, yesterday most recent
        :return: Dict[str, int]
        """

        # Create a dictionary for data
        result_dict = {}

        response = requests.get(ENDPOINT,
        params={'symbol': ticker, 'interval': 'daily', 'start': start_date,
        'end': end_date},
        headers={'Authorization': f'Bearer {API_KEY}', 'Accept': 'application/json'}
        )
        json_response = response.json()
        days_data_list = json_response["history"]["day"]
        result_dict = {day["date"]: day["close"] for day in days_data_list}

        return result_dict
