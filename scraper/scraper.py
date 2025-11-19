import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

# Custom user-agent as required by Jumia robots.txt
headers = {
    "User-Agent": "JumiaPriceResearchBot/1.0 (+mailto:your-email@example.com)"
}

BASE_URL = "https://www.jumia.co.ke"
CATEGORY_URL = "https://www.jumia.co.ke/smartphones/"   # Change to any category


# Request HTML
def get_page_html(url):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


# Extract product cards
def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("article.prd")

    products = []
    for item in items:
        name_tag = item.select_one("h3.name")
        name = name_tag.get_text(strip=True) if name_tag else None

        price_tag = item.select_one("div.prc")
        price = price_tag.get_text(strip=True) if price_tag else None

        old_price_tag = item.select_one("div.old")
        old_price = old_price_tag.get_text(strip=True) if old_price_tag else None

        link_tag = item.select_one("a.core")
        link = urljoin(BASE_URL, link_tag["href"]) if link_tag else None

        products.append({
            "name": name,
            "price": price,
            "old_price": old_price,
            "link": link
        })

    return products


# Find next page
def get_next_page(html):
    soup = BeautifulSoup(html, "html.parser")

    next_btn = soup.select_one("a.pg.next")
    if next_btn:
        return urljoin(BASE_URL, next_btn.get("href"))

    next_btn2 = soup.find("a", attrs={"aria-label": "Next Page"})
    if next_btn2:
        return urljoin(BASE_URL, next_btn2.get("href"))

    return None


# Main scraper
def scrape_jumia():
    url = CATEGORY_URL
    page_num = 1

    with open("jumia_products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "old_price", "link"])
        writer.writeheader()

        while url:
            print(f"Scraping Page {page_num}: {url}")
            html = get_page_html(url)

            products = parse_products(html)
            if not products:
                print("No products found — stopping.")
                break

            writer.writerows(products)
            print(f"Extracted {len(products)} products from page {page_num}")

            time.sleep(3)   # Respect crawling limits

            url = get_next_page(html)
            page_num += 1

    print("Scraping complete — saved to jumia_products.csv")


if __name__ == "__main__":
    scrape_jumia()
