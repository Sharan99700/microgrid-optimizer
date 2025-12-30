import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Indian Army Microgrid Optimizer",
    layout="wide"
)

# Read HTML file
html_file = Path("new.html").read_text(encoding="utf-8")

# Render HTML
st.components.v1.html(
    html_file,
    height=1200,
    scrolling=True
)
