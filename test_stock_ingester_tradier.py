from pprint import pprint
from unittest import TestCase
import stock_ingester_tradier as si

class TestStockIngester(TestCase):
    def test_get_past_days(self):
        ingester = si.StockIngester()
        result = ingester.get_past_days("AAPL", "2020-11-01", "2020-11-11")
        pprint(result)
        #Test for presence of last date
        self.assertTrue("2020-11-11" in result)
        # Test for number of entries
        self.assertEqual(8, len(result))
