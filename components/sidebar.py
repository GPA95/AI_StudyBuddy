import streamlit as st

def sidebar_ui():
    """Sidebar with mode selector and chat controls."""

    st.sidebar.title("⚙️ Settings")

    # API choice (fixed for now)
    st.sidebar.markdown("### 🤖 Model")
    st.sidebar.info("Using **Gemini 2.5 Flash**")

    # Mode selection
    st.sidebar.markdown("### 🧩 Choose Mode")
    mode = st.sidebar.radio(
        "Select a core function:",
        ["Explainer", "Summarizer", "Quizzer"],
        index=0
    )

    # Divider
    st.sidebar.markdown("---")

    # New chat button
    if st.sidebar.button("🆕 New Chat"):
        st.session_state.messages = []
        st.sidebar.success("Started a new chat!")

    # Divider
    st.sidebar.markdown("---")

    # GitHub Repository link
    st.sidebar.markdown("### 🧭 Project Links")
    st.sidebar.markdown(
        """
        [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/GPA95/AI_StudyBuddy)
        """
    )

    # Footer note
    st.sidebar.markdown("---")
    st.sidebar.caption("✨ StudyBuddy - AI Powered Study Assistant")

    return mode
