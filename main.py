import streamlit as st

def main():
    st.set_page_config(page_title="Kuis Pemula", page_icon="📚")
    st.markdown("Selamat Datang di Kuis Pemula! Pemula atau Pemain udah lama?")
    
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
    
    if st.button("Mulai"):
        st.session_state.page = "quiz"
        st.rerun()
        
if __name__ == "__main__":
    main()
