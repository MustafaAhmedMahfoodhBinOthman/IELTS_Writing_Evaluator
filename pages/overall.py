import streamlit as st
import pyperclip
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
# Function to calculate the overall band score


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
st.sidebar.write('This is currently in Beta version, and everyday it will be updated to reach better evalaution GOOD LUCK 😊⚡')
# st.sidebar.write('There will be many special features and big improvments coming soon😊')
type_check = 'primary'
type_take = 'secondary'


side_check_button = st.sidebar.button('Check Your Essay', type=type_take, use_container_width=True)
if side_check_button:
    st.switch_page("ielts_writing.py")
st.sidebar.write("if you want to calculate the overall band score of Task 1 and Task 2 click the button 👇")
side_check_button2 = st.sidebar.button('Caculate overall Band Score', type=type_check, use_container_width=True)
# side_take_button = st.sidebar.button("Take a Test (it's coming soon)", type=type_take, use_container_width=True, disabled=True)
message = """**Looking to evaluate your IELTS writing essays for free? Check out this website that uses AI to assess your work:** \n Website link: ielts-writing-ai.streamlit.app
"""

# Button in the sidebar to trigger the copy function
st.sidebar.write("Help others to improve their IELTS writing by sharing the website ")
# if st.sidebar.button('Share the website ', type=type_check):
#     # Use pyperclip to copy the message to the clipboard
#     pyperclip.copy(message)
#     st.sidebar.success('Copied thanks for sharing my website')
st.sidebar.write('Now you can evaluate your essay via Telegram:\n https://t.me/ielts_writing2_bot')
st.sidebar.write("if there is any issue in the performance or any suggetions please contact me")

# st.sidebar.write("Email: mustafabinothman2023@gmail.com")

st.sidebar.write("Telegram:  https://t.me/ielts_pathway")
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
        overall_score_task1 = calculate_overall_score(scores_task1)
        overall_score_task2 = calculate_overall_score(scores_task2)
        overall_score = calculate_overall_score([overall_score_task1, overall_score_task2])
        st.markdown(f'## Overall writing Band Score {(overall_score)}')
        # st.success(f"Overall Band Score for Task 1: {overall_score_task1}")
        # st.success(f"Overall Band Score for Task 2: {overall_score_task2}")
        # st.success(f"Combined IELTS Writing Overall Band Score: {overall_score}")

