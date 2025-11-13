from utils.gemini_helper import generate_response

def summarize_text(text: str, previous_context: str = "", user_focus: str = "", extra_instruction: str = "") -> str:
    """
    Summarize study materials, aligning output for exam preparation if requested.

    Notes:
    - Keeps backwards compatibility with existing callers that pass `previous_context` or `user_focus`.
    - `extra_instruction` (preferred) or `user_focus` will be used to adapt the output.
    """
    # Short-text guard
    if not text or len(text.strip()) < 50:
        return "⚠️ This text is too short to summarize. Please provide longer content."

    # Prefer extra_instruction, fall back to user_focus (keeps compatibility)
    instruction = extra_instruction.strip() if extra_instruction else user_focus.strip()

    prompt = f"""
You are Study Buddy, an academic summary AI.

- If text is VERY short (<50 words), say: "This text is too short to summarize. Please provide longer content."
- Otherwise, create a compact, exam-ready summary in clear, bullet-point sections:
  - Core definitions
  - Most important points (bullets)
  - Key formulas or diagrams (if present)
  - Application scenarios or examples
  - Add 2-3 practice/follow-up questions based on the content

If the user gives extra instructions (below), adapt output accordingly (e.g., "focus on applications"):
{instruction}

Reference prior chat context if relevant:
{previous_context}

Content:
{text}
"""
    return generate_response(prompt.strip())
# ...existing code...