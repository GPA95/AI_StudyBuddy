import streamlit as st
from core.explainer import explain_concept
from core.summarizer import summarize_text
from core.quizzer import generate_quiz
import time

def get_previous_messages_summary(messages, limit=3):
    """
    Summarize or serialize the last few exchanges for context.
    Returns a string that will be given to the model for follow-up responses.
    """
    # Only show the last `limit` user+assistant turns (flattened, preserves order)
    context_messages = messages[-2*limit:]
    formatted = []
    for m in context_messages:
        formatted.append(f"{m['role'].capitalize()}: {m['content']}")
    return "\n".join(formatted)

def chat_ui(selected_mode):
    """Main chat interface with chat history and follow-up context awareness."""

    st.subheader(f"💬 StudyBuddy Chat — Mode: {selected_mode}")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input box
    prompt = st.chat_input(f"Type your message for {selected_mode} mode…")
    if prompt:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare previous context for better follow-up answers
        previous_context = get_previous_messages_summary(st.session_state.messages[:-1], limit=3)
        assistant_response = ""
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            try:
                with st.spinner("💡 Study Buddy is thinking…"):
                    start_time = time.time()
                    if selected_mode == "Explainer":
                        assistant_response = explain_concept(prompt, previous_context)
                    elif selected_mode == "Summarizer":
                        assistant_response = summarize_text(prompt, previous_context)
                    elif selected_mode == "Quizzer":
                        assistant_response = generate_quiz(prompt, previous_context)
                    else:
                        assistant_response = "⚠️ Unknown mode selected."
                    elapsed = time.time() - start_time
                    if elapsed > 8:
                        assistant_response += (
                            "\n\n⏳ *Sorry, this response took longer than usual. "
                            "If delays happen often, there may be server/API issues.*"
                        )
            except Exception as e:
                assistant_response = (
                    "❌ Sorry, there was an error processing your request. "
                    "Please try again in a few seconds.\n\n"
                    f"Error: {str(e)}"
                )
            response_placeholder.markdown(assistant_response)

            # Copy button feature - displays response in copyable code block
            st.code(assistant_response, language="markdown")

            # Feedback buttons
            st.markdown("**Was this response helpful?**")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("👍 Helpful", key=f"fb_yes_{len(st.session_state.messages)}"):
                    st.success("Thank you for your feedback!")
            with col2:
                if st.button("👎 Not Helpful", key=f"fb_no_{len(st.session_state.messages)}"):
                    st.info(
                        "We appreciate your input! Please let us know how we can improve."
                    )

        st.session_state.messages.append({"role": "assistant", "content": assistant_response})