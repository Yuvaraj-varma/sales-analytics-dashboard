from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI(title="Sales Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("data/clean/superstore_clean.csv")

@app.get("/")
def home():
    return {"message": "Sales Analytics API is running!"}

@app.get("/summary")
def summary():
    return {
        "total_sales": round(df["Sales"].sum(), 2),
        "total_profit": round(df["Profit"].sum(), 2),
        "total_orders": int(df["Order ID"].nunique()),
        "total_customers": int(df["Customer ID"].nunique()),
        "avg_profit_margin": round(df["Profit Margin %"].mean(), 2)
    }

@app.get("/sales-by-category")
def sales_by_category():
    result = df.groupby("Category")["Sales"].sum().round(2)
    return result.to_dict()

@app.get("/profit-by-region")
def profit_by_region():
    result = df.groupby("Region")["Profit"].sum().round(2)
    return result.to_dict()

@app.get("/profit-by-segment")
def profit_by_segment():
    result = df.groupby("Segment")["Profit"].sum().round(2)
    return result.to_dict()
