import streamlit as st
# import pytesseract
import google.generativeai as genai
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import random
import re
from PIL import Image

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



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
Claude_API_KEY = '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'

Gemini_API_Key = 'AIzaSyAtnlV6rfm_OsSt9M_w9ZaiFn3NjdjSVuw' #mustafabinothman22
Gemini_API_Key2 = 'AIzaSyDbU_8cAQCAhr59bqtGf40FV-92KCKkLWs' #mustafanotion
Gemini_API_Key3 = 'AIzaSyBOb6xrGvLxRBvgMEUyWvTSGKZVDGT4j3w' #mustafabinothman2003
Gemini_API_Key4 = 'AIzaSyB5Cy4KIg4xKwz2poq3sywJEvqI0BL10iQ' #mustafabinothman2023
Gemini_API_Key5 = 'AIzaSyBUpws7IJIKo9rZI1YKSBPQj_RpPWwTqFo' #www.binothman24

keys = ['AIzaSyAtnlV6rfm_OsSt9M_w9ZaiFn3NjdjSVuw','AIzaSyDbU_8cAQCAhr59bqtGf40FV-92KCKkLWs','AIzaSyBOb6xrGvLxRBvgMEUyWvTSGKZVDGT4j3w','AIzaSyB5Cy4KIg4xKwz2poq3sywJEvqI0BL10iQ','AIzaSyBUpws7IJIKo9rZI1YKSBPQj_RpPWwTqFo']
used_key = random.choice(keys)


model = genai.GenerativeModel('gemini-1.0-pro-latest')
model_vision = genai.GenerativeModel('gemini-pro-vision')

type_check = 'primary'
type_take = 'secondary'


st.sidebar.title('IELTS Writing Evaluator (Free)')
st.sidebar.write('This is currently in Beta version launched on 11/3/2024')
st.sidebar.write('There will be many special features and big improvments coming soon😊')
side_check_button = st.sidebar.button('Check Your Essay', type=type_check, use_container_width=True)
side_take_button = st.sidebar.button("Take a Test (it's coming soon)", type=type_take, use_container_width=True, disabled=True)

st.sidebar.write("if there is any issue in the performance kindly contact me to solve that problem")
st.sidebar.write("Email: mustafabinothman2023@gmail.com")
st.sidebar.write("Telegram:  https://t.me/ielts_pathway")
st.sidebar.markdown("Developed by **Mustafa Bin Othman**")


st.title('IELTS Writing Evaluator (Free)')
st.write('This is a high-quality AI that is competent in evaluating IELTS writing. It uses advanced LLMs to make an accurate analysis of IELTS essays.')

#make the user take a test
# the problem is that the timer and the text input does not work in the same time
# def take_test():
#     import time
#     import asyncio
#     def input_area():
#         question = st.text_area(label='**Enter the question**')
#         essay = st.text_area(label='**Write your essay**', height=700)
#         num_words = len(essay.split())
#         q_words = len(question.split())
#         st.write('Number of Words:', num_words)
#         button = st.button('Evaluate')

#     async def countdown_timer(duration, task):
#         st.header(f"Task {task} Timer")
#         seconds = duration * 60  # Convert minutes to seconds
#         placeholder = st.empty()  # Create a placeholder

#         while seconds > 0:
#             mins, secs = divmod(seconds, 60)  # Get minutes and seconds
#             timeformat = '{:02d}:{:02d}'.format(mins, secs)  # Format time as mm:ss
#             placeholder.subheader(timeformat)  # Update the placeholder
#             await asyncio.sleep(1)  # Asynchronous sleep for 1 second
#             seconds -= 1

#         placeholder.write("Time's up!")  # Update the placeholder after countdown
#     async def main():
#         select_task = st.selectbox("Select Task", ["Task 1", "Task 2"])
#         if select_task == "Task 1":
#             await asyncio.gather(input_area(),await countdown_timer(20, 1))  # 20 minutes for Task 1
#         elif select_task == "Task 2":
#             await asyncio.gather(input_area(),await countdown_timer(40, 2))  # 40 minutes for Task 2

#     st.write("Running input area and countdown timer concurrently...")
#     asyncio.run(main())


task = ''
gen_acad = ''
# st.markdown('**Please Select which task you want to evlauate**')
select_task = st.selectbox('**Please Select which task you want to evlauate**', ['Task 1', 'Task 2'])

