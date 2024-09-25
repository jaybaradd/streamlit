# import streamlit as st
# import pandas as pd
# import os
# import json

# # CSV file to store user data

# # Check if the CSV file exists, if not, create it with the appropriate columns
# # if not os.path.exists(CSV_FILE):
# #     df = pd.DataFrame(columns=['Username', 'Phone', 'DOB', 'Email', 'Password'])
# #     df.to_csv(CSV_FILE, index=False)

# # Function to save user details to the CSV file
# # def save_user_data(username, phone, dob, email, password filename='user_data.json'):
# #     new_data = [username, phone, dob, email, password]
# #     with open(filename, mode='a',newline='') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(new_data)

# user_data_file = 'user_data.json'
# if not os.path.exists(user_data_file):
#     with open(user_data_file, "w") as f:
#         json.dump([], f) 
    
# def save_user_data(user_data):
#     try: 
#         with open('user_data.json','r') as f:
#             existing_data = json.load(f)
#     except FileNotFoundError:
#         existing_data = []
    
#     existing_data.append(user_data)

#     with open('user_data.json','w') as f:
#         json.dump(existing_data,f,indent=4)

# def load_user_data():
#     if os.path.exists('user_data.json'):
#         with open('user_data.json', "r") as f:
#             return json.load(f)
#     return {}

# def save_user_data(users):
#     with open('user_data.json', "w") as f:
#         json.dump(users, f)

# def user_exists(email):
#     users = load_user_data()
#     return email in users

# def create_user_folder(email):
#     folder_path = os.path.join(os.getcwd(), email)
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)


    

# # Sidebar for Login and Signup
# st.sidebar.title("User Authentication")
# auth_option = st.sidebar.button('Login', key='login')
# # st.session_state.login_state = True
# auth_option2 = st.sidebar.button('Signup', key='signup')
# # st.session_state = "signup"
# def signup():
#     st.title("🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻🖕🏻")

#     if 'logged_in' not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.user = None
    

#     # Signup fields
#     username = st.text_input("Username", value=st.session_state['username'])
#     phone = st.text_input("Phone number", value=st.session_state['phone'])
#     dob = st.text_input("Date of Birth",value=st.session_state['dob'])
#     email = st.text_input("Email",value=st.session_state['email'])
#     password = st.text_input("Password",value=st.session_state['password'])
    
    
    
    
#     if st.button("Submit"):
#         if username and password and phone and dob and email:
#             # Save user data to JSON   
#             user_data = {
#                 "username" : username,
#                 "phone" : phone,
#                 "dob" : dob,
#                 "email": email,
#                 "password" : password
#             }
#             save_user_data(user_data)
#             st.success(f"User {username} registered successfully!")
#             st.session_state['username'] = ""
#             st.session_state['phone'] = ""
#             st.session_state['dob'] = ""
#             st.session_state['email'] = ""
#             st.session_state['password'] = ""
#         else:
#             st.error("Please fill in all fields!")
# # st.session_state.form = 'login'
# def login():
#     st.title("Login Form")

#     # Login fields
#     login_username = st.text_input("Username", key='login_username')
#     login_password = st.text_input("Password", type='password', key='login_password')

#     if st.button("Log in"):
#         with open('user_data.json','r') as f:
#             credentials = json.load(f)
#         df = pd.DataFrame(credentials)
#         # Check if the username and password match any entry in the CSV
#         if not df[(df['Username'] == login_username) & (df['Password'] == login_password)].empty:
#             st.success(f"Welcome {login_username}!")
#         else:
#             st.error("Invalid username or password!")

# if auth_option:
#         login()
# elif auth_option2:
#         signup()



import streamlit as st
from datetime import date
import json
import os
import pandas as pd
import plotly.express as px

# Use a relative path for the JSON file
user_data_file = "Credentials.json"

# Check if the file exists, if not, create it
if not os.path.exists(user_data_file):
    with open(user_data_file, "w") as f:
        json.dump([], f)  # Initialize an empty list in the file

