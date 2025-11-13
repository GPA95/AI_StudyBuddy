from utils.gemini_helper import generate_response

def explain_concept(concept: str, previous_context: str = "") -> str:
    """
    Explain a concept in simple terms, considering previous context for follow-up questions.
    """
    prompt = f"""
You are Study Buddy, an AI-powered academic explainer.
[Recent chat for context:]
{previous_context}

[Current topic/question:]
{concept}

Instructions:
- If this is a topic (e.g., "Heap Sort", "Normalization in DBMS"):
    - Start with a simple definition or analogy/real-life example.
    - Follow with a step-by-step breakdown or main characteristics in bullet points.
    - Add common mistakes or misconceptions (if any).
    - End with 2-3 quick 'Key Takeaways' for revision.
- If the input sounds like an instruction ("make a quiz", "summarize this"):
    - Gently respond: "It looks like you might want to use the Quizzer or Summarizer mode instead."
- Use information from the previous chat for follow-up or clarifying answers.
- Keep language concise, avoid jargon unless needed, and always favor clarity.
- Use Markdown formatting for structure.
"""
    return generate_response(prompt.strip())