if select_task == 'Task 1':
    task = 'Task 1'
    gen_aca = st.selectbox('**Academic or General essay**', ['Academic', 'General'])
    gen_acad = gen_aca
    if gen_acad == 'Academic':
        chart_image = st.file_uploader('Please upload Task 1 chart/map', type=['png', 'jpg'] )
    else:
        pass
    
    
    # essay_image= st.file_uploader('if you have a written essay upload it (currently is unsupported it is coming soon)', type=['png', 'jpg'], accept_multiple_files=False,)
else:
    task = 'Task 2'
    # essay_image= st.file_uploader('if you have a written essay upload it (currently is unsupported it is coming soon)', type=['png', 'jpg'], accept_multiple_files=False)

# if task == 'Task 1':
#     if chart_image is not None:
#             st.image(chart_image, width=400)

described_image = ''  
        
def decripe_image(api):
    image_prompt = 'only describe the image and do not add any additional information that the image do not present'
    genai.configure(api_key=api)
    model_vision = genai.GenerativeModel('gemini-pro-vision')

    try:
        response2 = model_vision.generate_content([image_prompt, image_pil])
        response2.resolve()
        describe = response2.text
        described_image = describe
        # print('---------------')
        print(len(described_image))
    except Exception as e:
        print("An error has occurred:", e)
        print("Retrying...")

if task == 'Task 1' and gen_acad == 'Academic' :
    if chart_image is not None:
        image_pil = Image.open(chart_image)
        st.image(image_pil, width=500)
        # decripe_image(used_key, image_pil)
        



question = st.text_area(label='**Enter the question of the essay**')
# st.markdown('### Write the essay')
essay = st.text_area(label='**Write or Paste the essay**', height= 600)
num_words = len(essay.split())
q_words = len(question.split())
st.write('Number of Words:    ',num_words)
button = st.button('Evaluate')

list_of_repeated_words = []

def words_charts():
    from collections import Counter

    # Remove punctuation and convert to lowercase
    essay_cleaned = re.sub(r'[^\w\s]', '', essay).lower()

    excluded_words = ['were','was','my','these', 'your', 'you', 'this', 'because', 'other', 'before', 'after', 'should', 'would', 'can', 'be', 'why', 'where', 'when', 'what', "don't", 'does', 'do', 'how', 'which', 'that', 'me', 'am', 'i', "hasn't", "havn't", 'we', 'they', 'she', 'he', 'us', 'our', 'its', 'their', 'them', 'her', 'him', 'his', 'while', 'it', 'while', 'about', 'are', 'is', 'has', 'have', 'at', 'in', 'on', 'of', 'to', 'from', 'for', 'with', 'by', 'as', 'and', 'or', 'but', 'nor', 'so', 'yet', 'the', 'a', 'an', 'not']

    # Split the essay into words and exclude words in the excluded_words list
    words = [word for word in essay_cleaned.split() if word not in excluded_words]

    # Filter out numbers from the words list
    words = [word for word in words if not word.isdigit()]

    word_counts = Counter(words)
    most_repeated_words = word_counts.most_common(5)

    for word, count in most_repeated_words:
        list_of_repeated_words.append(word)

    st.markdown('**Top 5 Most Repeated Words**')

    words = [word for word, _ in most_repeated_words]
    counts = [count for _, count in most_repeated_words]

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.title('Top 5 Most Repeated Words')
    st.pyplot(plt)

def synonym(api):
    sy_prompt = f"""Please provide three synonyms for each of the five words I will give you,
    closely related to the meaning of the word in the context of this essay {essay}. Your response should include words suitable for IELTS writing 
    to enhance the score and should avoid repeating the same word. The words should be 100% related to the intended meaning 
    in the context of the word from the provided IELTS writing essay. Please list the words followed by their synonyms in order,
    without any additional information unrelated to the task. please if the synonym is not suitable for the context of the word do not write it 
The words are {list_of_repeated_words} from the IELTS writing essay {essay}.
and you should organize them 
    """
    genai.configure(api_key = api)
    # model = genai.GenerativeModel('gemini-1.0-pro-latest')
    while True:
        try:
            response2 = model.generate_content(sy_prompt, stream=True)
            response2.resolve()
            synonyms = response2.text
            st.write(synonyms)
            break  # Break out of the while loop if the generation is successful
        except Exception as e:
            print("An error has occurred:", e)
            print("Retrying...")
            continue 

