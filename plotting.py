import plotly.graph_objects as go

def plot_signals(df, signals):
    """
    Plots the stock data with buy/sell signals.

    Parameters:
        df (pd.DataFrame): The stock data.
        signals (pd.Series): The buy/sell signals.

    Returns:
        go.Figure: The plotly figure object.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['price'], mode='lines', name='Price'))
    fig.add_trace(go.Scatter(x=df.index, y=df['short_mavg'], mode='lines', name='Short Moving Average'))
    fig.add_trace(go.Scatter(x=df.index, y=df['long_mavg'], mode='lines', name='Long Moving Average'))
    fig.add_trace(go.Scatter(x=signals[signals=='Buy'].index, y=df[signals=='Buy']['short_mavg'], mode='markers', name='Buy', marker_symbol='triangle-up'))
    fig.add_trace(go.Scatter(x=signals[signals=='Sell'].index, y=df[signals=='Sell']['short_mavg'], mode='markers', name='Sell', marker_symbol='triangle-down'))

    fig.update_layout(title='Price and Buy/Sell Signals', xaxis_title='Date', yaxis_title='Price')
    return fig