#!/usr/bin/python3
import re

# Simulated API string response with realistic data
sample_data = """
Contact: john.doe@example.com, support@company.co.uk
Backup site: https://subdomain.example.org/page and https://www.example.com
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234-5678-9012-3456, 1234 5678 9012 3456
Meeting times: 14:30, 2:30 PM, 09:00 am
HTML Sample: <p>Paragraph</p> <div class="example">Hello</div> <img src="pic.jpg" alt="Image">
Hashtags: #coding #ThisIsAHashtag #Regex101
Prices: $19.99, $1,234.56, $100
"""

# 1. Email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, sample_data)

# 2. URLs
url_pattern = r'https?://[^\s<>"]+'
urls = re.findall(url_pattern, sample_data)

# 3. Phone numbers
phone_pattern = r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
phones = re.findall(phone_pattern, sample_data)

# 4. Credit card numbers
credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
credit_cards = re.findall(credit_card_pattern, sample_data)

# 5. Time (12-hour and 24-hour format)
time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
times = re.findall(time_pattern, sample_data)

# 6. HTML tags
html_tag_pattern = r'<[^>]+>'
html_tags = re.findall(html_tag_pattern, sample_data)

# 7. Hashtags 
hashtag_pattern = r'#\w+'
hashtags = re.findall(hashtag_pattern, sample_data)

# 8. Currency amounts 
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
currency_amounts = re.findall(currency_pattern, sample_data)

# -------------------------------
# Output Section
# -------------------------------

print(" Emails Found:", emails)
print(" URLs Found:", urls)
print(" Phone Numbers Found:", phones)
print(" Credit Card Numbers Found:", credit_cards)
print(" Times Found:", times)
print(" HTML Tags Found:", html_tags)
print(" Hashtags Found:", hashtags)
print("Currency Amounts Found:", currency_amounts)