def rewrite_essay(api):
    re_prompt = f"""
    pretend you are English teacher and you have experience in IELTS writing essays 
    your task is to rewrite this IELTS writing essay {essay} based on this question {question}to a better version and match 
    IELTS requirements in IELTS academic writing {task}, please do not write the headline of the paragraph
    and it must be more than 250 words and less than 330 words if task 2 and more than 150 and less than 200 if task 1
    
    In your revised essay, focus on refining the structure, coherence, and language to meet the IELTS academic writing standards. Ensure that the essay effectively addresses the question, 
    demonstrates a clear understanding of the topic, and presents well-developed ideas with supporting examples and evidence. Additionally, pay attention to grammar, vocabulary, 
    and sentence structure to create a more polished and coherent essay that meets the requirements for IELTS academic writing.
    """
    genai.configure(api_key = api)
    # model = genai.GenerativeModel('gemini-1.0-pro-latest')
    
    num_word = 0
    if task == 'Task 1':
        num_word = 150
    else:
        num_word = 250
    
    while True:
        try:
            while True:
                response = model.generate_content(re_prompt, stream=True)
                response.resolve()
                rewrtie = response.text
                word_count = len(rewrtie.split())
                
                if word_count >= num_word and word_count < (num_word + 40):
                    st.write(rewrtie)
                    st.write('Number of Words:', word_count)
                    # print("Essay generated successfully.")
                    print(num_word)
                    break  # Break out of the loop if the essay meets the word count requirement
                else:
                    # print("The generated essay is under 250 words. Regenerating...")
                    continue 
            break  # Break out of the while loop if the generation is successful
        except Exception as e:
            print("An error has occurred:", e)
            print("Retrying...")
            continue
   
def count_words():
    more_details = st.button('more details')
    if more_details:
        st.markdown('##Here are the most repeated words in your essay')
        stop_w = set(STOPWORDS)
        #words = essay
        word_cloud = WordCloud(stopwords=stop_w).generate(essay)
        img = word_cloud.to_image()
        st.image(img)


#prompts
tas_prompt = f"""
    you are an IELTS examiner and your roll is to check IELTS Writing Essays
    in {task}, your task is to check only the TASK RESPONSE in this {essay} based on the TASK RESPONSE official asssement provided by IELTS.org
    i will give you the instructions how to measure the TASK RESPONSE according to the IELTS official website and you should follow it 
    
    For {task} of both AC Writing tests, candidates are required to formulate and 
    develop a position in relation to a given prompt in the form of a question or 
    statement, using a minimum of 250 words and the number of words that the candidate has been written is {num_words}. 
    Ideas should be supported by evidence, 
    and examples may be drawn from a candidate’s own experience.
    
    TASK RESPONSE (TR) 
    The TR criterion assesses:
    
    - how fully the candidate responds to the task.
    - how adequately the main ideas are extended and supported. 
    - how relevant the candidate’s ideas are to the task. 
    - how clearly the candidate opens the discourse, establishes their position and formulates conclusions. 
    - how appropriate the format of the response is to the task.

    
    Below are the band descriptors for the TR criterion:
    
     Band 9: The prompt is appropriately addressed and explored in depth. A clear and fully developed position is presented which directly answers the question/s. Ideas are relevant, fully extended and well supported. Any lapses in content or support are extremely rare.

    Band 8: The prompt is appropriately and sufficiently addressed. A clear and well-developed position is presented in response to the question/s. Ideas are relevant, well extended and supported. There may be occasional omissions or lapses in content.
    
    Band 7: The main parts of the prompt are appropriately addressed. A clear and developed position is presented. Main ideas are extended and supported but there may be a  tendency to over-generalise or there may be a lack of focus and  precision in supporting ideas/material.
        
    Band 6: The main parts of the prompt are addressed (though some may be more fully covered than others). An appropriate format is used. A position is presented that is directly relevant to the prompt, although the conclusions drawn may be unclear, unjustified or repetitive. Main ideas are relevant, but some may be insufficiently developed or may lack clarity, while some supporting arguments and evidence may be less relevant or inadequate.
        
    Band 5: The main parts of the prompt are incompletely addressed. The format may be inappropriate in places. The writer expresses a position, but the development is not always clear. Some main ideas are put forward, but they are limited and are not sufficiently developed and/or there may be irrelevant detail. There may be some repetition.
        
    Band 4: The prompt is tackled in a minimal way, or the answer istangential, possibly due to some misunderstanding of the prompt. The format may be inappropriate. A position is discernible, but the reader has to read carefullyto find it. Main ideas are difficult to identify and such ideas that are identifiable may lack relevance, clarity and/or support. Large parts of the response may be repetitive.
        
    Band 3: No part of the prompt is adequately addressed, or the prompt has been misunderstood. No relevant position can be identified, and/or there is little direct response to the question/s. There are few ideas, and these may be irrelevant or insufficiently developed
        
    Band 2: The content is barely related to the prompt. No position can be identified. There may be glimpses of one or two ideas without development.
        
    Band 1: Responses of 20 words or fewer are rated at Band 1. The content is wholly unrelated to the prompt. An co ied rubric must be discounted.

    Band 0: The candidate did not attempt the task, so no assessment of task response can be made.
     
    NOTE: you do not need to give an explicit number such as 7 you can also give a fraction number if it is possible such as 6.5 etc..
    
    in the end you should explain why you gave him this band score and what he should do to improve it
    
    i want the structure of your response looks like:
    first in the beginning write the band score for example: Bnnd Score : ....
    
    then write an about your evaluation in details and explain why this eesay deserve this band score
    after that write suggetions to improve the writing in organized points
   
    
    """
