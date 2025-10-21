from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import os
import smtplib
from email.mime.text import MIMEText

Job_Url = "https://careers.se.com/jobs?sortBy=posted_date&descending=true&page=1&country=United%20States"
seen_jobs_file = "seen_jobs.json"

# --- EMAIL CONFIGURATION (change these) ---
sender_email = "yashsd99@gmail.com"
app_password = "vkgv zfur hpnc qwir"
recipient_email = "deshpande.ya@northeastern.edu"


# ------------- Email Notifier -------------
def send_email(job):
    msg = MIMEText(f"New job posting!\n\n{job['title']}\n{job['link']}\nPosted: {job['posted_date']}")
    msg['Subject'] = f"New Job: {job['title']}"
    msg['From'] = sender_email
    msg['To'] = recipient_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print(f"Notification sent for job: {job['title']}")

# ------------- Scraper & Notifier -------------
def fetch_and_notify_latest_jobs():
    response = requests.get(Job_Url)
    soup = BeautifulSoup(response.text, 'html.parser')
    today = datetime.today()
    for panel in soup.find_all('mat-expansion-panel'):
        job_link_tag = panel.find('a', class_="job-title-link")
        if not job_link_tag:
            continue
        job_title = job_link_tag.find('span', itemprop='title').text.strip()
        job_link = job_link_tag['href']
        if job_link.startswith('/'):
            job_link = 'https://careers.se.com' + job_link
        # Grab posted date, fallbacks in case of missing label
        posted_date_elem = panel.find('span', class_="label-value posted_date")
        posted_date = posted_date_elem.text.strip() if posted_date_elem else "Unknown"
        # Optional: compare posted_date with today (September 8, 2025), customize as needed
        # If posted_date is 'September 8, 2025' (today), notify
        if posted_date.lower().startswith(today.strftime("%B %d, %Y").lower()) or posted_date.lower().startswith(today.strftime("%m/%d/%Y").lower()):
            job = {'title': job_title, 'link': job_link, 'posted_date': posted_date}
            send_email(job)

if __name__ == "__main__":
    fetch_and_notify_latest_jobs()