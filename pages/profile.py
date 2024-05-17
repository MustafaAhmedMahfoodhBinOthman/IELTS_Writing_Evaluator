import streamlit as st
# from streamlit_gsheets import GSheetsConnection
from google.oauth2 import service_account
from datetime import datetime
import gspread
st.set_page_config(
    page_title='Evaluation History',
    # page_icon=...
)
# Google Spreadsheet setup 

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
# gsheets = GSheetsConnection(credentials_json)

free_trial_id = '18Cc9ITOYVEvmkhjQbNXgA6NxARPtFB_bHgN4ERozfXI'
subscription_id = '12Z_BTDGHPgITYV7XOMObLv17Ckt1pzUPYt4Uu_De2us'
progression_file_id = '1yCimM9WMtDdXEjJPMm9SX9blvQx541tFDKRiL0upovA'
essay_file_id = '1TD000SU1S2RqJp99e9fMeR-M8UsyCOdTXInqFgQpnR0'
all_essays_file_id = "1-_fGuj3WVyR2rhDsRaKOzKVAJW7Vxuy5D6Oacm1pHjA"


    
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
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        transition: margin-left .3s;
    }
    .reportview-container .main .block-container {
        max-width: 100%;
        padding-left: 20rem;
        transition: padding-left .3s;
    }
    .sidebar-expanded .sidebar .sidebar-content {
        margin-left: 0;
    }
    .sidebar-expanded .reportview-container .main .block-container {
        padding-left: 7rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title('IELTS Writing Evaluator (Free)')
side_check_button3 = st.sidebar.button('Profile', type="primary", use_container_width=True)

side_check_button = st.sidebar.button('Check Your Essay', type="secondary", use_container_width=True)
if side_check_button:
    st.switch_page("ielts_writing.py")
# st.sidebar.write("If you want to calculate the overall band score of Task 1 and Task 2 press the button 👇")


side_check_button2 = st.sidebar.button('Overall Band Score Calculator', type="secondary", use_container_width=True)
if side_check_button2:
    st.switch_page("pages/overall.py")
    # st.page_link("pages/overall.py", label="IELTS Overall Band Score Calculater", icon="🔶")
side_check_button3 = st.sidebar.button('Progress Tracker', type="secondary", use_container_width=True)
if side_check_button3:
    st.switch_page("pages/progression_track.py")
# side_take_button = st.sidebar.button("Take a Test (it's coming soon)", type=type_take, use_container_width=True, disabled=True)

message = """**Looking to evaluate your IELTS writing essays for free? Check out this website that uses AI to assess your work:** \n Website link: ielts-writing-ai.streamlit.app
"""

# Button in the sidebar to trigger the copy function
st.sidebar.write("Help others to improve their IELTS writing by sharing the website ")
# if st.sidebar.button('Share the website ', type=type_check):
#     # Use pyperclip to copy the message to the clipboard
#     pyperclip.copy(message)
#     st.sidebar.success('Copied thanks for sharing my website')
st.sidebar.write('Now you can evaluate your essay via Telegram: https://t.me/ielts_writing2_bot')
st.sidebar.write("If there is any issue in the performance or any suggetions please contact me")

# st.sidebar.write("Email: mustafabinothman2023@gmail.com")
st.sidebar.write("Telegram:  https://t.me/ielts_pathway")
st.sidebar.markdown("Developed by **Mustafa Bin Othman**")
st.sidebar.markdown("You can support my effort by buying me a coffee. ☕️ :heart: " + "[Please click here](https://ko-fi.com/mustafa_binothman)")

# Function to get user's evaluation history
def get_evaluation_history(email):
    essay_file = client.open_by_key(essay_file_id)
    try:
        essay_sheet = essay_file.worksheet(email)
        data = essay_sheet.get_all_values()[1:]  # Skip the header row
        return data
    except:
        return [] 

# Streamlit app for the history page


# ... (Add your code to hide Streamlit elements if needed, like in your main app) ... 
email = st.session_state.registered_email if 'registered_email' in st.session_state else None
st.title('Your Evaluation History')
# st.markdown(f"#### {email}")

with st.spinner('wait few seconds...'):
    try:
        # Get the registered email from session state (assuming it's stored in your main app)
        

        if email:
            evaluation_history = get_evaluation_history(email)

            if evaluation_history:
                for i, evaluation in enumerate(evaluation_history):
                    # Create an expander that initially only shows task type and question
                    with st.expander((f"**Evaluation {i+1} - {evaluation[1]}**  -  {evaluation[2]}  -  {evaluation[0]} - {evaluation[11]}")):  
                        # st.markdown(f"**Date:** \n{evaluation[0]}")
                        st.markdown(f"##### Essay:")
                        st.markdown(f"\n{evaluation[3]}")

                        # Display other evaluation details
                        st.markdown(f"##### Task Response:")
                        st.markdown(f"{evaluation[4]}")
                        st.markdown(f"##### Coherence and Cohesion:")
                        st.markdown(f"{evaluation[5]}")
                        st.markdown(f"##### Lexical Resources:")
                        st.markdown(f"{evaluation[6]}")
                        st.markdown(f"##### Grammar Accuracy:")
                        st.markdown(f"{evaluation[7]}")
                        st.markdown(f"##### Grammar and Spelling Mistakes:")
                        st.markdown(f"{evaluation[8]}")
                        st.markdown(f"##### Synonyms of most repeated words:")
                        st.markdown(f"{evaluation[9]}")
                        st.markdown(f"##### Rewritten Essay:")
                        st.markdown(f"{evaluation[10]}")
                        st.markdown(f"##### {evaluation[1]} **{evaluation[11]}**") 

            else:
                st.write("No evaluation history found. PLease evaluate your essay.")
                try:
                    if st.button("Start evaluating"):
                        st.switch_page("ielts_writing.py")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    # st.error("I am sorry there is an issuue happend please try again")
        else:
            st.warning("Please register on the main page to view your evaluation history.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        st.error("I am sorry there is an issuue happend please try again")
