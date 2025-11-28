import streamlit as st
import time
def sidebar_ui():
    """Sidebar with mode and Quizzer sub-mode selectors, and core controls."""

    st.sidebar.title("⚙️ Settings")

    # API/info
    st.sidebar.markdown("### API Model")
    st.sidebar.info("**Gemini 2.5 Flash**")

    # Mode selection
    st.sidebar.markdown("### 🧩 Choose Mode")
    mode = st.sidebar.radio(
        "Select a core function:",
        ["💡 Explainer", "📰 Summarizer", "🧩 Quizzer"],
        index=0
    )

    # Nested radio for Quizzer
    sub_mode = None
    if mode == "🧩 Quizzer":
        st.sidebar.markdown("### ✨ Quizzer Action")
        sub_mode = st.sidebar.radio(
            "Choose Quizzer action:",
            [
                "📝 Generate Questions",
                "📖 Solve Questions",
                "✅ Evaluate Answers"
            ],
            index=0
        )

    st.sidebar.markdown("---")
    if st.sidebar.button("🆕 New Chat"):
        st.session_state.messages = []
        # Success message that auto-disappears after 2 seconds
        success_placeholder = st.sidebar.empty()
        with success_placeholder.container():
            st.success("Started a new chat!")
        time.sleep(2)
        success_placeholder.empty()

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        [![Watch Demo](https://img.shields.io/badge/Watch-Demo%20Video-red?logo=youtube)](https://youtu.be/Yd0xMocB-V0)
        [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/GPA95/AI_StudyBuddy)
        [![HelpDoc](https://img.shields.io/badge/User%20Help-How%20to%20Use-blue?logo=google-drive)](https://drive.google.com/file/d/14NEdW6L4WC_hiqlhNBEElzJnfN60EZDa/view?usp=sharing)
        """
    )
    st.sidebar.markdown("---")
    st.sidebar.caption("✨ StudyBuddy - AI Powered Study Assistant")

    return mode, sub_mode
