import streamlit as st
import json
import random

def run_quiz():
    if 'quiz_data' not in st.session_state:
        with open('questions.json', 'r', encoding='utf-8') as f:
            quiz_data = json.load(f)
        st.session_state.quiz_data = random.sample(quiz_data, 5)
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.selected_option = None
        st.session_state.answer_submitted = False
        
    question_item = st.session_state.quiz_data[st.session_state.current_index]
    st.write(f"Pertanyaan {st.session_state.current_index + 1}")
    st.subheader(question_item['question'])
    
    st.markdown(""" ___""")

    options = question_item['options']
    correct_answer = question_item['answer']

    st.markdown("""
    <style>
    div.stButton > button:first-child {
        display: block;
        margin: 0 auto;
        width: 100%;
        text-align: center;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
        
    if st.session_state.answer_submitted:
        for option in options:
            if option == correct_answer:
                st.success(f"{option} (Correct answer)")
            elif option == st.session_state.selected_option:
                st.error(f"{option} (Incorrect answer)")
    else:
        cols = st.columns(2)
        
        for i, option in enumerate(options):
            with cols[i % 2]:
                if st.button(option):
                    st.session_state.selected_option = option
                
    st.markdown(""" ___""")
    
    if st.session_state.answer_submitted:
        if st.session_state.current_index < len(st.session_state.quiz_data) - 1:
            st.button('Next', on_click=lambda: next_question())
        else:
            st.write(f"Quiz completed! Your score is: {st.session_state.score} / {len(st.session_state.quiz_data) * 10}")
            if st.button("Selesai"):
                st.session_state.page = "main"
                restart_quiz()
                st.rerun()
    else:
        if st.button('Submit'):
            submit_answer()

def submit_answer():
    if st.session_state.selected_option is not None:
        st.session_state.answer_submitted = True
        if st.session_state.selected_option == st.session_state.quiz_data[st.session_state.current_index]['answer']:
            st.session_state.score += 10
        st.rerun()
    else:
        st.warning("Tolong pilih jawaban sebelum klik submit.")
        
def next_question():
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False
    
def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False
    
if __name__ == "__main__":
    run_quiz()
    