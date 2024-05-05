import streamlit as st

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Function to calculate the overall band score
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json
from google.oauth2 import service_account
st.set_page_config(
    
    page_title= 'Overall Band score Calculator'
    # page_icon=
)
scopes = [
   'https://www.googleapis.com/auth/spreadsheets'
]

credentials_json = {
  "type": "service_account",
  "project_id": "ielts-writing-evaluator",
  "private_key_id": "a503f35fe20c737d9373cef7a6d450e26855faf0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCrdr0FxPMPxx10\nBQcmsFciybuoUKO2nUlp5iRheaDOA//LB+wZBbNP1fj3+hj+ztL1zh992e91ny35\nruxiutMTh2iL1a/YLyUh7xBcH6japLZPoAUjjQHm7qS5RQtdftgKN2jJJ3R8STDd\nk1pbRwkrIWOhYwqeWHGzn/RO9IgwoSuHLRyuTLOKAg66q0un0GIt3xzA30d9Y5Lx\nfDH4QidW/VuU+ICfM/d/Op274yjtnDRt9g3DTT+i+vIf5IJDXej/Pew8KhSEXw9e\nFZjpueoZsDcBs2sABBr7xAyQH/xkn8z7mpM+99RMTUZX4HHVQLcrH+R6hpnYA7BO\n2tA0e/1rAgMBAAECggEAG3qZCn6o0YOApeJUZg/mtw2LhIr/4blNVaprdC+w5LNh\nYCFx5gSy2v2Yu+0Z6mQtDPWuuFWf+cK79ILjIWN9hmiyCY8CcmwD0G9muMzeG8Q/\n73zetfbYMjFWttZo3uAAMYr1wR8QnQaBzVDbLzuwLXhZZjjgL8ZO2pGs7qZj2R8H\ngn1qMof5x91hqyjyk30MS35tX3lCyex0Zi0WDC7h+dcMkt5kyX3s0vbizrC3Q+2L\njZrplSAUTW+wH1TOmdM39lx47ajOx+izsDFOfNpKL2OOfttG32/A7fW91lPWUQ0f\nWQa6QkrLw4SIok56l1CbHQysBDk0j8bu0I9Oal9oYQKBgQDvSJFNfX9+45Qhsoqa\nX4vI4uGbpwxGuzpPaKPYweZvsaitIb8zCd1yNJyy2HrhmWy3H+AdHQ+vpTvuY/oi\noNb0+v2fcP6gyjzKES6gaosQcuOq4IM69nVoK5l+d1q2GWuJyaA0hftA1Z8+qSUE\niVfLU0FaA6+XX2XskE8IXJMGkQKBgQC3cUJ2QFLXNEH3c1u1V5WAWFqdviNhyWsw\nBR3CmVGAM6Zfevm+fIhCoZ1czFx1VMyqZKtGXyyWdkzVTRa2Jani5FXEMta3o9Hl\nJcg38DwoUHLBpRTYvJftZA0dwV+YUKD8MK8xlNzv7kzSpg1f8dGb+mNaZrkoISA/\noBNZb+LaOwKBgQDaaeXf0rcG7tqu65bilGY25wnCF3f4NDxkcYJlf5BE0ejCp/Qr\ntUyCS43hHgMEXBRFD351dKp1zKBo2K9g3ml30oag+/YgdJmKZKan3Li1OfmgZzDC\nKGdAv9NrAa02XPuxGO74IngWVSf3fVOB0Y/m00bq0ER+KqERjyPk4QN/UQKBgQCH\nVyiR1iNIY2XIC3Q99sB2ULmKaB3yp4hNhXjPeg6HZ5P4HeLkhzyA7HwNWzlb15So\nol07LjzXRbCqLpXzDRaqL4yXlGqWUmcpiRaPLs8zbyc7d3BJ99qfapHCwkilN9eO\nON0I16up2UcUoy56+w6K5dEngWJaGRaR2qhr9ACKwQKBgQCnaD+295ZQR3D+zS1h\nqnUVdxDvCIuAEiC6UTiZIxHMW4p6CkyW7Oxv+rZENEexh4BCClIA2wvP9OvQbxUe\nWR8iUS0lKQ8yZ3S+1dLLhzhSJn+Y6gdskfAu69y3/a98nM9GvI3J/NgG71HrbPCK\nidCVD+IWMS5EqnaYMVrJSRUgbw==\n-----END PRIVATE KEY-----\n",
  "client_email": "user-registration@ielts-writing-evaluator.iam.gserviceaccount.com",
  "client_id": "104756563010734258293",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/user-registration%40ielts-writing-evaluator.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
# json_string = json.dumps(credentials_json,ensure_ascii=False, indent=4)

# creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
# creds = Credentials.from_service_account_file(credentials_json, scopes=scopes)
creds = service_account.Credentials.from_service_account_info(credentials_json, scopes=scopes)
# creds = Credentials.from_service_account_file(st.secrets["credentials_json"], scopes=scopes)
client = gspread.authorize(creds)

# Sheet IDs
free_trial_id = '18Cc9ITOYVEvmkhjQbNXgA6NxARPtFB_bHgN4ERozfXI'
subscription_id = '12Z_BTDGHPgITYV7XOMObLv17Ckt1pzUPYt4Uu_De2us'
progression_file_id = '1yCimM9WMtDdXEjJPMm9SX9blvQx541tFDKRiL0upovA'
essay_file_id = '1TD000SU1S2RqJp99e9fMeR-M8UsyCOdTXInqFgQpnR0'
user_email = st.session_state.registered_email
# user_email = "www.binothman24@gmail.com"
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
st.sidebar.markdown("You can support my effort by buying me a coffee. ☕️ :heart: " + "[Please click here](https://ko-fi.com/mustafa_binothman)")

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

