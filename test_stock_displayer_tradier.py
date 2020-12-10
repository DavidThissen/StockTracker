from unittest import TestCase

from stock_ingester_tradier import StockIngester
from stock_displayer_tradier import StockDisplayer


class TestStockDisplayer(TestCase):
    def test_display_days(self):
        """
        The only thing this test does is verify that the graph is created
        """
        # Create StockIngester object
        ingester = StockIngester()
        # Get new some stock data
        result_dict = ingester.get_past_days("AAPL", "2020-11-01", "2020-11-10")
        # Create StockDisplayer object so that we can create a graph
        sd = StockDisplayer()
        # Call display_days to visualize data
        sd.display_days("AAPL", result_dict)
        # Meaningless test
        self.assertTrue(True, True)
