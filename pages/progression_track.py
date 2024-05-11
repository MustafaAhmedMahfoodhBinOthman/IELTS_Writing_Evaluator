import streamlit as st
st.set_page_config(
    
    page_title= 'Overall Band score Calculator'
    # page_icon=
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
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
    unsafe_allow_html=True)
# Function to calculate the overall band score
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json
from google.oauth2 import service_account
import pandas as pd
import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt
# from plotly.subplots import make_subplots
import plotly.graph_objects as go


st.sidebar.title("""
                 
                 
                 
              
                 
                 """)

st.sidebar.title('IELTS Writing Evaluator (Free)')
# st.sidebar.write('This is currently in Beta version, and everyday it will be updated to reach better evalaution GOOD LUCK 😊⚡')
# st.sidebar.write('There will be many special features and big improvments coming soon😊')

side_check_button = st.sidebar.button('Check Your Essay', type='secondary', use_container_width=True)
if side_check_button:
    st.switch_page("ielts_writing.py")
# st.sidebar.write("If you want to calculate the overall band score of Task 1 and Task 2 press the button 👇")

side_check_button2 = st.sidebar.button('Overall Band Score Calculator', type='secondary', use_container_width=True)
if side_check_button2:
    st.switch_page("pages/overall.py")
    
side_check_button3 = st.sidebar.button('Progress Tracker', type='primary', use_container_width=True)

    # st.page_link("pages/overall.py", label="IELTS Overall Band Score Calculater", icon="🔶")
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

if 'registered_email' not in st.session_state:
    st.session_state['registered_email'] = None # or any default value you want

# Now you can safely access 'registered_email'
user_email = st.session_state['registered_email']

def get_user_scores(user_email):
    try:
        progression_file = client.open_by_key(progression_file_id)
        # Open the specific sheet for the user
        user_sheet = progression_file.worksheet(user_email)
        # Get all data from the sheet
        data = user_sheet.get_all_records()
        # Convert to DataFrame
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        st.error(f"Failed to retrieve data: {e}")
        return pd.DataFrame()

# Check if the user is registered and retrieve data
if 'registered_email' in st.session_state and st.session_state['registered_email']:
    df_scores = get_user_scores(st.session_state['registered_email'])
else:
    st.warning("Please register to view your progression.")
    st.stop()

st.markdown("## Progression Tracker")
st.write("Here you can find your IELTS band scores history")
colors = "'#FF4B4B'"
template = "ggplot2"
if df_scores.empty:
    st.warning("You haven't evaluated your essay yet. please evaluate your essay first.")
    # Task 1 has no scores, create a placeholder plot
    fig_task1_placeholder = px.line(x=[], y=[1, 2, 3, 4, 5, 6, 7, 8, 9], title='Task 1 Score',markers=True,template=template,)
    fig_task1_placeholder.update_layout(yaxis_title='Task 1 Score',xaxis_title='')
    fig_task1_placeholder.update_layout(
            yaxis=dict(
                range=[1, 9],
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                ticktext=[1, 2, 3, 4, 5, 6, 7, 8, 9]
            ),
            xaxis=dict(showticklabels=False),
            annotations=[dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=1.05,
                text='',
                font=dict(size=14),
                showarrow=False,
                xanchor='center',
                yanchor='top'
            )]
        )
    st.plotly_chart(fig_task1_placeholder)
    # fig_task1_placeholder.show()
    # Task 2 has no scores, create a placeholder plot
    fig_task2_placeholder = px.line(x=[], y=[1, 2, 3, 4, 5, 6, 7, 8, 9], title='Task 2 Score',markers=True,template=template,)
    fig_task2_placeholder.update_layout(yaxis_title='Task 2 Score',xaxis_title='')
    fig_task2_placeholder.update_layout(
            yaxis=dict(
                range=[1, 9],
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                ticktext=[1, 2, 3, 4, 5, 6, 7, 8, 9]
            ),
            xaxis=dict(showticklabels=False),
            annotations=[dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=1.05,
                text='',
                font=dict(size=14),
                showarrow=False,
                xanchor='center',
                yanchor='top'
            )]
        )
    st.plotly_chart(fig_task2_placeholder)
    # fig_task2_placeholder.show()
    # Overall scores have no data, create a placeholder plot
    overall_placeholder = go.Figure()
    overall_placeholder.add_trace(go.Scatter(x=[], y=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9], mode='lines'))
    overall_placeholder.update_layout(
            yaxis=dict(
                range=[1, 9],
                tickmode='array',
                tickvals=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9],
                ticktext=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]
            ),
            xaxis=dict(showticklabels=False),
            yaxis_title='Overall band Score',
            xaxis_title='',
            annotations=[dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=1.05,
                text='',
                font=dict(size=14),
                showarrow=False,
                xanchor='center',
                yanchor='top'
            )]
        )
    st.plotly_chart(overall_placeholder)
    # overall_placeholder.show()
    # Plot Task 1 Scores