co_prompt = f"""
    you are an IELTS examiner and your roll is to check IELTS Writing Essays
    in {task}, your task is to check only the COHERENCE AND COHESION in this {essay}  based on the COHERENCE AND COHESION official asssement provided by IELTS.org
    i will give you the instructions how to measure the COHERENCE AND COHESION according to the IELTS official website and you should follow it
    
    COHERENCE AND COHESION (CC) 
    This criterion is concerned with the overall organisation and logical development of 
    the message: how the response organises and links information, ideas and language. 
    Coherence refers to the linking of ideas through logical sequencing, while cohesion 
    refers to the varied and appropriate use of cohesive devices (e.g. logical connectors, 
    conjunctions and pronouns) to assist in making clear the relationships between and 
    within sentences.
    
    The CC criterion assesses: 
    - the coherence of the response via the logical organisation of information 
      and/or ideas,   or the logical progression of the argument.
    - the appropriate use of paragraphing for topic organisation and presentation.
    - the logical sequencing of ideas and/or information within and across 
      paragraphs.
    - the flexible use of reference and substitution (e.g. definite articles, pronouns). 
    - the appropriate use of discourse markers to clearly mark the stages in a 
      response, e.g. [First of all | In conclusion], and to signal the relationship between 
      ideas and/or information, e.g. [as a result | similarly]
      
    you should be fair when you assess this criteria and give a band score and provide some explanation 
    
    Below are the band descriptors for the CC criterion:
    
    Band 9: The message can be followed effortlessly. Cohesion is used in such a way that it very rarely attracts attention. Any lapses in coherence or cohesion are minimal. Paragraphing is skilfully managed.
    
    Band 8: The message can be followed with ease. Information and ideas are logically sequenced, and cohesion is well managed. Occasional lapses in coherence and cohesion may occur. Paragraphing is used sufficiently and appropriately.
        
    Band 7: Information and ideas are logically organised, and there is a clear progression throughout the response. (A few lapses may occur, but these are minor.) A range of cohesive devices including reference and substitution is used flexibly but with some inaccuracies or some over/under use. Paragraphing is generally used effectively to support overall coherence, and the sequencing of ideas within a paragraph is generally logical.
        
    Band 6: Information and ideas are generally arranged coherently and there is a clear overall progression. Cohesive devices are used to some good effect but cohesion within and/or between sentences may be faulty or mechanical due to misuse, overuse or omission. The use of reference and substitution may lack flexibility or clarity and result in some repetition or error. Paragraphing may not always be logical and/or the central topic may not always be clear.
        
    Band 5: Organisation is evident but is not wholly logical and there may be a lack of overall progression. Nevertheless, there is a sense of underlying coherence to the response. The relationship of ideas can be followed but the sentences are not fluently linked to each other. There may be limited/overuse of cohesive devices with some inaccuracy. The writing may be repetitive due to inadequate and/or inaccurate use of reference and substitution. Paragraphing may be inadequate or missin
        
    Band 4: Information and ideas are evident but not arranged coherently and there is no clear progression within the response. Relationships between ideas can be unclear and/or inadequately marked. There is some use of basic cohesive devices, which may be inaccurate or repetitive. There is inaccurate use or a lack of substitution or referencing. There may be no paragraphing and/or no clear main topic within paragraphs.
    
    Band 3: There is no apparent logical organisation. Ideas are discernible but difficult to relate to each other. There is minimal use of sequencers or cohesive devices. Those used do not necessarily indicate a logical relationship ideas. There is difficulty in identifying referencing. An attem tsat ara ra hin are unhelpful.
        
    Band 2: There is little relevant message, or the entire response may be off-topic. There is little evidence of control of organisational features.
        
    Band 1: Responses of 20 words or fewer are rated at Band 1. The writing fails to communicate any message and appears to be by a virtual non-writer.
    
    Band 0: The candidate did not attempt the task, so no assessment of coherence and cohesion can be made.
   
   NOTE: you do not need to give an explicit number such as 7 you can also give a fraction number if it is possible such as 6.5 etc..
    
    in the end you should explain why you gave him this band score and what he should do to improve it
    
    i want the structure of your response looks like:
    first in the beginning write the band score for example: Bnnd Score : ....
    
    then write an about your evaluation in details and explain why this eesay deserve this band score
    after that write suggetions to improve the writing in organized points
    
    """
