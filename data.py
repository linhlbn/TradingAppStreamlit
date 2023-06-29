import yfinance as yf

def get_stock_data(stock, period='1y'):
    """
    Retrieves stock data from Yahoo Finance.

    Parameters:
        stock (str): The stock symbol.
        period (str): The time period for the data. Default is '1y'.

    Returns:
        pd.DataFrame: The stock data.
    """
    data = yf.download(stock, period=period)
    data['price'] = data['Close']
    return data
