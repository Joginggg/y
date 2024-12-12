import streamlit as st
from main import main as main_page
from quiz import run_quiz

st.set_page_config(page_title="Kuis Pemula", page_icon="")

def run():
    if 'page' not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "quiz":
        run_quiz()

if __name__ == "__main__":
    run()