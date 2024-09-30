import streamlit as st

# Title for the App
st.title('CMPDI Project Monitoring Dashboard')

# Subtitle or Header
st.header('Welcome to the Project Monitoring System')

# Basic Info Display
st.write('This platform allows you to monitor, update, and track the progress of R&D and S&T projects at CMPDI.')
import pandas as pd

# Simulated project data for CMPDI
projects_data = {
    'Project ID': ['P001', 'P002', 'P003'],
    'Title': ['Mine Safety Improvement', 'Water Resource Management', 'Clean Energy Development'],
    'Principal Investigator': ['Dr. Sharma', 'Dr. Verma', 'Dr. Gupta'],
    'Start Date': ['2023-01-10', '2023-02-20', '2023-03-15'],
    'End Date': ['2024-01-10', '2024-02-20', '2024-03-15'],
    'Status': ['Ongoing', 'Ongoing', 'Completed'],
    'Fund Utilization (%)': [50, 75, 100]
}

# Convert data to a DataFrame
df = pd.DataFrame(projects_data)

# Display the DataFrame in the app
st.write('### Project Overview')
st.dataframe(df)
# Sidebar filter for project status
st.sidebar.header('Filter Projects by Status')
status_filter = st.sidebar.selectbox('Select Project Status', ['All', 'Ongoing', 'Completed'])

# Filter the DataFrame based on the selected status
if status_filter != 'All':
    filtered_df = df[df['Status'] == status_filter]
else:
    filtered_df = df

# Display the filtered DataFrame
st.write('### Filtered Project List')
st.dataframe(filtered_df)
# Section to submit quarterly progress report
st.write('### Submit Quarterly Progress Report')

# Select project for which the report is submitted
project_id = st.selectbox('Select Project', df['Project ID'])

# Text area to enter progress details
progress_report = st.text_area('Enter Progress Details')

# Submit button
if st.button('Submit Report'):
    st.success(f'Progress report for {project_id} submitted successfully!')
# Display fund utilization as progress bars
st.write('### Fund Utilization')
for i, row in filtered_df.iterrows():
    st.write(f"Project {row['Project ID']}: {row['Title']}")
    st.progress(row['Fund Utilization (%)'] / 100)
import pytesseract
from PIL import Image

# File uploader for project-related reports (images)
uploaded_image = st.file_uploader("Upload Project Report (Image)", type=['png', 'jpg', 'jpeg'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    # Use OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(image)
    st.write("Extracted Text from the Report:")
    st.write(extracted_text)
import datetime

# Example deadlines
project_deadlines = {
    'P001': '2023-12-01',
    'P002': '2023-11-15',
    'P003': '2024-01-01'
}

current_date = datetime.date.today()

st.write("### Upcoming Submission Deadlines")
for project_id, deadline in project_deadlines.items():
    deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
    days_left = (deadline_date - current_date).days
    
    if days_left > 0:
        st.write(f"Project {project_id}: {days_left} days left until the next report is due.")
    else:
        st.warning(f"Project {project_id}: Report submission is overdue!")
# Simple authentication
def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if login(username, password):
        st.success("Logged in successfully!")
        # Continue with the app...
    else:
        st.error("Invalid username or password")
import matplotlib.pyplot as plt

# Visualize fund utilization
st.write("### Fund Utilization Chart")

fig, ax = plt.subplots()
ax.bar(df['Project ID'], df['Fund Utilization (%)'])
ax.set_xlabel('Project ID')
ax.set_ylabel('Fund Utilization (%)')
ax.set_title('Fund Utilization by Project')
st.pyplot(fig)