lex_prompt = f"""
    you are an IELTS examiner and your roll is to check IELTS Writing Essays
    in {task}, your task is to check only the LEXICAL RESOURCE in this {essay} based on the LEXICAL RESOURCE official asssement provided by IELTS.org
    i will give you the instructions how to measure the LEXICAL RESOURCE according to the IELTS official website and you should follow it
    
    LEXICAL RESOURCE (LR) :
    This criterion refers to the range of vocabulary the candidate has used and the 
    accuracy and appropriacy of that use in terms of the specific task. 
    The LR criterion assesses:
    
    - the range of general words used (e.g. the use of synonyms to avoid repetition)
    - the adequacy and appropriacy of the vocabulary (e.g. topic-specific items, 
      indicators of writer’s attitude). 
    - the precision of word choice and expression. 
    - the control and use of collocations, idiomatic expressions and sophisticated 
      phrasing. 
    - the density and communicative effect of errors in spelling. 
    - the density and communicative effect of errors in word formation.
    
    you should be fair when you assess this criteria and give a band score and provide some explanation
    
    Below are the band descriptors for the LR criterion:
    
    Band 9: Full flexibility and precise use are widely evident. A wide range of vocabulary is used accurately and appropriately with very natural and sophisticated control of lexical features. Minor errors in spelling and word formation are extremely rare and have minimal impact on communication.
        
    Band 8: A wide resource is fluently and flexibly used to convey precise meanings. There is skilful use of uncommon and/or idiomatic items when appropriate, despite occasional inaccuracies in word choice and collocation. Occasional errors in spelling and/or word formation may occur, but have minimal impact on communication.
        
    Band 7: The resource is sufficient to allow some flexibility and precision. There is some ability to use less common and/or idiomatic items. An awareness of style and collocation is evident, though inappropriacies occur. There are only a few errors in spelling and/or word formation and they do not detract from overall clarity.
        
    Band 6: The resource is generally adequate and appropriate for the task. The meaning is generally clear in spite of a rather restricted range or a lack of precision in word choice. If the writer is a risk-taker, there will be a wider range of vocabulary used but higher degrees of inaccuracy or inappropriacy. There are some errors in spelling and/or word formation, but these do not impede communication.
        
    Band 5: The resource is limited but minimally adequate for the task. Simple vocabulary may be used accurately but the range does not permit much variation in expression. There may be frequent lapses in the appropriacy of word choice and a lack of flexibility is apparent in frequent si mplifications and/or repetitions. Errors in spelling and/or word formation may be noticeable and may cause some difficulty for the reader.
        
    Band 4: The resource is limited and inadequate for or unrelated to the task. Vocabulary is basic and may be used repetitively. There may be inappropriate use of lexical chunks (e.g. memorised phrases, formulaic language and/or language from the input material). I nappropriate word choice and/or errors in word formation and/or in spelling may impede meaning.
        
    Band 3: The resource is inadequate (which may be due to the response being significantly underlength). Possible over-dependence on input material or memorised language. Control of word choice and/or spelling is very limited, and errors predominate. These errors may severely impede meaning.
        
    Band 2: The resource is extremely limited with few recognisable strings, apart from memorised phrases. There is no apparent control of word formation and/or spellin
        
    Band 1: Responses of 20 words or fewer are rated at Band 1. No resource is apparent, except for a few isolated words.
        
    Band 0: The candidate did not attempt the task, so no assessment of lexical resource can be made.
    
    NOTE: you do not need to give an explicit number such as 7 you can also give a fraction number if it is possible such as 6.5 etc..
    
    in the end you should explain why you gave him this band score and what he should do to improve it
    
    i want the structure of your response looks like:
    first in the beginning write the band score for example: Bnnd Score : ....
    
    then write an about your evaluation in details and explain why this eesay deserve this band score
    after that write suggetions to improve the writing in organized points
    
    """
