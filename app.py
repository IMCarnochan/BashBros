
import streamlit as st
import pandas as pd
import random

# Load CSV file
@st.cache_data
def load_words(csv_file):
    df = pd.read_csv(csv_file)
    return df["Word"].tolist()

st.title("Warren & Logan's D&D Bash Bros Battlecry")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV of D-words", type="csv")

if uploaded_file:
    words = load_words(uploaded_file)

    if st.button("Generate Battle Cry!"):
        if len(words) >= 2:
            warren_word, logan_word = random.sample(words, 2)
            st.subheader("**Warren shouts:**")
            st.success(warren_word)
            st.subheader("**Logan screams:**")
            st.warning(logan_word)
        else:
            st.error("Need at least 2 unique words to proceed.")
