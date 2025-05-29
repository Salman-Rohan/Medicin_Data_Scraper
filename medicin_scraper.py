import requests
from bs4 import BeautifulSoup
import csv
import re

def fix_spacing(text):
    # কিছু বেসিক রেগুলার এক্সপ্রেশন দিয়ে স্পেসিং ঠিক করা
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # CamelCase এর মাঝে স্পেস
    text = re.sub(r'([a-z])([0-9])', r'\1 \2', text)  # অক্ষর ও নম্বরের মাঝে স্পেস
    text = re.sub(r'([0-9])([a-z])', r'\1 \2', text)  # নম্বর ও অক্ষরের মাঝে স্পেস
    # অতিরিক্ত স্পেসগুলো একত্রে করার জন্য
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

url = "https://medlineplus.gov/diabetes.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'  # Encoding ঠিক করে দিচ্ছি

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No Title Found"

    paragraphs = soup.find_all("p")
    para_texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]

    with open("medlineplus_diabetes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Page Title", "Paragraph"])

        for para in para_texts:
            para = fix_spacing(para)
            writer.writerow([title, para])

    print(f"Data scraped and saved to medlineplus_diabetes.csv successfully!")

else:
    print(f"Failed to retrieve page, status code: {response.status_code}")

