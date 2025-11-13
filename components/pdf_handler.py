import streamlit as st
from PyPDF2 import PdfReader

def handle_pdf_upload():
    """
    Handles PDF upload with editable extraction.
    Returns tuple: (pdf_text, user_extra_prompt, summarize_clicked)
    """
    uploaded_file = st.file_uploader("📚 Upload your study material (PDF)", type=["pdf"])
    pdf_text = ""
    user_extra = ""

    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            try:
                reader = PdfReader(uploaded_file)
                for page in reader.pages:
                    pdf_text += page.extract_text() or ""
            except Exception as e:
                st.error(f"❌ Error reading PDF: {str(e)}")
                return None, None, False
        
        st.success("✅ PDF processed successfully!")
        
        # Let user edit the extracted text
        st.markdown("### 📝 Review & Edit Extracted Text")
        pdf_text = st.text_area(
            "Edit extracted text below (review, trim, or add notes):",
            value=pdf_text[:3000] if pdf_text else "",
            height=300,
            help="You can modify the text before summarizing"
        )
        
        # Extra custom prompt for summarization
        st.markdown("### 🎯 Customization Options")
        user_extra = st.text_input(
            "Any specific focus? (e.g., 'Focus on applications', 'Make exam-ready', 'Explain with examples')",
            placeholder="Leave empty for general summary",
            help="This will guide the AI on how to summarize"
        )
        
        # Summarize button
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🚀 Summarize", use_container_width=True):
                if pdf_text.strip():
                    return pdf_text, user_extra, True
                else:
                    st.warning("⚠️ No text to summarize. Please upload a valid PDF.")
                    return None, None, False
        
        with col2:
            if st.button("🔄 Clear", use_container_width=True):
                st.rerun()
        
        return pdf_text, user_extra, False
    
    return None, None, False