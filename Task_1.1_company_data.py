from sec_edgar_downloader import Downloader
import yfinance as yf
import time
from datetime import datetime
import requests


def ipo_year(ticker):
    try:
        #historical data
        historical_data = yf.download(ticker, start="1950-01-01", end="2024-01-01")

        #first trade date (index of the first non-NaN value)
        first_trade_date = historical_data.index[0]

        #IPO year from the first trade date
        ipo_year = first_trade_date.year

        return ipo_year
    
    except Exception as e:

        print(f"Error retrieving IPO year for {ticker}: {e}")

        return None

def _10_k_filings(ticker, start_year, end_year):

    #Initializing Downloader
    downloader = Downloader("IITBombay", "parikhkhanjan@gmail.com")

    #getting IPO year so that if IPO is after 1995 it can collect filing from that year
    ipo = int(ipo_year(ticker))

    #adjust start year if company was listed after 1995
    start_year = max(start_year,ipo)
    date_str = str(start_year) + '-01-01'
    print(date_str)
    start_date = datetime.strptime(date_str, '%Y-%m-%d')

    #loop through each year and download 10-K filing
    for year in range(start_year,end_year+1):
        #download 10-K filings of given year and ticker
        downloader.get_10k_filings(ticker, 1)
        print(f'Downloaded 10-K filing for {ticker} for the year {year}')

        time.sleep(60)

        # except Exception as e:
        #     print(f'Error downloading 10-K filing for {ticker} for the year {year}')

ticker = 'NVDA'
start_year = 1995
end_year = 2023

_10_k_filings(ticker, start_year, end_year)


