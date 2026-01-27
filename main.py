import streamlit as st
from components.sidebar import sidebar_ui
from components.chat_ui import chat_ui
from components.pdf_handler import handle_pdf_upload

st.set_page_config(page_title="SGPA", page_icon="🧠", layout="wide")

# Initialize session state
if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = None
if "user_focus" not in st.session_state:
    st.session_state.user_focus = ""

# Unpack the tuple returned by sidebar_ui()
selected_mode, selected_sub_mode = sidebar_ui()

# Header
st.title("🧠 SGPA")
st.subheader("Study Guide & Personal Assistant")

# PDF Handler (optional upload)
st.markdown("### 📚 Upload a PDF (Optional)")
pdf_text, user_focus, summarize_clicked = handle_pdf_upload()

if summarize_clicked and pdf_text:
    st.session_state.pdf_content = pdf_text
    st.session_state.user_focus = user_focus
    st.divider()
    st.success("✅ PDF loaded! Starting summary chat...")

st.divider()

# Pass mode and sub_mode separately to chat_ui
chat_ui(selected_mode, selected_sub_mode)