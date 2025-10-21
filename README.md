JobTriggerNotification
JobTriggerNotification automatically scrapes new job postings from Schneider Electric Careers and sends an email notification when jobs are posted on the current day.

Features
Web Scraping: Fetches job postings from Schneider Electric's career portal.

Email Notifications: Sends alerts for jobs posted today to a specified recipient.

Configurable: Easily update the sender, recipient, and email credentials.

Usage
Clone this repository:

bash
git clone https://github.com/Yashsd1311/JobTriggerNotification.git
Configure email credentials:

Open main.py

Update the following placeholders:

python
sender_email = "your email id"
app_password = "app password using gcp"
recipient_email = "recipient email id"
Install Dependencies:

bash
pip install requests beautifulsoup4
Run the script:

bash
python main.py
How It Works
The script scrapes Schneider Electric job board for jobs posted today.

For each new posting, it sends an email with job title, link, and posted date using Gmail SMTP.

Example Email
text
Subject: New Job: Data Analyst

New job posting!

Data Analyst
https://careers.se.com/jobs/123456
Posted: October 21, 2025
Customization
Target job URL: Change the Job_Url variable if you wish to target a different country or criteria.

Notification logic: Modify the date comparison logic to customize which jobs trigger alerts.
