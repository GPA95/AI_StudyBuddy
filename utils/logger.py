import csv
import os
from datetime import datetime
import uuid
import streamlit as st

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "usage_log.csv")

def get_session_id():
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id

def log_usage(mode, sub_mode, had_pdf, prompt_text, response_text=""):
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        row = {
            "timestamp": datetime.utcnow().isoformat(),
            "session_id": get_session_id(),
            "mode": mode,
            "sub_mode": sub_mode or "",
            "had_pdf": int(bool(had_pdf)),
            "prompt_chars": len(prompt_text or ""),
            "response_chars": len(response_text or ""),
        }
        file_exists = os.path.isfile(LOG_FILE)
        with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)
    except Exception:
        pass  # Logging must never break the app
