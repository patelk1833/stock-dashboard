# Install required libraries (run in terminal if needed)
# !pip install streamlit yfinance pandas plotly

import requests
import streamlit as st # type: ignore
import yfinance as yf # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import plotly.graph_objects as go # type: ignore
from stocknews import StockNews # type: ignore
from alpha_vantage.fundamentaldata import FundamentalData # type: ignore

# Introduction Text
st.markdown("""
## Welcome to the USA Stock Data Dashboard

This interactive stock data dashboard is designed to help users analyze and visualize stock market data effectively. 
The dashboard provides real-time stock prices, historical trends, dividends, financial statements, and market news, 
all in one place. 

You can explore different tabs to view raw stock data, price charts, volume trends, moving averages, and fundamental 
financial data such as balance sheets, income statements, and cash flow statements. The data is fetched using APIs 
from Yahoo Finance, Polygon.io, and Alpha Vantage.

Stay informed and make better investment decisions!

### Created by Krish Patel
""")


# Import the CSS file for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply the CSS
local_css("style.css")

# Page title
st.title("USA Stock Data Dashboard")

# Sidebar inputs for customization
st.sidebar.header("Stock Settings")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))
ma_window = st.sidebar.slider("Moving Average Window", min_value=5, max_value=50, value=20)


# Fetching data from Yahoo Finance
st.write(f"Fetching data for **{ticker_symbol}** from {start_date} to {end_date}...")
try:
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
    if data.empty:
        st.error("No data found. Please check the ticker symbol or date range.")
        st.stop()
except Exception as e:
    st.error(f"Error fetching data: {e}")
    st.stop()

# Calculating Moving Average
data['MA'] = data['Close'].rolling(window=ma_window).mean()

# Calculating Percentage Change
# Calculating Percentage Change with 2 decimal places
data['% Change'] = data['Close'].pct_change().fillna(0).apply(lambda x: round(x * 100, 2))


# Initialize Tabs for different views
tabs = st.tabs(["Raw Data", "Price Chart", "Volume Chart", "Moving Averages", "Dividends & Splits", "Info", "News"])

# Tab 1: Raw Data
# Tab 1: Raw Data with Proper Column Headers
with tabs[0]:
    st.subheader(f"Raw Data for {ticker_symbol}")
    # Ensure column headers are shown properly with st.dataframe()
    st.write(data.tail()[['Close', 'High', 'Low', 'Open', 'Volume', 'MA', '% Change']])
    st.download_button("Download Data as CSV", data.to_csv(), file_name=f"{ticker_symbol}_data.csv")

# Tab 2: Interactive Price Chart using Plotly
with tabs[1]:
    st.subheader("Closing Price Over Time")
    fig = px.line(data, x=data.index, y=data['Close'].values.flatten(), title=f"{ticker_symbol} - Closing Price")
    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="Closing Price (INR)",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig)

# Tab 3: Interactive Volume Chart
with tabs[2]:
    st.subheader("Volume Over Time")
    fig = px.bar(data, x=data.index, y=data['Volume'].values.flatten(), title=f"{ticker_symbol} - Volume Over Time")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig)

# Tab 4: Interactive Moving Averages Chart
with tabs[3]:
    st.subheader(f"Closing Price with {ma_window}-Day Moving Average")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'].values.flatten(), mode='lines', name='Closing Price'))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA'].values.flatten(), mode='lines', name=f'{ma_window}-Day Moving Average'))
    fig.update_layout(title=f"{ticker_symbol} - Moving Averages", template="plotly_dark")
    st.plotly_chart(fig)

# Tab 5: Dividends & Splits with CSV Download
with tabs[4]:
    st.subheader("Dividends & Splits")
    ticker = yf.Ticker(ticker_symbol)
    dividends = ticker.dividends.copy()
    dividends.index = dividends.index.tz_localize(None)
    splits = ticker.splits.copy()
    splits.index = splits.index.tz_localize(None)

    dividends = dividends.loc[start_date:end_date]
    splits = splits.loc[start_date:end_date]

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Dividends:**")
        st.dataframe(dividends)
        st.download_button("Download Dividends as CSV", dividends.to_csv(), file_name=f"{ticker_symbol}_dividends.csv")

    with col2:
        st.write("**Splits:**")
        st.dataframe(splits)
        st.download_button("Download Splits as CSV", splits.to_csv(), file_name=f"{ticker_symbol}_splits.csv")

# Tab 6: Company's Information From Alpha Vantage 
# Tab 6: Financial Data from Alpha Vantage with Currency Formatting and Download Option
# Tab 6: Financial Data from Alpha Vantage (with enhanced error handling)
with tabs[5]:
    alpha_vantage_key = st.secrets["alpha_vantage"]["key"]
    st.subheader(f"Financial Data for {ticker_symbol}")
    fd = FundamentalData(key=alpha_vantage_key, output_format='pandas')
    
    try:
        st.subheader("Balance Sheet")
        balance_sheet = fd.get_balance_sheet_annual(ticker_symbol)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
        st.download_button("Download Balance Sheet as CSV", bs.to_csv(), file_name=f"{ticker_symbol}_balance_sheet.csv")
    except Exception as e:
        st.error("Error fetching Cash Flow Statement data.API limit Reached.")
    
    try:
        st.subheader("Income Statement")
        income_statement = fd.get_income_statement_annual(ticker_symbol)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1)
        st.download_button("Download Income Statement as CSV", is1.to_csv(), file_name=f"{ticker_symbol}_income_statement.csv")
    except Exception as e:
        st.error("Error fetching Cash Flow Statement data.API limit Reached.")
    
    try:
        st.subheader("Cash Flow Statement")
        cash_flow = fd.get_cash_flow_annual(ticker_symbol)[0]
        cf = cash_flow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)
        st.download_button("Download Cash Flow Statement as CSV", cf.to_csv(), file_name=f"{ticker_symbol}_cash_flow.csv")
    except Exception as e:
        st.error("Error fetching Cash Flow Statement data.API limit Reached.")




# Tab 7: Stock News from Polygon.io
with tabs[6]:
    st.subheader(f"Latest News for {ticker_symbol}")
    
    # Set your Polygon.io API Key here
    polygon_key = st.secrets["polygon"]["key"]

    # Function to fetch news using Polygon.io API
    def get_stock_news_polygon(ticker):
        url = f"https://api.polygon.io/v2/reference/news?ticker={ticker}&apiKey={polygon_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            news_data = response.json()
            if 'results' in news_data:
                return news_data['results']
            else:
                return None
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching news: {e}")
            return None
    
    news_data = get_stock_news_polygon(ticker_symbol)
    if news_data:
        for i, article in enumerate(news_data[:5]):
            st.write(f"**News {i + 1}:**")
            st.write(f"**Published Date:** {article.get('published_utc', 'N/A')}")
            st.write(f"**Title:** {article.get('title', 'N/A')}")
            st.write(f"**Summary:** {article.get('description', 'N/A')}")
            st.write(f"**Sentiment:** {article.get('insights')[0].get('sentiment', 'N/A') if 'insights' in article and article['insights'] else 'N/A'}")
            st.write(f"**Source:** {article.get('publisher', {}).get('name', 'N/A')}")
            if article.get('image_url'):
                st.image(article.get('image_url'), caption="News Image", use_container_width =True)
            else:
                st.write("**Image URL:** Not Available")
            st.write("---")
    else:
        st.error("No news articles found for the specified ticker.")




# Footer message
st.sidebar.info("Dashboard Created with Streamlit, Yahoo Finance, and Plotly")



