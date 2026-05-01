import os
import random
import time
from datetime import datetime
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

TOPICS = [
    "a Python tip for beginners",
    "an interesting fact about space",
    "a short motivational thought about consistency",
    "a fun fact about world history",
    "a beginner explanation of a programming concept",
    "a creative writing prompt",
    "a useful productivity habit",
    "a Linux command worth knowing",
    "a life lesson in 3 sentences",
    "a curious fact about mathematics",
    "a tip about healthy habits",
    "something fascinating about the ocean",
    "a quick explanation of how the internet works",
    "a fact about a famous scientist",
    "a tip for better sleep",
]

def call_groq(topic):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # fastest free model, 14,400 req/day limit
        messages=[
            {
                "role": "user",
                "content": (
                    f"Write a unique, creative 3-5 sentence piece about: {topic}. "
                    "Be engaging and vary your style each time. "
                    "Do not repeat yourself."
                )
            }
        ],
        max_tokens=200,
        temperature=1.0,
    )
    return response.choices[0].message.content.strip()

def make_commit(index, total):
    topic = random.choice(TOPICS)
    content = call_groq(topic)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = datetime.now().strftime("%Y-%m-%d")

    filename = f"content/{date_str}_entry_{index:03d}.md"
    with open(filename, "w") as f:
        f.write(f"# Daily Entry {index} of {total}\n\n")
        f.write(f"**Topic:** {topic}\n\n")
        f.write(f"**Generated at:** {timestamp}\n\n")
        f.write(f"{content}\n")

    os.system(f'git add "{filename}"')
    result = os.system(f'git commit -m "daily({index}/{total}): {topic[:48]}"')
    if result == 0:
        print(f"  ✓ Commit {index}/{total} — {topic[:40]}")
    else:
        print(f"  ✗ Commit {index}/{total} FAILED")

def main():
    total_commits = random.randint(40, 50)
    print(f"Target: {total_commits} commits")

    for i in range(1, total_commits + 1):
        try:
            make_commit(i, total_commits)
        except Exception as e:
            print(f"  ✗ Error on commit {i}: {e}")
        if i < total_commits:
            time.sleep(random.randint(3, 8))

    print(f"\nAll done — {total_commits} commits made.")

if __name__ == "__main__":
    main()
