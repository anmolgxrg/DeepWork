import streamlit as st
import pandas as pd
from datetime import datetime

# Path to the Excel file
excel_file = 'attendance_records.xlsx'

# Function to load data from the Excel file
def load_data():
    with pd.ExcelFile(excel_file) as xls:
        summary = pd.read_excel(xls, sheet_name='Summary')
        transactions = pd.read_excel(xls, sheet_name='Transactions')
        managers = pd.read_excel(xls, sheet_name='Managers')
        stations = pd.read_excel(xls, sheet_name='Stations')['Station Name'].tolist()
    return summary, transactions, managers, stations

# Function to save data to the Excel file
def save_data(summary_df, transactions_df):
    with pd.ExcelWriter(excel_file) as writer:
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        transactions_df.to_excel(writer, sheet_name='Transactions', index=False)
        managers_data.to_excel(writer, sheet_name='Managers', index=False)
        stations_data.to_excel(writer, sheet_name='Stations', index=False)

# Load existing data
summary_data, transactional_data, managers_data, stations_data = load_data()

# Fetch distinct names from the summary data for search functionality
names = summary_data['Name'].unique()
managers = managers_data['Name'].unique()

# Streamlit app layout
st.title("Attendance for Managers & CL 2024")

# Manager selection
manager = st.selectbox("Select the manager filling this form", options=managers, help="Select the manager from the list.")

# Name field with search functionality
name = st.selectbox("What is the student's name?", options=names, help="Search and select a name from the list.")
shift_time = st.text_input("What is the shift time?")
station = st.selectbox("Station", options=stations_data + ["Other"], help="Select the station from the list or choose 'Other'.")

issue = st.selectbox("Issue", ["Tardy", "Uniform & Grooming Standards", "NCNS", "Unexcused Absence", "Excused Absence", "No ID", "Safety Issue", "Other"])
comments = st.text_area("Comments")

tardy_minutes = None
uniform_action = None
no_id_sent_home = None
no_id_minutes_late = None
safety_issue_reason = None

if issue == "Tardy":
    tardy_minutes = st.number_input("How many minutes was the student late to his shift?", min_value=0, max_value=1440, step=1)

if issue == "Uniform & Grooming Standards":
    uniform_action = st.text_input("What action was taken for not following Uniform & Grooming?")

if issue == "No ID":
    no_id_sent_home = st.selectbox("Was the student sent home?", ["Yes", "No"])
    no_id_minutes_late = st.number_input("How many minutes was the student late?", min_value=0, max_value=1440, step=1)

if issue == "Safety Issue":
    safety_issue_reason = st.text_input("Reason for Safety Issue")

if st.button("Submit"):
    timestamp = datetime.now().isoformat()
    new_record = pd.DataFrame({
        "Name": [name],
        "Shift Time": [shift_time],
        "Station": [station],
        "Issue": [issue],
        "Comments": [comments],
        "Tardy Minutes": [tardy_minutes],
        "Uniform Action": [uniform_action],
        "No ID Sent Home": [no_id_sent_home],
        "No ID Minutes Late": [no_id_minutes_late],
        "Safety Issue Reason": [safety_issue_reason],
        "Timestamp": [timestamp],
        "Manager": [manager]
    })

    # Update the transactional data
    transactional_data = pd.concat([transactional_data, new_record], ignore_index=True)
    
    # Update points in the summary data
    summary_data.loc[summary_data['Name'] == name, 'Points'] += 1

    # Save the updated data
    save_data(summary_data, transactional_data)
    
    st.success("Attendance record submitted successfully!")

# Display the attendance records
if st.checkbox("Show attendance records"):
    st.dataframe(transactional_data)
    
# Display the summary data
if st.checkbox("Show summary data"):
    st.dataframe(summary_data)
