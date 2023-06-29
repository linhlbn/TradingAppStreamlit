import streamlit as st

# Import the respective page modules
import homepage
import analyticalpage

# Set page configuration
st.set_page_config(layout="wide")

# Navigation or selection logic
selected_page = st.sidebar.selectbox("Select Page", ["Home", "Analytical"])

# Run the selected page
if selected_page == "Home":
    homepage.run()
elif selected_page == "Analytical":
    analyticalpage.run()
