Below is your **complete, badge-styled, professional GitHub README.md**, fully tailored to YOUR code — including features, setup, data pipeline, pagination scraping, cleaning pipeline, EDA, charts, outputs, and project structure.

It is formatted, clean, and ready to paste into GitHub.

---

# **📘 Jumia Smartphone Price Scraper & Data Analysis**

A complete **web scraping + data cleaning + exploratory data analysis (EDA)** pipeline built in **Python + BeautifulSoup + Pandas + Matplotlib/Seaborn**.
This project scrapes smartphone product data from **Jumia Kenya**, cleans and preprocesses it, and performs full statistical and visual analysis.

---

<p align="center">

🎯 **End-to-end Automated Data Pipeline**
🔎 **Web Scraping** • 🧼 **Data Cleaning** • 📊 **EDA** • 🔄 **Pagination**

</p>

---

## **🏷️ Badges**

<p align="left">
<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/BeautifulSoup-4-6A5ACD?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Requests-Library-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Matplotlib-Charts-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Seaborn-Visualization-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</p>

---

# **📌 Project Overview**

This project automatically:

- Scrapes all smartphone product listings from **Jumia Kenya**
- Supports **multi-page pagination scraping**
- Extracts **name, price, old price, product link**
- Cleans, structures, and preprocesses the dataset
- Handles missing data using smart rules
- Computes discount percentages and variation metrics
- Generates visualizations and statistical summaries
- Produces **cleaned CSV outputs** + **top discount report**

---

# **🕸️ Web Scraping Features**

### **Smart Pagination Extraction**

Supports multiple pagination styles:

```python
# pagination type 1       ->  <a class="pg next">
# pagination type 2       ->  aria-label="Next Page"
```

###  **Product Fields Scraped**

* Product name
* Current price
* Old price
* Full product URL

###  **Crawl Safety**

* Request headers
* 3-second delay between pages
* Jumia-safe user-agent

---

# **🔧 Technologies Used**

| Component      | Tools                           |
| -------------- | ------------------------------- |
| Web Scraping   | BeautifulSoup4, Requests        |
| Data Cleaning  | Pandas                          |
| Visualizations | Matplotlib, Seaborn             |
| Environment    | Google Colab / Jupyter Notebook |

---

# **📁 Project Structure**

```
📦 Jumia Price Analysis
│
├── jumia_products.csv                # raw scraped data
├── jumia_products_cleaned.csv        # cleaned dataset
├── jumia_top_discounts.csv           # top discount report
│
├── WEB SCRAPING.ipynb                # full notebook
└── README.md
```

---

# **🚀 How to Run**

### **1️⃣ Install Dependencies**

```bash
pip install beautifulsoup4 requests pandas matplotlib seaborn
```

### **2️⃣ Run the Notebook or Script**

```python
all_products = scrape_jumia()
```

### **3️⃣ View output CSVs**

* `jumia_products.csv`
* `jumia_products_cleaned.csv`
* `jumia_top_discounts.csv`

---

# **🔍 Detailed Process Breakdown**

---

## **1️⃣ Web Scraping**

### **Fetch HTML**

```python
response = requests.get(url, headers=headers)
```

### **Parse Product Cards**

```python
items = soup.select("article.prd")
```

### **Pagination Logic**

```python
next_btn = soup.select_one("a.pg.next")                 # Pagination type 1
next_btn2 = soup.find("a", {"aria-label": "Next Page"}) # Pagination type 2
```

---

## **2️⃣ Data Cleaning Pipeline**

### Remove duplicate products

### Trim product names to 4 key words

### Clean price fields from `"KSh 20,000"` → `20000`

### Handle missing values dynamically:

* **<5% missing** → drop rows
* **5–30% missing** → impute
* **>30% missing** → flagged for manual handling

### Compute discount percentage

```python
df['discount_percent'] = ((old_price - price) / old_price) * 100
```

---

## **3️⃣ Exploratory Data Analysis (EDA)**

Includes:

📌 Summary statistics
📌 Dataset shape
📌 Missing values table
📌 Histograms (price, old price)
📌 Boxplots
📌 Scatter plot (old price vs current price)
📌 Correlation matrix
📌 Price variation analysis
📌 Top & bottom 20 variation reports

---

## **📊 Visuals Generated**

* Histogram of prices
* Histogram of old prices
* Boxplots
* Scatter plot
* Heatmap correlation matrix
* Bar charts (top/bottom discounts)

---

# **📈 Key Insights Generated**

* Average smartphone price
* Most expensive models
* Cheapest models
* Real discount percentages
* True vs fake sale prices
* Correlation between old & new price
* Unique product count

---

# **📦 Output Files**

| File                           | Description                     |
| ------------------------------ | ------------------------------- |
| **jumia_products.csv**         | Raw scraped data                |
| **jumia_products_cleaned.csv** | Clean, ready-to-analyze dataset |
| **jumia_top_discounts.csv**    | Top 10 discounted smartphones   |

---

# **🛡️ Ethical Notes**

This project respects:

✔ Public product information
✔ Jumia's server load (via timed requests)
✔ Identified user-agent with contact email

No personal data is collected.

---

# **📜 License**

This project is released under the **MIT License**.
You may modify, reuse, or extend it freely.

---

# **🙌 Author**

**Isaack Mutembei Sani**
Data Scientist & Statistician
Passionate about automation, analytics, and clean data pipelines.



