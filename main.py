import streamlit as st
from components.sidebar import sidebar_ui
from components.chat_ui import chat_ui
from components.pdf_handler import handle_pdf_upload
from core.summarizer import summarize_text

st.set_page_config(page_title="StudyBuddy", page_icon="🧠", layout="wide")

# Initialize session state for PDF context
if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = None
if "user_focus" not in st.session_state:
    st.session_state.user_focus = ""

# Sidebar
selected_mode = sidebar_ui()

# Header
st.title("🧠 StudyBuddy - Your Smart Study Assistant")

# PDF Handler (optional upload)
st.markdown("### 📚 Upload a PDF (Optional)")
pdf_text, user_focus, summarize_clicked = handle_pdf_upload()

# Store in session state if summarize was clicked
if summarize_clicked and pdf_text:
    st.session_state.pdf_content = pdf_text
    st.session_state.user_focus = user_focus
    st.divider()
    st.success("✅ PDF loaded! Starting summary chat...")

# Main chat interface
st.divider()

# Specialized chat UI when PDF context is available
def chat_ui_with_pdf_context(selected_mode, pdf_text, user_focus):
    """Chat UI specifically for Summarizer with PDF context."""
    st.subheader(f"💬 StudyBuddy Chat — Mode: {selected_mode}")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Initial summary generation
    if len(st.session_state.messages) == 0:
        with st.chat_message("assistant"):
            with st.spinner("💡 Generating summary from your PDF..."):
                initial_summary = summarize_text(pdf_text, user_focus=user_focus)
                st.markdown(initial_summary)
                st.code(initial_summary, language="markdown")
            
            st.session_state.messages.append({"role": "assistant", "content": initial_summary})
    
    # Follow-up questions
    prompt = st.chat_input("Ask follow-up questions about the summary...")
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("💡 Study Buddy is thinking…"):
                response = summarize_text(f"{prompt}\n\nBased on: {pdf_text[:1000]}", user_focus=user_focus)
                st.markdown(response)
                st.code(response, language="markdown")
            
            st.session_state.messages.append({"role": "assistant", "content": response})

# Pass PDF context to chat UI if available
if st.session_state.pdf_content and selected_mode == "Summarizer":
    chat_ui_with_pdf_context(selected_mode, st.session_state.pdf_content, st.session_state.user_focus)
else:
    chat_ui(selected_mode)