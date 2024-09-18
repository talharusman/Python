import re

def extract_dates(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b|\b(?:[A-Z][a-z]{2}) \d{1,2}, \d{4}\b'
    dates = re.findall(pattern,text)
    return  dates

text = """
This document contains various dates like 12/09/2023, 2023-09-12, and Sep 12, 2023.
Other dates could be like 31/08/2021, 2020-12-25, or Dec 25, 2020.
"""
dates = extract_dates(text)

print("Extracted of dates: ")
for dates in dates:
    print(dates)