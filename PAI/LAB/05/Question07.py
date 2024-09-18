
import re
def extract_emails(text):

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails


text = "Hi there, you can contact me at alice.smith@domain.com, or feel free to reach out to me at alice123@yahoo.com or info@mywebsite.org."

emails = extract_emails(text)
print("Extracted email addresses:")
for email in emails:
    print(email)