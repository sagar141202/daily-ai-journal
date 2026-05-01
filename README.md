# 📓 Daily AI Journal

An automated GitHub repository that generates and commits AI-written content every day at **6:00 AM IST** — completely hands-free.

Powered by **Groq API** (Llama 3.1 8B) + **GitHub Actions**.

---

## 🤖 How it works

Every morning at 6:00 AM IST, a GitHub Actions workflow automatically:

1. Spins up a runner and installs dependencies
2. Calls the Groq API to generate unique, creative content
3. Makes **40–50 individual commits** with varied topics
4. Pushes everything to this repository
5. Updates the GitHub contribution graph — zero manual effort

---

## 📁 Repository structure

daily-ai-journal/
├── .github/
│   └── workflows/
│       └── daily_commit.yml     # GitHub Actions automation
├── scripts/
│   └── auto_commit.py           # Python script that drives commits
├── content/
│   └── YYYY-MM-DD_entry_NNN.md  # Auto-generated daily entries
└── README.md

---

## 🛠️ Tech stack

| Tool | Purpose |
|---|---|
| GitHub Actions | Cron scheduler & workflow runner |
| Python 3.12 | Automation script |
| Groq API | AI content generation (Llama 3.1 8B) |
| `groq` SDK | Python client for Groq |

---

## ⚙️ Setup (for your own fork)

### 1. Get a free Groq API key
Sign up at [console.groq.com](https://console.groq.com) — no credit card required.

### 2. Create a GitHub Personal Access Token
Go to [github.com/settings/tokens](https://github.com/settings/tokens) → Generate new token (classic) → select `repo` scope.

### 3. Add repository secrets
Go to your repo → **Settings → Secrets and variables → Actions** and add:

| Secret name | Value |
|---|---|
| `GROQ_API_KEY` | Your Groq API key (`gsk_...`) |
| `PAT_TOKEN` | Your GitHub PAT (`ghp_...`) |

### 4. Update the git identity in the workflow
In `.github/workflows/daily_commit.yml`, replace:
```yaml
git config user.email "your@email.com"
git config user.name "yourusername"
```
with your own GitHub email and username.

### 5. Trigger manually to test
Go to **Actions → Daily AI Journal → Run workflow**.

---

## 📊 Content topics

The script randomly picks from topics including:

- Python tips for beginners
- Space and science facts
- Programming concept explanations
- Productivity and life habits
- History and mathematics curiosities
- Linux commands worth knowing
- Creative writing prompts

Each entry is unique, timestamped, and stored as a Markdown file under `/content`.

---

## ⏰ Schedule

Runs daily at `00:30 UTC` which is `06:00 AM IST (UTC+5:30)`.

To change the time, edit the cron expression in `.github/workflows/daily_commit.yml`:

```yaml
- cron: '30 0 * * *'   # minute hour * * *
```

---

## 📈 Contribution graph

Each daily run produces **40–50 commits** attributed to your GitHub account, keeping your contribution graph consistently green.

---

## 🔒 Security notes

- The Groq API key and PAT are stored as **GitHub encrypted secrets** — never hardcoded in any file
- The PAT uses minimum required scope (`repo` only)
- No sensitive data is written to the repository

---

## 📄 License

MIT — free to fork, modify, and use for your own automation.
