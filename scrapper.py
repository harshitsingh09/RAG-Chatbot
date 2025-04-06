import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.angelone.in"
SECTIONS = [
    "/calculators/",
    "/mutual-funds/",
    "/mutual-funds/amc/"
]
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_section_links(section_url):
    print(f"Fetching section page: {section_url}")
    response = requests.get(section_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)
    
    article_links = set()
    for link in links:
        href = link.get("href")
        if href.startswith("/") and href.count("/") > 2:  # Heuristic to identify article links
            full_url = BASE_URL + href
            article_links.add(full_url)
    return list(article_links)

def extract_article_text(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code != 200:
            print(f"Failed to fetch {url} - Status Code: {res.status_code}")
            return ""
        soup = BeautifulSoup(res.text, "html.parser")

        # Adjust the selector based on actual article structure
        article = soup.find("article") or soup.find("div", class_="container") or soup
        text = article.get_text(separator="\n", strip=True)
        return text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def scrape_all_articles():
    all_article_links = set()
    for section in SECTIONS:
        section_url = BASE_URL + section
        section_links = get_section_links(section_url)
        all_article_links.update(section_links)
        time.sleep(1)  # Be respectful to the server

    print(f"Total articles found: {len(all_article_links)}")

    with open("angelone_articles.txt", "w", encoding="utf-8") as f:
        for idx, url in enumerate(all_article_links):
            print(f"[{idx+1}/{len(all_article_links)}] Scraping: {url}")
            article_text = extract_article_text(url)
            if article_text:
                f.write(f"URL: {url}\n")
                f.write(article_text + "\n\n" + "="*80 + "\n\n")
            time.sleep(1)  # Be respectful to the server

scrape_all_articles()
