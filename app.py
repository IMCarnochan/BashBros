
import streamlit as st
import pandas as pd
import random
import os

# Load words from selected CSV
@st.cache_data
def load_words(csv_filename):
    df = pd.read_csv(csv_filename)
    return df["Word"].tolist()

st.title("Warren & Logan's D-Word Duel")

# Dropdown to select from one of the five preloaded CSVs
csv_files = {
    "DnD001": "DnD001.csv",
    "DnD002": "DnD002.csv",
    "DnD003": "DnD003.csv",
    "DnD004": "DnD004.csv",
    "DnD005": "DnD005.csv"
}

selected_file = st.selectbox("Choose your word list:", list(csv_files.keys()))
csv_path = os.path.join(os.path.dirname(__file__), csv_files[selected_file])

words = load_words(csv_path)

if st.button("Generate Battle Cry!"):
    if len(words) >= 2:
        warren_word, logan_word = random.sample(words, 2)
        st.subheader("**Warren shouts:**")
        st.success(warren_word)
        st.subheader("**Logan screams:**")
        st.warning(logan_word)
    else:
        st.error("Need at least 2 unique words to proceed.")
