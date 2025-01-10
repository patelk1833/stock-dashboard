# Stock Market Data Analysis Dashboard using Python and Streamlit
### By: **Krish Patel**  
### Date: **2/10/2025**
---

## Overview
This project involves the development of a comprehensive **Stock Market Data Analysis Dashboard** using **Python** and **Streamlit**. The primary objective of the dashboard is to provide **financial insights**, **stock price trends**, and **market analysis** for investors and financial analysts in a **user-friendly web interface**.

The dashboard integrates multiple data sources, including **Yahoo Finance**, **Polygon.io**, and **Alpha Vantage** APIs to fetch real-time stock data, financial statements, and recent news articles for the selected companies. Users can input stock ticker symbols and customize the date range for analysis, enabling personalized data exploration.

### Key features of the dashboard include:
- **Stock Price Visualization:** Interactive price charts using Plotly.
- **Moving Averages & Volume Analysis:** Graphical representation of price movements with dynamic moving averages.
- **Financial Data:** Display of balance sheets, income statements, and cash flow statements retrieved using Alpha Vantage API.
- **News Sentiment Analysis:** Latest financial news with sentiment insights and source attribution.
- **Dividend & Split Data:** Side-by-side display of dividend and stock split data with CSV download options.

---

## Objectives
1. **Data Analysis & Visualization:** Provide interactive charts and data tables for stock prices, volume, and moving averages.
2. **Financial Insights:** Display financial statements, dividends, and splits with CSV download options for better data exploration.
3. **Access to Data:** Ensure seamless access to financial data through API integration for accurate and real-time information.

---

## Methodology

### 1. Data Collection
The data for this project was collected using multiple financial data APIs to ensure comprehensive coverage of stock information.  
- **Yahoo Finance API:** Used to gather historical stock price data, dividends, and stock splits.  
- **Alpha Vantage API:** Employed to retrieve detailed company financial information, including balance sheets, income statements, and cash flow statements.  
- **Polygon.io API:** Integrated to fetch the latest financial news and sentiment analysis related to the selected stock ticker, providing a holistic view of the company's market performance.

### 2. Data Processing
Once the data was collected, it underwent processing to ensure clarity and usability.  
- The data was **cleaned and formatted** for better readability, and missing values were handled appropriately.  
- Financial data was transformed into a structured tabular format suitable for display, while moving averages were calculated to provide trend analysis insights.  
- This step ensured the data was ready for accurate representation and analysis in the dashboard.

### 3. Visualization through Plotly
The processed data was visualized using **Plotly**, a powerful Python library for creating interactive charts.  
- Price trends, volume, and moving averages were represented using **line and bar charts**, while financial data and news articles were displayed in a structured **tabular format** for better clarity.  
- This visualization provided users with an intuitive understanding of the stock's performance.

### 4. User Interface Design
The dashboard was developed using **Streamlit**, a Python-based web framework ideal for data visualization projects.  
- The interface was organized using a **tab-based layout** for seamless navigation across raw data, price charts, financial data, and news sections.  
- Custom **CSS** was used to enhance the visual appeal of the dashboard, while interactive controls for **stock ticker selection**, **date range adjustments**, and **CSV download options** were added to ensure accessibility and ease of use.

---

## Conclusion
The **Stock Market Data Analysis Dashboard** provides an intuitive platform for exploring stock market data through comprehensive financial metrics, price trends, and company news.  
By integrating multiple APIs and utilizing tools like **Streamlit** and **Plotly**, the dashboard offers a visually appealing and user-friendly experience for market analysis. This project serves as a foundation for further financial data exploration, empowering users to make **informed investment decisions**.

---

## Future Work
The future scope of this project includes:
- Simplifying data access for companies from **various countries**.  
- Allowing users to input **company names** with automatic **ticker retrieval**.  
- Integrating **AI for in-depth analysis**, including financial sentiment insights, to further enhance decision-making capabilities.

---

## Skills Demonstrated
- **Advanced Python programming** (Pandas, NumPy, Plotly)  
- **API Integration and Data Collection** (Yahoo Finance, Alpha Vantage, Polygon.io)  
- **Data Preprocessing and Transformation**  
- **Financial Data Analysis and Visualization**  
- **Interactive Dashboard Development** using Streamlit and CSS  
- **CSV Handling and Export Functionality**  
- **Error Handling and Validation Techniques**  
- **Project Structuring and Code Management**  

---

## Repository Contents
- **main.py:** The core Python script that runs the Streamlit dashboard.  
- **requirements.txt:** List of dependencies required for running the project.  
- **style.css:** Custom CSS for enhancing the visual appearance of the dashboard.  
- **.gitignore:** Specifies files and folders to exclude from version control (e.g., `.streamlit/secrets.toml`).  
- **README.md:** Provides a summary of the project, setup instructions, and usage guidelines.

---

## Dashboard Link:
You can access the live dashboard here: **[Stock-dashboard-Streamlit](#)**  

