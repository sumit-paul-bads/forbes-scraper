# Forbes Billionaires Scraper & Analysis

## 📌 Overview
This project extracts billionaire data from Forbes using Scrapy by leveraging internal API endpoints instead of traditional HTML scraping. The extracted dataset is then analyzed using Excel to generate insights through pivot tables and visualizations.

---

## 🚀 Key Features
- API-based data extraction (no JavaScript scraping)
- Pagination using `start` and `limit`
- Extracts 400+ billionaire records
- Data cleaning and transformation
- Excel-based analysis with pivot tables and charts

---

## 🛠 Tech Stack
- Python
- Scrapy
- Excel (Pivot Tables, Charts)

---

## ⚙️ How It Works
1. Inspected Forbes website using browser DevTools
2. Identified hidden JSON API from Network tab
3. Reverse-engineered pagination logic
4. Built Scrapy spider to extract structured data
5. Exported dataset to CSV
6. Performed analysis using Excel

---

## 📂 Dataset Sample

![Dataset](images/data_sample.png)

---

## 📊 Data Analysis & Visualizations

### 🏭 Industry-wise Distribution
![Industry Pivot](images/industry.png)

**Insights:**
- Finance & Investments has the highest number of billionaires
- Technology dominates total net worth despite fewer individuals
- Fashion & Retail is also a major contributor

---

### 👥 Age Distribution of Billionaires
![Age Distribution](images/age.png)

**Insights:**
- Majority of billionaires fall in the **51–86 age range**
- Very few are below 50 or above 87
- Wealth accumulation typically peaks in later stages of life

---

### 🌍 Country-wise Number of Billionaires
![Country Count](images/country_count.png)

**Insights:**
- United States dominates with a massive lead
- China is the second-largest contributor
- India and European countries follow

---

### 💰 Country-wise Total Net Worth
![Country Net Worth](images/country_worth.png)

**Insights:**
- United States leads significantly in total wealth
- Other countries contribute comparatively smaller shares
- Wealth distribution is highly concentrated

---

### 🏆 Top Billionaires by Net Worth
![Top Billionaires](images/top_people.png)

**Insights:**
- Elon Musk leads by a significant margin
- Tech industry dominates the top ranks
- Wealth is heavily concentrated among top individuals

---

## 📁 Output
- `bills.csv` → Contains structured billionaire dataset

---

## 🎯 Key Learnings
- Learned how to extract data using hidden APIs instead of HTML scraping
- Understood how modern websites load dynamic data
- Built an end-to-end pipeline from data extraction to analysis
- Gained hands-on experience with real-world datasets

---

## 🔗 Future Improvements
- Build interactive dashboard using Power BI / Tableau
- Automate periodic data updates
- Perform deeper statistical analysis

---

## 💬 Conclusion
This project demonstrates a complete data workflow:
➡️ Data Extraction → Processing → Analysis → Insights

---