gr_prompt = f"""
    you are an IELTS examiner and your roll is to check IELTS Writing Essays
    in {task}, your task is to check only the grammar in this {essay} only grammar based on the grammar official asssement provided by IELTS.org
    i will give you the instructions how to measure the grammar according to the IELTS official website and you should follow it
    GRAMMATICAL RANGE AND ACCURACY (GRA):
    This criterion refers to the range and accurate use of the candidate'’'s grammatical 
    resource via the candidate's writing at sentence level. 
    The GRA criterion assesses:
    
    - the range and appropriacy of structures used in a given response (e.g. simple,
      compound and complex sentences).
    - the accuracy of simple, compound and complex sentences.
    - the density and communicative effect of grammatical errors.
    - the accurate and appropriate use of punctuation.
    
    you should be fair when you assess this criteria and give a band score and provide some explanation 
    
    Below are the band descriptors for the GRA criterion:

    Band 9: A wide range of structures is used with full flexibility and control. Punctuation and grammar are used appropriately throughout. Minor errors are extremely rare and have minimal impact on communication.
    
    Band 8: A wide range of structures is flexibly and accurately used. The majority of sentences are error-free, and punctuation is well managed. Occasional, non-systematic errors and inappropriacies occur, but have minimal impact on communication.
    
    Band 7: A variety of complex structures is used with some flexibility and accuracy. Grammar and punctuation are generally well controlled, and error-free sentences are frequent. A few errors in grammar may persist, but these do not impede communication.
    
    Band 6: A mix of simple and complex sentence forms is used but flexibility is limited. Examples of more complex structures are not marked by the same level of accuracy as in simple structures. Errors in grammar and punctuation occur, but rarely impede communication.
    
    Band 5: The range of structures is limited and rather repetitive. Although complex sentences are attempted, they tend to be faulty, and the greatest accuracy is achieved on simple sentences. Grammatical errors may be frequent and cause some difficultyfor the reader. Punctuation may be faulty.
    
    Band 4: A very limited range of structures is used. Subordinate clauses are rare and simple sentences predominate. Some structures are produced accurately but grammatical errors are frequent and may impede meaning. Punctuation is often faulty or inadequate.
    
    Band 3: Sentence forms are attempted, but errors in grammar and punctuation predominate (except in memorised phrases or those taken from the input material). This prevents most meaning from coming through. Length may be insufficient to provide evidence of control of sentence forms.
    
    Band 2: There is little or no evidence of sentence forms (except in memorised phrases).
    
    Band 1: Responses of 20 words or fewer are rated at Band 1. No rateable language is evident.
    
    Band 0: The candidate did not attempt the task.
   
   NOTE: you do not need to give an explicit number such as 7 you can also give a fraction number if it is possible such as 6.5 etc..
    
    in the end you should explain why you gave him this band score and what he should do to improve it
    
    i want the structure of your response looks like:
    first in the beginning write the band score for example: Bnnd Score : ....
    
    then write an about your evaluation in details and explain why this eesay deserve this band score
    after that write suggetions to improve the writing in organized points
    """

tas_academic_task1 = f"""
    you are an IELTS examiner and your roll is to check IELTS Writing Essays
    in academic {task}, your task is to check only the TASK RESPONSE in this {essay} based on the TASK RESPONSE official asssement provided by IELTS.org
    i will give you the instructions how to measure the TASK RESPONSE according to the IELTS official website and you should follow it 
    
    This Writing {task} has a defined input and a largely predictable output. It is basically an 
    information-transfer task, which relates narrowly to the factual content of a diagram, 
    graph, table, chart, map or other visual input, not to speculative explanations that lie 
    outside the given data. and the here is the description of the chart or whatever the task {described_image} if it is avaliable and you should use it as a referance
    The TA criterion assesses the ability to summarise the information provided in the 
    diagram by: 
    - selecting key features of the information. 
    - providing sufficient detail to illustrate these features. 
    - reporting the information, figures and trends accurately. 
    - comparing or contrasting the information by adequately highlighting the identifiable trends, principal changes or differences in the data and other inputs (rather than mechanical description reporting detail). 
    - presenting the response in an appropriate format.
    
        
    you should be fair when you assess this criteria and give a band score and provide some explanation 
    
    Below are the band descriptors for the task response task 1 criterion:
    
    Band 9: All the requirements of the task are fully and appropriately satisfied.
    
    Band 8: The response covers all the requirements of the task appropriately, relevantly and sufficiently. 
        There may be occasional omissions or lapses in content. Key features are skilfully selected, and clearly presented, highlighted and illustrated
    
    Band 7: The response covers the requirements of the task. The content is relevant and accurate – 
        there may be a few omissions or lapses. The format is appropriate.  Key features which are selected are covered and clearly highlighted but could be more fully or more appropriately illustrated or extended. 
        It presents a clear overview, the data are appropriately categorised, and main trends or differences are identified.
    
    Band 6: The response focuses on the requirements of the task and an appropriate format is used. Some irrelevant, 
        inappropriate or inaccurate information may occur in areas of detail or when illustrating or extending the main points. 
        Some details may be missing (or excessive) and further extension or illustration may be needed. Key features which are selected are covered and adequately highlighted. A relevant overview is attempted. Information is appropriately 
        selected and supported using figures/data.
    
    Band 5: The response generally addresses the requirements of the task. The format may be inappropriate in places. 
        There may be a tendency to focus on details (without referring to the bigger picture). The inclusion of irrelevant, 
        inappropriate or inaccurate material in key areas detracts from the task achievement. There is limited detail when extending and illustrating the main points. 
        Key features which are selected are not adequately covered. The recounting of detail is mainly mechanical. There may be no data to support the description.
    
    Band 4: The response is an attempt to address the task. Few key features have been selected.  Few key features have been selected.
    
    Band 3: Key features/bullet points which are presented may be irrelevant, repetitive, inaccurate or inappropriate. The response does not address the requirements of the task (possibly because of misunderstanding of the data/diagram/situation). Key features/bullet points which are presented may be largely irrelevant. Limited information is presented, and this may be used repetitively.
    
    Band 2: The content barely relates to the task.
    
    Band 1: The content is wholly unrelated to the task. Any copied rubric must be discounted. Responses of 20 words or fewer are rated at Band 1.
    
    i want the structure of your response looks like:
    first in the beginning write the band score for example: Bnnd Score : ....
    
    then write an about your evaluation in details and explain why this eesay deserve this band score
    after that write suggetions to improve the writing in organized points

"""

