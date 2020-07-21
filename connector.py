"""Stock picker that conectors to the marketstack API to obtain EOD stock prices."""
import requests

class Fetcher:
    """Downloads stock prices from a master index."""
    
    def __init__(self):
        self.data = []

    def download_end_of_day(self):
        """Download end of day stock data object."""
        payload = {'access_key': '', 'symbols': 'AAPL'}
        output = requests.get('http://api.marketstack.com/v1/eod', params=payload)
        return output
    

if __name__== '__main__':
    output = Fetcher().download_end_of_day()
    print(output)