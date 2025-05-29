# MedlinePlus Diabetes Data Scraper

এই প্রোজেক্টটি `BeautifulSoup` ও `requests` লাইব্রেরি ব্যবহার করে MedlinePlus-এর [Diabetes Information Page](https://medlineplus.gov/diabetes.html) থেকে ডাটা স্ক্র্যাপ করে একটি CSV ফাইলে সংরক্ষণ করে।

---

## Features

- ওয়েবপেজ থেকে টাইটেল এবং প্যারাগ্রাফ গুলো সংগ্রহ করে  
- টেক্সটের মাঝে ভুল স্পেসিং ও CamelCase ইস্যু কিছুটা ঠিক করে  
- UTF-8 এনকোডিং ব্যবহার করে CSV ফাইল তৈরি করে  
- Excel বা অন্য টুলসে সহজে ওপেন করার জন্য প্রস্তুত

---

## Requirements

- Python 3.x  
- `requests` লাইব্রেরি  
- `beautifulsoup4` লাইব্রেরি

---

## Installation

```bash
pip install requests beautifulsoup4

Scraped By
Salman Rohan

