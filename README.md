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

![1fs](https://github.com/user-attachments/assets/8e491506-6f94-4a20-b190-65b23a1612ea)


---

## 📊 Data Analysis & Visualizations

### 🏭 Industry-wise Distribution

![6fs](https://github.com/user-attachments/assets/2cde455d-a1ab-4855-9ebe-1e170afaf3f7)

**Insights:**
- Finance & Investments has the highest number of billionaires
- Technology dominates total net worth despite fewer individuals
- Fashion & Retail is also a major contributor

---

### 👥 Age Distribution of Billionaires

![5fs](https://github.com/user-attachments/assets/bbb26105-c96d-40b6-8524-7827800083d3)

**Insights:**

- Majority of billionaires fall in the **51–86 age range**
- Very few are below 50 or above 87
- Wealth accumulation typically peaks in later stages of life

---

### 🌍 Country-wise Number of Billionaires

![2fs](https://github.com/user-attachments/assets/3b5328f2-8923-420d-9cbe-aa48baf62bf4)

**Insights:**
- United States dominates with a massive lead
- China is the second-largest contributor
- India and European countries follow

---

### 💰 Country-wise Total Net Worth

![3fs](https://github.com/user-attachments/assets/28882f74-8000-4e52-bbde-024a161cabd3)


**Insights:**
- United States leads significantly in total wealth
- Other countries contribute comparatively smaller shares
- Wealth distribution is highly concentrated

---

### 🏆 Top Billionaires by Net Worth

![4fs](https://github.com/user-attachments/assets/682ca2ab-2785-46d2-b188-7347a04421b9)


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
