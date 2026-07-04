"""
Generates one random, non-repeating study note (Data Science / Python / ML / DL /
Agentic AI / Gen AI / SQL / AI-ML) using the Groq API, saves it under notes/,
and records the subtopic in notes/history.json so it's never repeated.
"""

import os
import re
import sys
import json
import random
import datetime
import requests

TOPICS = [
    "Data Science",
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Agentic AI",
    "Generative AI",
    "SQL",
    "AI/ML Concepts",
]

NOTES_DIR = "notes"
HISTORY_FILE = os.path.join(NOTES_DIR, "history.json")

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

MAX_RETRIES = 3


def load_history() -> dict:
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {"used_subtopics": []}


def save_history(history: dict) -> None:
    os.makedirs(NOTES_DIR, exist_ok=True)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def build_prompt(topic: str, used_subtopics: list) -> str:
    avoid_list = "\n".join(f"- {s}" for s in used_subtopics) or "None yet"
    return f"""You are writing a short daily study note for a learner.

Topic category: {topic}

Subtopics already covered (do NOT reuse or closely repeat any of these):
{avoid_list}

Instructions:
1. Pick ONE specific, narrow subtopic inside "{topic}" not covered above.
2. Write a concise Markdown note (150-300 words):
   - H1 title = the subtopic name
   - Short explanation of the concept
   - Why/where it's used in practice
   - A short code snippet or example if relevant
3. End with exactly one line in this exact format (nothing after it):
SUBTOPIC: <3-8 word name of the subtopic>

No preamble, no extra commentary outside the note."""


def call_groq(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.9,
        "max_tokens": 700,
    }
    resp = requests.post(GROQ_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def extract_subtopic(content: str):
    match = re.search(r"SUBTOPIC:\s*(.+)", content)
    subtopic = match.group(1).strip() if match else "Untitled Note"
    body = re.sub(r"SUBTOPIC:\s*.+", "", content).strip()
    return body, subtopic


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "note"


def main():
    session = sys.argv[1] if len(sys.argv) > 1 else "session"

    history = load_history()
    used_subtopics = history.get("used_subtopics", [])

    topic = random.choice(TOPICS)
    prompt = build_prompt(topic, used_subtopics)

    body, subtopic = "", ""
    for _ in range(MAX_RETRIES):
        content = call_groq(prompt)
        body, subtopic = extract_subtopic(content)
        if subtopic.lower() not in {s.lower() for s in used_subtopics}:
            break
    else:
        # Fallback: make it unique by tagging with a timestamp
        subtopic = f"{subtopic} - {datetime.datetime.utcnow().strftime('%H%M')}"

    now = datetime.datetime.utcnow()
    date_str = now.strftime("%Y-%m-%d")
    topic_slug = slugify(topic)
    subtopic_slug = slugify(subtopic)

    filename = f"{NOTES_DIR}/{topic_slug}/{date_str}-{session}-{subtopic_slug}.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(f"# {subtopic}\n\n")
        f.write(f"**Category:** {topic}  \n**Date:** {date_str} ({session})\n\n---\n\n")
        f.write(body + "\n")

    used_subtopics.append(subtopic)
    history["used_subtopics"] = used_subtopics
    save_history(history)

    github_env = os.environ.get("GITHUB_ENV")
    if github_env:
        with open(github_env, "a") as f:
            f.write(f"NOTE_TOPIC={topic}\n")
            f.write(f"NOTE_SUBTOPIC={subtopic}\n")
            f.write(f"NOTE_FILE={filename}\n")


if __name__ == "__main__":
    main()
