# Sales Analytics Dashboard

A complete end-to-end sales analytics project built with Python, Power BI, and FastAPI — designed to derive business insights from retail sales data.

## Project Overview

This project demonstrates a full data analytics pipeline:
- **Data Source**: Superstore retail dataset (9,994 transactions)
- **ETL Pipeline**: Python + Pandas for data cleaning and transformation
- **Analysis**: Statistical insights, trend analysis, and segmentation
- **Dashboard**: Power BI with 4 interactive visualizations
- **API**: FastAPI backend exposing analytics endpoints

## Key Business Insights

- Total Sales: **$2,297,200**
- Total Profit: **$286,397**
- Avg Profit Margin: **12.03%**
- Top Category: **Technology ($836K)**
- Top Region: **West ($108K profit)**
- High discounts (40%+) cause **average loss of $106 per order**

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| ETL & Analysis | Pandas, NumPy, Matplotlib, Scikit-learn |
| Dashboard | Power BI |
| API | FastAPI, Uvicorn |
| Database | CSV, SQLAlchemy |
| Version Control | Git, GitHub |

## Project Structure
```
sales-analytics-dashboard/
├── data/
│   ├── raw/          # Original dataset
│   ├── clean/        # Cleaned data
│   └── charts/       # Generated charts
├── api/
│   └── main.py       # FastAPI backend
├── etl_pipeline.py   # Data cleaning pipeline
├── analysis.py       # Data analysis scripts
└── README.md
```

## Dashboard Preview

Built in Power BI with 4 visualizations:
1. Sales by Category
2. Profit by Region
3. Monthly Sales Trend
4. Profit by Customer Segment

## API Endpoints

| Endpoint | Description |
|---|---|
| GET / | API health check |
| GET /summary | Full business summary |
| GET /sales-by-category | Sales breakdown by category |
| GET /profit-by-region | Profit breakdown by region |
| GET /profit-by-segment | Profit breakdown by segment |

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run ETL pipeline
python etl_pipeline.py

# Run analysis
python analysis.py

# Start API
uvicorn api.main:app --reload
```
