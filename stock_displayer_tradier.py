from typing import Dict
import matplotlib.pyplot as plt


class StockDisplayer:

    def display_days(self, ticker, data_dict: Dict[str, int]):
        dates = list(data_dict.keys())
        values = list(data_dict.values())

        figure, axes = plt.subplots()

        axes.plot(dates, values, label = ticker)
        axes.set(title=f"Closing Stock Price for {ticker}", xlabel="Date", ylabel="Closing Prices")
        axes.tick_params(axis="x", labelrotation=270)

        plt.show()
