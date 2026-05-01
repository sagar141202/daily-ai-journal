import os
import random
import time
import requests
from datetime import datetime

GROK_API_KEY = os.environ["GROK_API_KEY"]
TOPICS = [
    "a Python tip for beginners",
    "an interesting fact about space",
    "a short motivational thought",
    "a fun fact about history",
    "a beginner's explanation of a CS concept",
    "a creative writing prompt",
    "a productivity habit",
    "a Linux command worth knowing",
    "a life lesson in 3 sentences",
    "a math curiosity",
]

def call_grok(topic):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "grok-3-mini",
        "messages": [
            {
                "role": "user",
                "content": f"Write a short, unique, 3-5 sentence piece about: {topic}. Be creative and vary your style each time."
            }
        ],
        "max_tokens": 200,
        "temperature": 1.0,
    }
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def make_commit(index, total):
    topic = random.choice(TOPICS)
    content = call_grok(topic)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write unique file
    filename = f"content/{datetime.now().strftime('%Y-%m-%d')}_entry_{index:03d}.md"
    with open(filename, "w") as f:
        f.write(f"# Entry {index} of {total}\n\n")
        f.write(f"**Topic:** {topic}\n\n")
        f.write(f"**Generated at:** {timestamp}\n\n")
        f.write(f"{content}\n")
    
    # Stage and commit
    os.system(f'git add "{filename}"')
    os.system(f'git commit -m "daily({index}/{total}): {topic[:50]}"')
    print(f"  ✓ Commit {index}/{total} done")

def main():
    total_commits = random.randint(40, 50)
    print(f"Starting: {total_commits} commits scheduled")
    
    # Git config (needed inside Actions runner)
    os.system('git config user.email "bot@daily-journal.auto"')
    os.system('git config user.name "Daily Journal Bot"')
    
    for i in range(1, total_commits + 1):
        make_commit(i, total_commits)
        # Random pause 5-20 seconds between commits (looks natural)
        if i < total_commits:
            time.sleep(random.randint(5, 20))
    
    print(f"\nDone! {total_commits} commits made.")

if __name__ == "__main__":
    main()
