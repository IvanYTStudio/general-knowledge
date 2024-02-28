import streamlit as st
import random

with open('questions.txt') as questions_txt:
    questions = [questions.replace('\n', '') for questions in questions_txt.readlines()]

with open('answers.txt') as answers_txt:
    answers = [answer.replace('\n','') for answer in answers_txt.readlines()]

num_of_questions = len(questions)

def generate_question_and_answer():
    q_index = random.randint(0, num_of_questions)
    return questions[q_index], answers[q_index]

st.set_page_config(page_title='General Knowledge', page_icon='favicon.ico', layout='wide')

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

question, answer = generate_question_and_answer()

st.title(question, anchor='question')

col1, col2, col3 = st.columns([1,7,1])

with col2:
    st.title(answer, anchor='answer')
    st.title('Hover for answer', anchor='reveal_button')

col4, col5, col6 = st.columns([1.5,3,1])

with col4:
    st.title('4200+ questions', anchor='questions')
    st.title('From The General Knowledge Quiz Book', anchor='tribute')

with col6:
    st.title("Press 'R' for a new question", anchor='help')