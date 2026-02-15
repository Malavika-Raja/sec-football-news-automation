# 🏈 Weekly SEC Football Summary Automation

## Overview

📌 Overview

This project:
- Collects SEC football news articles
- Extracts article content
- Generates a structured weekly summary using the OpenAI API
- Sends the summary via email
- Runs automatically every week using GitHub Actions

---

## Architecture

News API → Article Extraction → AI Summary → Email Delivery
                              ↓
                      GitHub Actions (Scheduled)

### Core Components

| File | Purpose |
|------|---------|
| `main.py` | Orchestrates the pipeline |
| `fetch_news.py` | Retrieves SEC-related articles |
| `generate_summary.py` | Calls OpenAI API for summary |
| `send_email.py` | Sends formatted email |
| `config.py` | Centralized environment variable loader |
| `requirements.txt` | Python dependencies |
| `.github/workflows/weekly.yml` | Automation workflow |

---

## 🔐 Environment Variables

The project uses repository secrets for security.

### Required Secrets

Store these as GitHub Actions Secrets:

- `OPENAI_API_KEY`
- `SERPER_API_KEY`
- `EMAIL_ADDRESS`
- `EMAIL_PASSWORD`
- `RECIPIENT_EMAIL`

## 🤖 Automation

The workflow is defined in:
`.github/workflows/weekly.yml`

### Schedule

Runs every monday at 13:: UTC using cron syntax:
`0 13 * * 1
`
The workflow:
1. Spins up Ubuntu runner
2. Checks out repository
3. Installs Python 3.11
4. Installs dependencies
5. Injects secrets
6. Executes main.py

- Making HTTP requests to a third-party API
- Parsing structured JSON data
- Time-window filtering using timestamps
- Formatting programmatic reports
- Automated email delivery
- Basic workflow pipeline design

This project focuses on building a reliable end-to-end script rather than advanced architecture.

---

## 🧠 Tech Stack

- Python 3.11
- OpenAI API
- Serper API
- SMTP
- GitHub Actions

---

## Learning Context

1. End-to-end automation design - Built a fully automated pipeline integrating APIs, data processing, and scheduled execution without relying on a local machine.
2. Secure configuration management - Implemented environment variable handling and github secrets to prevent credential exposure and enable safe CI/CD deployment.

