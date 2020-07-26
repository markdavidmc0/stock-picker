"""Stock picker that conectors to the marketstack API to obtain EOD stock prices."""
import json
import pickle
import requests

class Stock:
    """Stock object across all stock exchanges."""
    
    def __init__(self):
        self.date = "2019-02-01T00:00:00+0000"
        self.ticker = ""
        self.exchange = ""
        self.open = 0
        self.high = 168.98
        self.low = 165.93
        self.close = 166.52
        self.volume = 32668138.0

    def download_end_of_day(self):
        """Download end of day stock data object."""
        payload = {'access_key': '', 'symbols': 'AAPL'}
        output = requests.get('http://api.marketstack.com/v1/eod', params=payload)
        return output

    def get_tickers(self):
        """Get paginated stock symbols in batches of 100."""
        payload = {'access_key': ''}
        output = requests.get('http://api.marketstack.com/v1/tickers', params=payload)
        content = json.loads(output.content)
        return content

    def save_tickers(self, tickers: dict) -> None:
        """Save paginated stock symbols in batches of 100 to pickle."""
        pickle.dump(tickers, open( "tickers.p", "wb" ))
        
    def load_tickers(self) -> None:
        """Save paginated stock symbols in batches of 100 to pickle."""
        tickers = pickle.load(open( "tickers.p", "rb" ))
        x = 5

    def append_tickers(self, tickers: dict) -> None:
        """Append new tickers to existing list of tickers."""
        existing_tickers = pickle.load(tickers, open( "save.p", "rb" ))
        if isinstance(existing_tickers.data, list):
            pickle.dump(existing_tickers.data.append(tickers), open( "tickers.p", "rb" ))
        

if __name__== '__main__':
    # download = Fetcher().download_end_of_day()
    tickers = Stock().get_tickers()
    Stock().save_tickers(tickers)
    read_tickers = Stock().load_tickers()
    x = 5