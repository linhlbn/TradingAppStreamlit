import streamlit as st
import mysql.connector

# Establish MySQL connection
db = mysql.connector.connect(
    host="localhost", # hostname 
    user="root", # user
    password="qwer1234", # password
    database="cryptoapp" # database
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create the users table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)
db.commit()

# Sign-up form
st.title("Sign Up")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):
    if password == confirm_password:
        # Check if the username already exists
        check_username_query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(check_username_query, (username,))
        result = cursor.fetchone()
        if result:
            st.error("Username already exists. Please choose a different username.")
        else:
            # Insert the new user into the users table
            insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(insert_user_query, (username, password))
            db.commit()
            st.success("User created successfully. You can now sign in.")
    else:
        st.error("Passwords do not match.")

# Close the database connection
cursor.close()
db.close()
