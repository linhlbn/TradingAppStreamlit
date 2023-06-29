import streamlit as st
from data import get_stock_data
from indicators import moving_average_crossover, rsi_bot
from plotting import plot_signals


def run():

    # Set page configuration to wide layout and center alignment
    # st.set_page_config(layout="wide")
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container{
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Stock Trading App & Bot for Auto trading')

    # Use columns to create a responsive layout
    col1, col2 = st.columns([1, 2])

    try:
        with col1:
            selected_stock = st.selectbox('Select the stock', ('GOOGL', 'META', 'TSLA'))

            period = st.selectbox('Select the period', (None, '1y', '6mo', '3mo'))
            df = get_stock_data(selected_stock, period)

            if st.button('Show Price'):
                df = df[::-1]  # Reverse the DataFrame to display the latest data at the top
                st.write(df)
                
            st.markdown(f"Total records: {len(df)}")


        with col2:
            short_window = st.slider('Select the short moving average window', 1, 30, 5)
            long_window = st.slider('Select the long moving average window', 1, 30, 15)
            if short_window and long_window:
                signals = moving_average_crossover(df, short_window, long_window)
                fig = plot_signals(df, signals)
                st.plotly_chart(fig, use_container_width=True)

            rsi_window = st.slider('Select the RSI window', 1, 30, 14)
            oversold = st.slider('Select the oversold threshold', 0, 100, 30)
            overbought = st.slider('Select the overbought threshold', 0, 100, 70)
            if rsi_window and oversold and overbought:
                signals = rsi_bot(df, rsi_window, oversold, overbought)
                st.write(signals)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
