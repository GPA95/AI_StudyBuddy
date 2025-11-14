from utils.gemini_helper import generate_response

def generate_questions(text: str, previous_context: str = "") -> str:
    """
    Generate a quiz. Show hints if helpful. Answers listed at end as an answer key.
    """
    prompt = f"""
You are Study Buddy, an academic quiz generator.

Context:
{previous_context}

Content/topic:
{text}

Instructions:
- Create a mix of questions: Multiple Choice (with options A-D, each on a separate line), True/False, Fill in the Blanks, Short Descriptive.
- List all questions in order. If useful, include a short hint with a question.
- Do NOT show the correct answer right after each question.
- Instead, after ALL questions, provide a numbered "Answer Key" listing each answer (e.g., "1. B", "2. True", "3. Photosynthesis", ...).
- Number every question and answer for clarity.
- Format so the student can attempt first, then check answers.
"""
    return generate_response(prompt.strip())

def solve_questions(user_questions: str, previous_context: str = "", word_limit: int = 100) -> str:
    """
    Solve exam-style questions, using smart default word range with visual cues when needed.
    """
    prompt = f"""
You are Study Buddy, a question-solving AI.

Questions:
{user_questions}

Recent context:
{previous_context}

Instructions:
- For each question, decide what type it is (very short, short, long) and adapt your answer length:
  • Very short answer (objective, 0.5–1 mark): 25–40 words or 1–2 sentences.
  • Short answer (2–3 marks): 90–130 words, mention any diagrams/visuals if relevant.
  • Long answer (4–5 marks): 160–220 words, stepwise breakdowns/mention any diagrams if relevant.
- If user gives a word limit or mark value, follow it.
- Number all answers; use Markdown formatting (bold for questions/answers, bullet points, headings for diagrams).
"""
    return generate_response(prompt.strip())

def evaluate_answers(questions: str, user_answers: str, previous_context: str = "") -> str:
    """
    Evaluate user's answers; feedback, scores, and tips.
    """
    prompt = f"""
You are Study Buddy, an answer evaluator.

Questions:
{questions}

User's Answers:
{user_answers}

Recent chat:
{previous_context}

Instructions:
- For each answer, indicate if it’s correct/incorrect.
- Give specific suggestions for improvement, point out missing facts/examples if relevant.
- Assign a score out of the maximum possible (e.g., 1 mark, 3 marks, etc.)—be detailed.
- Summarize overall strengths and improvement areas.
- Use numbered feedback, concise language.
"""
    return generate_response(prompt.strip())
