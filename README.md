# 📘 **Study Buddy — AI-Powered Study Assistant**

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Gemini API](https://img.shields.io/badge/Backend-Gemini%202.5%20Flash-blue?logo=google)
![Python](https://img.shields.io/badge/Language-Python-yellow?logo=python)
![IBM SkillsBuild](https://img.shields.io/badge/AICTE%20x%20IBM-SkillsBuild%20Internship-orange?logo=ibm)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![Version](https://img.shields.io/badge/version-1.1.0-purple)

---

[![YouTube Demo](https://img.shields.io/badge/Watch-Demo%20Video-red?logo=youtube)](https://youtu.be/Yd0xMocB-V0)
[![Live App](https://img.shields.io/badge/Try%20it%20Now-Study%20Buddy-success?logo=streamlit)](https://sgpai-study-buddy.streamlit.app/)
[![HelpDoc](https://img.shields.io/badge/User%20Help-How%20to%20Use-blue?logo=google-drive)](https://drive.google.com/file/d/14NEdW6L4WC_hiqlhNBEElzJnfN60EZDa/view?usp=sharing)

---

## 🧠 **Project Overview**

Students often struggle to grasp difficult topics or summarize lengthy notes.  
**Study Buddy** is an AI-powered web app that acts as a **personal academic assistant**, capable of:

- 🧩 Explaining complex concepts in simple terms  
- 📄 Summarizing notes or uploaded PDFs  
- ❓ Generating quizzes, solving exam questions, and evaluating answers

Combines **Streamlit** for UI and **Gemini 2.5 Flash API** for fast, intelligent AI responses — all in a clean chat-based interface.

![Study Buddy Mobile Demo](https://github.com/user-attachments/assets/593f0b16-ebc5-4e93-b1f2-e2878c0c28a9)

---

## ⚙️ **System Design**

### 🏗️ **Architecture**
A lightweight **Streamlit frontend** interacts with **Google Gemini 2.5 Flash** backend via secure API calls.  
All secrets managed safely via `.env` and `st.secrets`.

### 🧩 **Core Features**

| Mode        | Function                                                           | Example                       |
|-------------|--------------------------------------------------------------------|-------------------------------|
| 🧠 **Explainer**      | Simplifies academic concepts                                   | “Explain Deadlock in OS”      |
| 📄 **Summarizer**     | Condenses notes or PDFs                                       | Upload 20-page PDF → summary  |
| 🧩 **Quizzer**        | Quiz generator, solver, evaluator (multi-mode workflow)       | MCQs, solve/evaluate Q&As     |

Other Features:
- 📂 PDF upload (PyPDF2 extraction)
- 💬 Real-time chat interface
- 🔄 New chat/reset option
- ☁️ Deployed on Streamlit Cloud

---

## 🧙‍♂️ **Quizzer Mode — Three Powerful Sub-modes**

1. **📝 Generate Questions**  
   Enter a topic/chapter/passage. Get a variety of questions (MCQ, T/F, fill-in, descriptive) — answers listed together as an answer key for self-testing.
2. **📖 Solve Questions**  
   Paste your exam questions (optionally add word limits or marks). Get concise, exam-ready answers formatted per input.
3. **✅ Evaluate Answers**  
   Submit questions and your answers (with '---' separator, or sequential prompts). Get detailed feedback, correction, and scoring.

---

## 🧱 **Project Structure**

```
StudyBuddy/
├── main.py
├── requirements.txt
├── assets/
│ └── PROBLEM STATEMENTS.pdf
├── components/
│ ├── chat_ui.py
│ ├── pdf_handler.py
│ └── sidebar.py
├── core/
│ ├── ai_utils.py
│ ├── explainer.py
│ ├── pdf_handler.py
│ ├── quizzer.py
│ └── summarizer.py
└── utils/
└── gemini_helper.py
```

---

## 🪜 **Workflow**
![StudyBuddy Workflow](https://github.com/user-attachments/assets/2cdac27e-2ae1-4dcf-b339-3a63efcebbb3)
![StudyBuddy System Architecture](https://github.com/user-attachments/assets/ae8f9a61-c84b-4ebf-9081-f139b98cf441)
©️🖼️ Diagram Credits: [https://gitdiagram.com/](https://gitdiagram.com/)

---

## 📚 In-Repo User Guide (Quick Start)

You can keep the PDF as the detailed reference and mirror a concise, in-README guide here.

### 1️⃣ Getting Started

- Open the deployed app: `https://sgpai-study-buddy.streamlit.app/`
- Select a mode from the sidebar: **Explainer**, **Summarizer**, or **Quizzer**
- Provide input (topic, notes, PDF, or questions) in the main chat area

### 2️⃣ Mode Usage

- **Explainer**:  
  Type your concept or question (e.g., “Explain paging in OS for exams”).  
  Study Buddy returns a simple, exam-oriented explanation.

- **Summarizer**:  
  Upload a PDF or paste notes.  
  Choose the summary style (concise / detailed / bullet points) if enabled and generate a summary.

- **Quizzer**:  
  - Use “Generate Questions” for practice questions with an answer key.  
  - Use “Solve Questions” to get answers to your questions.  
  - Use “Evaluate Answers” to paste both question and your answer to receive feedback and scoring.

### 3️⃣ Tips for Best Results

- Mention exam context (e.g., “for B.Tech 3rd sem OS viva”) for sharper responses.  
- Use follow-up prompts in the same chat to refine or extend answers.  
- Reset the chat using the “New Chat” / reset option before switching topics heavily.

For full details, screenshots, and troubleshooting, refer to the PDF: [![HelpDoc](https://img.shields.io/badge/User%20Help-How%20to%20Use-blue?logo=google-drive)](https://drive.google.com/file/d/14NEdW6L4WC_hiqlhNBEElzJnfN60EZDa/view?usp=sharing)

---

## 💡 **Tech Stack**

| Category            | Technologies                             |
|---------------------|------------------------------------------|
| **Frontend**        | Streamlit                                |
| **Backend / AI**    | Google Gemini 2.5 Flash API              |
| **Language**        | Python                                   |
| **Libraries**       | PyPDF2, google-generativeai, streamlit, dotenv |
| **Deployment**      | Streamlit Community Cloud                |
| **Security**        | `.env` + `st.secrets` key handling       |

---

## 🧾 **Results**

- 🎯 Simple, modern, and interactive chat-based UI  
- 📑 Smart summarization, quiz generation, and answer evaluation  
- ⚡ Fast, context-aware AI with Gemini 2.5 Flash  
- 🧩 Smooth multi-mode workflow for study and revision

---

## 🚀 **Future Scope**

- 🗣️ Speech-to-text / text-to-speech interaction  
- 🌐 Multi-language explanations  
- 🧠 Flashcard & spaced-repetition support  
- 👤 Memory-based user personalization  
- ☁️ Drive/Notion integration for notes & sessions  

---

> 🧩 *“Integrating AI with Education — Making Learning Simpler, Smarter, and Accessible for All.”*

---

## 📜 Usage & Attribution

- You are welcome to **fork** this repository to learn from it or build your own version of Study Buddy.  
- If you deploy this project publicly or create a derivative version:
  - Keep the existing license file.  
  - Credit **“Study Buddy by Ammaar Ahmad Khan (GPA95)”**.  
  - Include a link back to the original repo:
    - https://github.com/GPA95/AI_StudyBuddy

For contributions, please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on forking, branching, and opening pull requests.

---

## 👨‍💻 Author

**Ammaar Ahmad Khan**  
- GitHub: [@GPA95](https://github.com/GPA95)

🌟 If you find this repository useful, please give it a star! 🌟

---