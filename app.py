import streamlit as st
import pandas as pd
from datetime import datetime

# Path to the Excel file
excel_file = 'attendance_records.xlsx'

# Function to load data from the Excel file
def load_data():
    try:
        return pd.read_excel(excel_file)
    except FileNotFoundError:
        return pd.DataFrame(columns=['Name', 'Shift Time', 'Station', 'Issue', 'Comments', 'Tardy Minutes', 'Uniform Action', 'No ID Sent Home', 'No ID Minutes Late', 'Safety Issue Reason', 'Timestamp'])

# Function to save data to the Excel file
def save_data(df):
    df.to_excel(excel_file, index=False)

# Load existing data
data = load_data()

# Fetch distinct names from the data for search functionality
names = data['Name'].unique()

# Streamlit app layout
st.title("Attendance for Managers & CL 2024")

# Name field with search functionality
name = st.selectbox("What is the student's name?", options=names, help="Search and select a name from the list or add a new name.")
shift_time = st.text_input("What is the shift time?")
station = st.text_input("What station?")

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
        "Timestamp": [timestamp]
    })
    data = pd.concat([data, new_record], ignore_index=True)
    save_data(data)
    st.success("Attendance record submitted successfully!")

# Display the attendance records
if st.checkbox("Show attendance records"):
    st.dataframe(data)
