import streamlit as st

def run():
    st.title("Home Page")

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

    st.title('Stock Trading App & Bot')
    st.subheader('Welcome to our Stock Trading App!')

    st.markdown("""
        This is a powerful and user-friendly platform for analyzing stocks, generating trading signals, and managing your investment portfolio. 
        Sign up or sign in to access the full range of features and take your trading to the next level.
        """)

    # Sign Up Button
    signup_button = st.button('Sign Up')
    if signup_button:
        # TODO: Implement Sign Up functionality
        st.write('Sign Up button clicked!')

    # Sign In Button
    signin_button = st.button('Sign In')
    if signin_button:
        # TODO: Implement Sign In functionality
        st.write('Sign In button clicked!')
