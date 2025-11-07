# Lifestyle and Health Risk Streamlit Dashboard
<img width="1211" height="587" alt="Image" src="https://github.com/user-attachments/assets/7b330b39-3383-4112-a397-01e1e4ab0f53" />

View the deployed Streamlit application:  https://yujin-k9-streamlit-portfolio-portfolio-mndq24.streamlit.app/



This Streamlit app explores relationships between **lifestyle habits** and **health risk indicators** using a synthetic dataset of 5,000 individuals.  
It provides interactive data visualizations, summary metrics, and future work plans for expanding the analysis.


## Author
**Yujin Kim**  
📧 ykim20@msudenver.edu  


## App Navigation Overview

This Streamlit app is structured into **four interactive pages**, accessible from the left sidebar:

### ① Bio  

Introduces the author and project purpose.  
Includes a professional bio, contact information, and visualization philosophy emphasizing **clarity, accessibility, and ethical communication**.  

### ② EDA Gallery 

Showcases **Exploratory Data Analysis (EDA)** with four unique chart types:  
- **Bar Chart** – Exercise Frequency vs. Health Risk  
- **Scatter Plot** – Sleep Duration vs. BMI  
- **Box Plot** – Marital Status vs. BMI  
- **Heatmap** – Correlations between numeric variables  
Each visualization includes a guiding question, “How to read this chart” section, and key insights.

### ③ Dashboard  

An **interactive analytics dashboard** combining key metrics and filters.  
Displays:
- Average BMI, Sleep Hours, and High-Risk Percentage  
- Dynamic filters for Exercise Level, Age Range, and Alcohol Consumption  
Visuals and KPIs update instantly based on user selections, allowing customized exploration.

### ④ Future Work  

Outlines **next development steps** and reflections from prototype to final build.  
Includes:
- Predictive modeling (forecasting) ideas  
- Data enrichment and accessibility audits  
- A/B layout experimentation for improved usability  
Features an embedded concept image and professional reflection.

## Dataset Information

**Dataset:** [[Lifestyle and Health Risk Prediction (Synthetic)](https://www.kaggle.com/datasets/miadul/lifestyle-and-health-risk-prediction)]  
**Records:** 5,000 rows  
**Source:** Kaggle (Synthetic Dataset — not based on real people)  

**Preprocessing Performed:**
- Converted categorical variables to ordered categories for logical chart display (e.g., exercise level)
- Created a derived numeric column `risk_score` to represent health risk levels for visualization purposes
- Sampled 200 records for scatter plot clarity (to avoid overplotting)

**Ethics Note:**  
This dataset is **synthetic** and does **not include real individuals**.  
All visuals use color-blind-safe palettes, clear labeling, and descriptive titles for accessibility.  
Charts illustrate general patterns only and are **not intended for personal health prediction**.


## Requirements

All dependencies are listed in `requirements.txt`.  
Install them before running the app:

```bash
pip install -r requirements.txt
```

## AI Assistance Acknowledgment

This project was partially developed with ChatGPT (OpenAI) for code refinement and documentation clarity.
All data analysis and final implementation were reviewed and completed by the author.
