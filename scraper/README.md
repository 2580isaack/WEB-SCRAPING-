# Jumia Product Scraper (Kenya)

This project scrapes product data such as name, price, old price, and product link
from Jumia Kenya category pages.

## Features
- Follows Jumia robots.txt rules
- Custom user-agent (required)
- Extracts product name, price, old price, URL
- Supports automatic pagination
- Outputs CSV file: `jumia_products.csv`

## Requirements
Install dependencies:

```
pip install -r requirements.txt
```

## Usage
Run the scraper:

```
python scraper.py
```

After running, the data will be saved in:

```
jumia_products.csv
```

## Warning
Scraping must follow Jumia robot rules:
- Correct user-agent
- Less than 200 requests/minute (this script pauses 3 seconds each page)