tas_general_task1 = f"""
you are an IELTS examiner and your roll is to check IELTS Writing Essays
in General {task}, your task is to check only the TASK RESPONSE in this {essay} based on the TASK RESPONSE official asssement provided by IELTS.org
i will give you the instructions how to measure the TASK RESPONSE according to the IELTS official website and you should follow it 
    
This Writing {task} also has a largely predictable output in that each task sets out the 
    context and purpose of the letter and the functions the candidate should cover in 
    order to achieve this purpose. 
    The TA criterion assesses the ability to: 
    - clearly explain the purpose of the letter. 
    - fully address the three bullet-pointed requirements set out in the task. 
    - extend these three functions appropriately and relevantly. 
    - use an appropriate format for the letter. 
    - consistently use a tone appropriate to the task.




you should be fair when you assess this criteria and give a band score and provide some explanation 
    
    Below are the band descriptors for the task response task 1 criterion:
    
    Band 9: All the requirements of the task are fully and appropriately satisfied.
    
    Band 8: The response covers all the requirements of the task appropriately, relevantly and sufficiently. 
        There may be occasional omissions or lapses in content. All bullet points are clearly presented, 
        and appropriately illustrated or extended.
    
    Band 7: The response covers the requirements of the task. The content is relevant and accurate – 
        there may be a few omissions or lapses. The format is appropriate.  All bullet points are covered and 
        clearly highlighted but could be more fully or more appropriately illustrated or extended. It presents a clear purpose. 
        The tone is consistent and appropriate to the task. Any lapses are minimal.
    
    Band 6: The response focuses on the requirements of the task and an appropriate format is used. Some irrelevant, 
        inappropriate or inaccurate information may occur in areas of detail or when illustrating or extending the main points.
        Some details may be missing (or excessive) and further extension or illustration may be needed. 
        All bullet points are covered and adequately highlighted. The purpose is generally clear. There may be minor inconsistencies in tone.
    
    Band 5: The response generally addresses the requirements of the task. The format may be inappropriate in places. 
        There may be a tendency to focus on details (without referring to the bigger picture. The inclusion of irrelevant, 
        inappropriate or inaccurate material in key areas detracts from the task achievement. 
        There is limited detail when extending and illustrating the main points. All bullet points are presented but one or more may not be adequately covered. 
        The purpose may be unclear at times. The tone may be variable and sometimes inappropriate
    
    Band 4: The response is an attempt to address the task. he format may be inappropriate. Few key features have been selected.  Not all bullet points are presented.  
        The purpose of the letter is not clearly explained and may be confused. The tone may be inappropriate
    
    Band 3: Key features/bullet points which are presented may be irrelevant, repetitive, inaccurate or inappropriate. The response does not address the requirements of the task (possibly because of misunderstanding of the data/diagram/situation). Key features/bullet points which are presented may be largely irrelevant. Limited information is presented, and this may be used repetitively.
    
    Band 2: The content barely relates to the task.
    
    Band 1: The content is wholly unrelated to the task. Any copied rubric must be discounted. Responses of 20 words or fewer are rated at Band 1.
    
    i want the structure of your response looks like:
    first in the beginning write the band score for example: Bnnd Score : ....
    
    then write an about your evaluation in details and explain why this eesay deserve this band score
    after that write suggetions to improve the writing in organized points

"""

