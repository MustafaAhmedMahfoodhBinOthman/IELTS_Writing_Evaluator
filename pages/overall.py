import streamlit as st
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
# Function to calculate the overall band score
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

st.set_page_config(
    
    page_title= 'Overall Band score Calculator'
    # page_icon=
)
scopes = [
   'https://www.googleapis.com/auth/spreadsheets'
]
# creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
credn_secret = st.secrets['credentials_json']
creds = Credentials.from_service_account_file(credn_secret, scopes=scopes)
client = gspread.authorize(creds)

# Sheet IDs
free_trial_id = '18Cc9ITOYVEvmkhjQbNXgA6NxARPtFB_bHgN4ERozfXI'
subscription_id = '12Z_BTDGHPgITYV7XOMObLv17Ckt1pzUPYt4Uu_De2us'
progression_file_id = '1yCimM9WMtDdXEjJPMm9SX9blvQx541tFDKRiL0upovA'
essay_file_id = '1TD000SU1S2RqJp99e9fMeR-M8UsyCOdTXInqFgQpnR0'
# user_email = st.session_state.registered_email
user_email = "www.binothman24@gmail.com"
def find_user_sheet(progression_file, email):
    # Get a list of all sheets in the progression file
    sheets = progression_file.worksheets()
    
    # Iterate through the sheets to find the one with the matching title
    for sheet in sheets:
        if sheet.title == email:
            return sheet
    
    # If no matching sheet is found, return None
    return None
def append_overall_score_and_date(progression_file, email, overall_score, date):
    # Find the user's sheet
    user_sheet = find_user_sheet(progression_file, email)
    if user_sheet is None:
        return False # Failed to find the sheet

    # The overall score and date will be appended to the 5th and 6th columns
    score_col_index = 5
    date_col_index = 6

    # Get all values from the sheet
    all_values = user_sheet.get_all_values()
    last_row_with_data = len(all_values) - 1 # Subtract 1 to exclude the header row

    # Check if the columns for the overall score and date are already filled
    if all_values[last_row_with_data][score_col_index - 1] and all_values[last_row_with_data][date_col_index - 1]:
        # If both columns are filled, append to the next row
        row_to_append = last_row_with_data + 2
    else:
        # If either column is empty, append to the current row
        row_to_append = last_row_with_data + 1

    # Append the overall score and date to the appropriate columns
    user_sheet.update_cell(row_to_append, score_col_index, overall_score)
    user_sheet.update_cell(row_to_append, date_col_index, date)

    return True
def calculate_overall_score(scores):
    average_score = sum(scores) / len(scores)
    # Rounding to the nearest half-band score
    rounded_score = round(average_score * 2) / 2
    return rounded_score

st.markdown(
    """
    <style>
        .st-emotion-cache-j7qwjs {
            display: none;
        }
        .st-emotion-cache-sntl9t {
            display: none;
        }
        .st-emotion-cache-1oe5cao {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("""
                 
                 
                 
              
                 
                 """)
st.title('IELTS Writing Evaluator (Free)')
st.markdown('### IELTS Writing Overall Band Score Calculator')
st.info(
    """
    **How to Use the IELTS Writing Overall Score Calculator:**
    
    1. **Evaluate Both Tasks:** Begin by evaluating both Task 1 and Task 2 using the evaluation page.
    2. **Record Scores:** Take note of the scores for each criterion (Task Achievement, Coherence and Cohesion, Lexical Resource, Grammatical Range and Accuracy) for both tasks.
    3. **Enter Scores:** Fill in the scores in the respective fields below for each task manually.
    4. **Calculate Overall Score:** Press the 'Calculate Overall Band Score' button to see your combined IELTS Writing score.
    
    Soon, these fields will be filled automatically based on your previous evaluations.
    """
)


st.sidebar.title('IELTS Writing Evaluator (Free)')
# st.sidebar.write('This is currently in Beta version, and everyday it will be updated to reach better evalaution GOOD LUCK 😊⚡')
# st.sidebar.write('There will be many special features and big improvments coming soon😊')
type_check = 'primary'
type_take = 'secondary'


side_check_button = st.sidebar.button('Check Your Essay', type=type_take, use_container_width=True)
if side_check_button:
    st.switch_page("ielts_writing.py")
# st.sidebar.write("if you want to calculate the overall band score of Task 1 and Task 2 click the button 👇")
side_check_button2 = st.sidebar.button('Overall Band Score Calculator', type=type_check, use_container_width=True)
# side_take_button = st.sidebar.button("Take a Test (it's coming soon)", type=type_take, use_container_width=True, disabled=True)
import pyperclip

# Define the message you want to copy to the clipboard
message = """**Looking to evaluate your IELTS writing essays for free? Check out this website that uses AI to assess your work:** \n Website link: ielts-writing-ai.streamlit.app
"""

# Button in the sidebar to trigger the copy function
st.sidebar.write("Help others to improve their IELTS writing by sharing the website ")
# if st.sidebar.button('Share the website '):
#     # Use pyperclip to copy the message to the clipboard
#     pyperclip.copy(message)
#     st.sidebar.success('Copied thanks for sharing my website')
st.sidebar.write('Now you can evaluate your essay via Telegram: https://t.me/ielts_writing2_bot')
st.sidebar.write("if there is any issue in the performance or any suggetions please contact me")

# st.sidebar.write("Email: mustafabinothman2023@gmail.com")
st.sidebar.write("Telegram:  https://t.me/mustafa_binothman")
st.sidebar.markdown("Developed by **Mustafa Bin Othman**")


with st.form("score_form"):
    st.write("Please enter the scores for each criterion for both tasks:")
    
    # Creating input fields for each criterion for both tasks
    criteria = ["Task Achievement", "Coherence and Cohesion", "Lexical Resource", "Grammatical Range and Accuracy"]
    scores_task1 = []
    scores_task2 = []
    
    for criterion in criteria:
        col1, col2 = st.columns(2)
        with col1:
            score = st.number_input(f"Task 1 - {criterion}", min_value=0.0, max_value=9.0, step=0.5, key=criterion+"1")
            scores_task1.append(score)
        with col2:
            score = st.number_input(f"Task 2 - {criterion}", min_value=0.0, max_value=9.0, step=0.5, key=criterion+"2")
            scores_task2.append(score)
    
    # Button to calculate the overall band score
    submitted = st.form_submit_button("Calculate Overall Band Score")
    if submitted:
        print(user_email)
        overall_score_task1 = calculate_overall_score(scores_task1)
        overall_score_task2 = calculate_overall_score(scores_task2)
        overall_score = calculate_overall_score([overall_score_task1, overall_score_task2])
        print("calculated overall score", overall_score)
        st.markdown(f'## Overall writing Band Score {(overall_score)}')
        current_date = datetime.now().strftime('%d/%m/%Y %H:%M')
        
        if user_email is None:
            pass
        else:
            try:
                progression_file = client.open_by_key(progression_file_id)
                # Append the overall score and date to the user's sheet
                print("Append the overall score and date to the user's sheet")
                append_overall_score_and_date(progression_file, user_email, float(overall_score), current_date)
            except Exception as e:
                print(f"erorr adding the overall score to the sheet, user's email: {user_email}:\n\n {e}")
            # st.success(f"Overall Band Score for Task 1: {overall_score_task1}")
            # st.success(f"Overall Band Score for Task 2: {overall_score_task2}")
            # st.success(f"Combined IELTS Writing Overall Band Score: {overall_score}")

