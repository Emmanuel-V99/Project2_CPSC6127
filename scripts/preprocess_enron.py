
import csv
import re
import sys

csv.field_size_limit(10**7)  # 10 MB per field

# Change these to match your actual column names
EMAIL_BODY_COL = "body"
EMAIL_SUBJECT_COL = "subject"  # Optional
INPUT_CSV_PATH = "../data/enron_emails.csv"
OUTPUT_TXT_PATH = "../data/cleaned_emails.txt"

# Optional: remove HTML tags and email headers
def clean_text(text):
    # Remove HTML
    text = re.sub(r'<[^>]+>', '', text)
    # Remove common email reply headers
    text = re.sub(r'From:.*\n|Sent:.*\n|To:.*\n|Subject:.*\n', '', text, flags=re.IGNORECASE)
    return text.strip()

with open(INPUT_CSV_PATH, 'r', encoding='utf-8', errors='ignore') as infile, \
     open(OUTPUT_TXT_PATH, 'w', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)

    for row in reader:
        # Combine subject + body (optional)
        body = row.get(EMAIL_BODY_COL, "")
        subject = row.get(EMAIL_SUBJECT_COL, "")
        combined_text = f"{subject} {body}".strip()

        if combined_text:
            cleaned = clean_text(combined_text)
            outfile.write(cleaned.replace('\n', ' ') + "\n")  # One email per line