else:
    if df_scores['task_1_score'].empty and df_scores['task_1_date'].empty:
            # Task 1 has no scores, create a placeholder plot
            fig_task1_placeholder = px.line(x=[], y=[1, 2, 3, 4, 5, 6, 7, 8, 9], title='Task 1 Score ',markers=True,template=template,)
            fig_task1_placeholder.update_layout(yaxis_title='Task 1 Score',xaxis_title='')
            fig_task1_placeholder.update_layout(
                yaxis=dict(range=[1, 9], tickmode='linear', tick0=1, dtick=1),
                xaxis=dict(showticklabels=False),
                annotations=[dict(
                    xref='paper',
                    yref='paper',
                    x=0.5,
                    y=1.05,
                    text='',
                    font=dict(size=14),
                    showarrow=False,
                    xanchor='center',
                    yanchor='top'
                )]
            )
            st.plotly_chart(fig_task1_placeholder)
            # fig_task1_placeholder.show()
    else:
            # Task 1 has scores, plot them
            fig_task1 = px.line(df_scores, x='task_1_date', y='task_1_score', title='Task 1 Score',markers=True,template=template, )
            fig_task1.update_layout(yaxis_title='Task 1 Score',xaxis_title='Date')
            fig_task1.update_layout(
                yaxis=dict(
                    range=[1, 9],
                    tickmode='array',
                    tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    ticktext=[1, 2, 3, 4, 5, 6, 7, 8, 9]
                ),
                # xaxis=dict(showticklabels=True),
                annotations=[dict(
                    xref='paper',
                    yref='paper',
                    x=0.5,
                    y=1.05,
                    text='',
                    font=dict(size=14),
                    showarrow=False,
                    xanchor='center',
                    yanchor='top'
                )]
            )
            st.plotly_chart(fig_task1)
            # fig_task1.show()
    if df_scores['task_2_score'].empty and df_scores['task_2_date'].empty:
            # Task 2 has no scores, create a placeholder plot
            fig_task1_placeholder = px.line(x=[], y=[1, 2, 3, 4, 5, 6, 7, 8, 9], title='Task 2 Score',markers=True,template=template,)
            fig_task1_placeholder.update_layout(yaxis_title='Task 2 Score',xaxis_title='')
            fig_task1_placeholder.update_layout(
                yaxis=dict(range=[1, 9], tickmode='linear', tick0=1, dtick=1),
                xaxis=dict(showticklabels=False),
                annotations=[dict(
                    xref='paper',
                    yref='paper',
                    x=0.5,
                    y=1.05,
                    text='',
                    font=dict(size=14),
                    showarrow=False,
                    xanchor='center',
                    yanchor='top'
                )]
            )
            st.plotly_chart(fig_task1_placeholder)
            # fig_task1_placeholder.show()
    else:
            # Task 2 has scores, plot them
            fig_task2 = px.line(df_scores, x='task_2_date', y='task_2_score', title='Task 2 Score',markers=True,template=template,)
            fig_task2.update_layout(yaxis_title='Task 2 Score',xaxis_title='Date')
            fig_task2.update_layout(
                yaxis=dict(
                    range=[1, 9],
                    tickmode='array',
                    tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    ticktext=[1, 2, 3, 4, 5, 6, 7, 8, 9]
                ),
                # xaxis=dict(showticklabels=True),
                annotations=[dict(
                    xref='paper',
                    yref='paper',
                    x=0.5,
                    y=1.05,
                    text='',
                    font=dict(size=14),
                    showarrow=False,
                    xanchor='center',
                    yanchor='top'
                )]
            )
            st.plotly_chart(fig_task2)
            # fig_task2.show()
    # Check if overall scores are empty and apply placeholder plot
    if df_scores['overall_score'].empty and df_scores['overall_date'].empty:
            # Overall scores have no data, create a placeholder plot
            fig_task1_placeholder = px.line(x=[], y=[1, 2, 3, 4, 5, 6, 7, 8, 9], title='Overall band Score',markers=True,template=template,)
            fig_task1_placeholder.update_layout(yaxis_title='Overall Score',xaxis_title='')
            fig_task1_placeholder.update_layout(
                yaxis=dict(range=[1, 9], tickmode='linear', tick0=1, dtick=1),
                xaxis=dict(showticklabels=False),
                annotations=[dict(
                    xref='paper',
                    yref='paper',
                    x=0.5,
                    y=1.05,
                    text='',
                    font=dict(size=14),
                    showarrow=False,
                    xanchor='center',
                    yanchor='top'
                )]
            )
            st.plotly_chart(fig_task1_placeholder)
            # fig_task1_placeholder.show()
    else:
            # Overall scores have data, plot them
            fig_overall = px.line(df_scores, x='overall_date', y='overall_score', title='Overall band Score',markers=True,template=template, )
            fig_overall.update_layout(yaxis_title='Overall score',xaxis_title='Date')
            fig_overall.update_layout(
            yaxis=dict(
                range=[1, 9],
                tickmode='array',
                tickvals=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9],
                ticktext=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]
            ),
            xaxis=dict(showticklabels=True),
            yaxis_title='Overall Score',
            xaxis_title='',
            annotations=[dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=1.05,
                text='',
                font=dict(size=14),
                showarrow=False,
                xanchor='center',
                yanchor='top'
            )]
        )

            st.plotly_chart(fig_overall)
            # fig_overall.show()