task_response = f""""""
if task == 'Task 1' and gen_acad == 'Academic':
    task_response = tas_academic_task1
elif task == 'Task 1' and gen_acad == 'General':
    task_response = tas_general_task1

else:
    task_response = tas_prompt

def extract_digit_from_essay(essay):
    digit = re.search(r'(?:^|\D)([3-9](?:\.\d+)?)(?!\d)', essay)
    if digit:
        return digit.group(1)
    else:
        return None
 
overall_band_score = []
def evaluate2(prompt):
    genai.configure(api_key = used_key)
    while True:
        try:
            task = model.generate_content(prompt, stream=True)
            task.resolve()
            task_ch = task.text
            st.write(task_ch)
            task_score = float(extract_digit_from_essay(task_ch))
            
            overall_band_score.append(task_score)
            break  # Break out of the while loop if the generation is successful
        except Exception  as e:
            print("An internal error has occurred:", e)
            print("Retrying...")
            continue
    
def grammar_spling():
    prompt = f"""As a grammar checker, your task is to carefully review the provided essay {essay} and identify any misspelled words and incorrect grammar. 
    When you encounter misspelled words, please provide the correct spelling, taking into account the differences between British and American English. 
    For incorrect grammar, you should also provide the correct grammar structure and an explanation of its correctness.
    providing accurate corrections for misspelled words and grammar errors. When addressing spelling, please consider both British and American English conventions. 
    Additionally, your explanations should help the writer understand why the provided corrections are accurate and how they improve the overall language usage in the essay.
   
    Note: you should only highlight the misuse of grammar and provide the correct structure and do not rewrite the correct essay 
   if there are no misspelling mistakes or incorrect grammar you should write your grammar and spelling is correct 
    """
    while True:
        try:
            task = model.generate_content(prompt, stream=True)
            task.resolve()
            task_ch = task.text
            st.write(task_ch)
            
            
            break  # Break out of the while loop if the generation is successful
        except Exception  as e:
            print("An internal error has occurred:", e)
            print("Retrying...")
            continue

# def extract_hand_written():
#     pytesseract.pytesseract.tesseract_cmd = 'C:/Users/B/Desktop/IELTS-WRITING-PROJECT/Tesseract/tesseract.exe'
#     image_path = essay_image
#     extracted_text = pytesseract.image_to_string(Image.open(image_path))
#     print(extracted_text)

if button:
    
    if q_words == 0:
        st.error(f'Please write the question ')
    elif num_words == 0:
        st.error(f'Please write your essay')
    elif task == 'Task 1' and num_words < 150 :
        st.error(f'Your essay is short the written words is {num_words}, please continue writing it should be at least 150 words')
    elif task == 'Task 2' and num_words < 250:
        st.error(f'Your essay is short the written words is {num_words}, please continue writing it should be at least 250 words')
    else:
        
        st.markdown('---')
        decripe_image(used_key)
        
        st.markdown("## Task Response")
        evaluate2(task_response)
        
        st.markdown('---')
        st.markdown("## Coherence and Cohesive")
        evaluate2(co_prompt)
        st.markdown('---')
        st.markdown("## Lexical Resources")
        evaluate2(lex_prompt)
        st.markdown('---')
        st.markdown("## Grammar and Acurrecy")
        evaluate2(gr_prompt)
        st.markdown('**- Grammar and Spelling mistakes**')
        grammar_spling()
        
        st.markdown('---')
        overall_score = round(sum(overall_band_score) /4)
        st.markdown(f"## Overall Band Score: {float(overall_score)} / 9")
        st.markdown('---')
        st.markdown('## Here is the most repeated words in your essay')
        stop_w = set(STOPWORDS)
            
        word_cloud = WordCloud(stopwords=stop_w, width= 800, height=400, background_color='white').generate(essay)
        img = word_cloud.to_image()
        st.image(img)
        st.markdown('---')
        words_charts()
        st.markdown('---')
        st.markdown('### Recommended Synonyms of the repeated words')
        synonym(Gemini_API_Key2)
        st.markdown('---')
        
        st.markdown('### Here is a rewritten version of your essay')
        rewrite_essay(Gemini_API_Key3)
        
        # print((overall_band_score))
        