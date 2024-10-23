import streamlit as st
pip install jdatetime streamlit
import numpy as np
import pandas as pd
import jdatetime
from datetime import datetime

# Function to convert Gregorian date to Jalali
def gregorian_to_jalali(date):
    jalali_date = jdatetime.date.fromgregorian(date=date)
    return jalali_date

# Function to convert Jalali date to Gregorian
def jalali_to_gregorian(year, month, day):
    return jdatetime.date(year, month, day).togregorian()

# Title for the app
st.title("Jalali Date Picker")

# Streamlit date picker (Gregorian)
selected_gregorian_date = st.date_input("Select a date (Gregorian)", datetime.now())

# Convert the selected Gregorian date to Jalali
selected_jalali_date = gregorian_to_jalali(selected_gregorian_date)

# Display the selected Jalali date
st.write(f"Selected Jalali date: {selected_jalali_date}")

# Custom Jalali date input
st.subheader("Jalali Date Input")
col1, col2, col3 = st.columns(3)
year = col1.number_input("Year", value=selected_jalali_date.year, step=1)
month = col2.number_input("Month", value=selected_jalali_date.month, step=1, min_value=1, max_value=12)
day = col3.number_input("Day", value=selected_jalali_date.day, step=1, min_value=1, max_value=31)

# Convert custom Jalali date input to Gregorian and display
if st.button("Submit Jalali Date"):
    try:
        gregorian_date = jalali_to_gregorian(int(year), int(month), int(day))
        st.write(f"Converted to Gregorian: {gregorian_date}")
    except ValueError as e:
        st.error(f"Invalid date: {e}")

st.write("Hi dude")
