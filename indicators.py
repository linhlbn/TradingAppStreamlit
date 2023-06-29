import pandas as pd
import ta

def moving_average_crossover(df, short_window, long_window):
    """
    Calculates moving average crossover signals.

    Parameters:
        df (pd.DataFrame): The stock data.
        short_window (int): The window for the short moving average.
        long_window (int): The window for the long moving average.

    Returns:
        pd.Series: The signals.
    """
    df['short_mavg'] = df['price'].rolling(window=short_window, min_periods=1, center=False).mean()
    df['long_mavg'] = df['price'].rolling(window=long_window, min_periods=1, center=False).mean()
    df['sma_signal'] = 0
    df.loc[df['short_mavg'] > df['long_mavg'], 'sma_signal'] = 'Buy'
    df.loc[df['short_mavg'] < df['long_mavg'], 'sma_signal'] = 'Sell'
    return df['sma_signal']

def rsi_bot(df, window, oversold, overbought):
    """
    Calculates RSI-based signals.

    Parameters:
        df (pd.DataFrame): The stock data.
        window (int): The window for RSI calculation.
        oversold (int): The oversold threshold for RSI.
        overbought (int): The overbought threshold for RSI.

    Returns:
        pd.Series: The signals.
    """
    df['rsi'] = ta.momentum.rsi(df['price'], window=window)
    df['rsi_signal'] = 0
    df.loc[df['rsi'] < oversold, 'rsi_signal'] = 'Buy'
    df.loc[df['rsi'] > overbought, 'rsi_signal'] = 'Sell'
    return df['rsi_signal']