# Load and save user data functions
def load_user_data():
    with open(user_data_file, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []  # Return an empty list if the file is empty or corrupted

def save_user_data(data):
    with open(user_data_file, "w") as f:
        json.dump(data, f)

# Check if email exists
def check_email_exists(email):
    user_data = load_user_data()
    for user in user_data:
        if user["email"] == email:
            return True
    return False

# Streamlit sidebar for login and sign up
st.sidebar.title("User Authentication")
auth_option = st.sidebar.radio("Select an option", ['Login', 'Sign-up'])

# Handle Sign-up
if auth_option == 'Sign-up':
    st.title("Sign-up Form")
    
    # Use session_state to store input values
    if 'username' not in st.session_state:
        st.session_state['username'] = ""
    if 'phno' not in st.session_state:
        st.session_state['phno'] = ""
    if 'dob' not in st.session_state:
        st.session_state['dob'] = date.today()
    if 'email' not in st.session_state:
        st.session_state['email'] = ""
    if 'password' not in st.session_state:
        st.session_state['password'] = ""

    username = st.text_input("Username", value=st.session_state['username'])
    phno = st.text_input("Phone No", value=st.session_state['phno'])
    dob = st.date_input("DOB", value=st.session_state['dob'])
    email = st.text_input("Email", value=st.session_state['email'])
    password = st.text_input("Password", type='password', value=st.session_state['password'])

    if st.button("Submit"):
        if username and phno and dob and email and password:
            if check_email_exists(email):
                st.error("Email already exists.")
            else:
                user_data = load_user_data()
                new_user = {"username": username, "phno": phno, "dob": str(dob), "email": email, "password": password}
                user_data.append(new_user)
                save_user_data(user_data)
                st.success("Signup successful!")
                st.session_state['username'] = ""
                st.session_state['phno'] = ""
                st.session_state['dob'] = ""
                st.session_state['email'] = ""
                st.session_state['password'] = ""
        else:
            st.error("Please fill in all fields!")

# Handle Login
if auth_option == 'Login':
    st.title("Login Form")
    
    login_email = st.text_input("Email", key='login_email')
    login_password = st.text_input("Password", type='password', key='login_password')

    if st.button("Login"):
        user_data = load_user_data()
        for user in user_data:
            if user["email"] == login_email and user["password"] == login_password:
                st.session_state['username'] = user['username']  # Store username in session state
                st.success("Login successful!")
                break
        else:
            st.error("Invalid credentials.")

# Check if user is logged in
if 'username' in st.session_state and st.session_state['username']:
    # Sidebar for sign out and navigation
    st.sidebar.button("Sign Out", on_click=lambda: st.session_state.clear())

    # Display welcome message
    st.title(f"Welcome {st.session_state['username']}")

    # Sliders for marks
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'Geography', 'History', 'English']
    marks = {subject: st.slider(f"{subject} Marks", 0, 100, 0) for subject in subjects}

    # Submit button
    if st.button("Submit"):
        # Create directory for user
        user_folder = st.session_state['username']
        os.makedirs(user_folder, exist_ok=True)

        # Save marks to a CSV file
        df = pd.DataFrame([marks])
        csv_file_path = os.path.join(user_folder, "marks.csv")
        df.to_csv(csv_file_path, index=False)

        st.success("Marks submitted successfully!")

        # Generate charts
        st.title("Your reports are ready!")

        # Bar chart for average marks
        average_marks = df.mean().reset_index()
        average_marks.columns = ['Subject', 'Average Marks']
        bar_chart = px.bar(average_marks, x='Subject', y='Average Marks', title="Average Marks")
        st.plotly_chart(bar_chart)

        # Line chart for marks of each subject
        line_chart_data = pd.DataFrame({
            'Subjects': subjects,
            'Marks': df.iloc[0].values
        })
        line_chart = px.line(line_chart_data, x='Subjects', y='Marks', title="Marks in Each Subject", markers=True)
        st.plotly_chart(line_chart)
        
        # Pie chart for absolute marks per subject
        pie_chart = px.pie(values=df.iloc[0], names=df.columns, title="Marks Distribution per Subject")
        st.plotly_chart(pie_chart)






