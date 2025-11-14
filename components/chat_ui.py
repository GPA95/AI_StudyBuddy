import streamlit as st
from core.explainer import explain_concept
from core.summarizer import summarize_text
from core.quizzer import (
    generate_questions,
    solve_questions,
    evaluate_answers
)
import time

def get_previous_messages_summary(messages, limit=3):
    context_messages = messages[-2*limit:]
    return "\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in context_messages)

def chat_ui(selected_mode, selected_sub_mode=None):
    """Main chat interface with mode and optional sub-mode for Quizzer."""
    
    # Build subheader dynamically
    if selected_sub_mode:
        st.subheader(f"💬 StudyBuddy Chat — {selected_mode} | {selected_sub_mode}")
    else:
        st.subheader(f"💬 StudyBuddy Chat — {selected_mode}")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input(f"Type your message…")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        previous_context = get_previous_messages_summary(st.session_state.messages[:-1], limit=3)
        assistant_response = ""
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            try:
                with st.spinner("💡 Study Buddy is thinking…"):
                    start_time = time.time()
                    if selected_mode == "💡 Explainer":
                        assistant_response = explain_concept(prompt, previous_context)
                    elif selected_mode == "📰 Summarizer":
                        assistant_response = summarize_text(prompt, previous_context)
                    elif selected_mode == "🧩 Quizzer":
                        if selected_sub_mode == "📝 Generate Questions":
                            st.info(
                                "Paste a subject/topic or relevant passage. "
                                "Questions will be listed first, answers as a separate numbered key at the end."
                            )
                            assistant_response = generate_questions(prompt, previous_context)
                        elif selected_sub_mode == "📖 Solve Questions":
                            st.info(
                                "Paste your exam questions here. If specifying marks/word range, include this in each question."
                            )
                            # No word limit input needed; backend smartly adapts using prompt instructions
                            assistant_response = solve_questions(prompt, previous_context)
                        elif selected_sub_mode == "✅ Evaluate Answers":
                            qs_ans = prompt.split("---")
                            assistant_response = evaluate_answers(qs_ans[0].strip(), qs_ans[1].strip(), previous_context)
                        else:
                            assistant_response = "⚠️ Unknown Quizzer sub-mode."
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
            st.code(assistant_response, language="markdown")

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
