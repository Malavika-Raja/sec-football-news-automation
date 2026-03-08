# 🏈 Weekly SEC Football Summary Automation

## Overview

This project is an automated pipeline that collects the latest SEC football news, extracts article content, generates a weekly summary using the OpenAI API, and sends the digest via email.

The entire workflow runs automatically every week using GitHub Actions.

---

## Pipeline Architecture

News API → Article Extraction → AI Summary → Email Delivery
↓
GitHub Actions (Scheduler)

---

## Project Structure

| File                           | Purpose                              |
| ------------------------------ | ------------------------------------ |
| `main.py`                      | Orchestrates the entire workflow     |
| `fetch_news.py`                | Retrieves SEC football articles      |
| `generate_summary.py`          | Generates summaries using OpenAI API |
| `send_email.py`                | Sends the formatted email report     |
| `config.py`                    | Loads environment variables          |
| `requirements.txt`             | Python dependencies                  |
| `.github/workflows/weekly.yml` | Scheduled GitHub Actions workflow    |

---

## Automation

The workflow is defined in:

`.github/workflows/weekly.yml`

The pipeline runs **every Monday at 13:00 UTC** using cron scheduling:

```
0 13 * * 1
```

GitHub Actions performs the following steps:

1. Launches an Ubuntu runner
2. Checks out the repository
3. Installs Python 3.11
4. Installs project dependencies
5. Injects environment secrets
6. Executes the automation pipeline (`main.py`)

---

## Environment Variables

The project uses **GitHub Actions Secrets** for secure configuration.

Required secrets:

* `OPENAI_API_KEY`
* `SERPER_API_KEY`
* `EMAIL_ADDRESS`
* `EMAIL_PASSWORD`
* `RECIPIENT_EMAIL`

---

## Tech Stack

* Python 3.11
* OpenAI API
* Serper News API
* SMTP (Email delivery)
* GitHub Actions (Workflow automation)

---

## Key Engineering Concepts

* API integration
* JSON data processing
* Time-based filtering
* Automated reporting
* Scheduled workflow automation
* Secure configuration using GitHub Secrets

---

## Learning Context

This project demonstrates how to build a reliable end-to-end automation pipeline that integrates APIs, processes data, and runs on a scheduled cloud workflow without requiring a local machine.
