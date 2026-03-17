import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/clean/superstore_clean.csv")
os.makedirs("data/charts", exist_ok=True)

# ── 1. SALES BY YEAR ─────────────────────────────────────
yearly = df.groupby('Order Year')['Sales'].sum().reset_index()
plt.figure(figsize=(8,4))
plt.bar(yearly['Order Year'], yearly['Sales'], color='#2E75B6')
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('data/charts/sales_by_year.png')
plt.close()
print("✅ Chart 1 saved: sales_by_year.png")

# ── 2. PROFIT BY CATEGORY ────────────────────────────────
cat_profit = df.groupby('Category')['Profit'].sum().reset_index()
plt.figure(figsize=(8,4))
plt.barh(cat_profit['Category'], cat_profit['Profit'], color='#1F4E79')
plt.title('Total Profit by Category')
plt.xlabel('Profit ($)')
plt.tight_layout()
plt.savefig('data/charts/profit_by_category.png')
plt.close()
print("✅ Chart 2 saved: profit_by_category.png")

# ── 3. TOP 10 STATES BY SALES ────────────────────────────
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(state_sales.index, state_sales.values, color='#2E75B6')
plt.title('Top 10 States by Sales')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('data/charts/top_states.png')
plt.close()
print("✅ Chart 3 saved: top_states.png")

# ── 4. MONTHLY SALES TREND ───────────────────────────────
monthly = df.groupby(['Order Year','Order Month'])['Sales'].sum().reset_index()
monthly['Period'] = monthly['Order Year'].astype(str) + '-' + monthly['Order Month'].astype(str).str.zfill(2)
plt.figure(figsize=(14,5))
plt.plot(monthly['Period'], monthly['Sales'], color='#2E75B6', marker='o', markersize=3)
plt.title('Monthly Sales Trend')
plt.xticks(rotation=90)
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('data/charts/monthly_trend.png')
plt.close()
print("✅ Chart 4 saved: monthly_trend.png")

# ── 5. SEGMENT ANALYSIS ──────────────────────────────────
seg = df.groupby('Segment')[['Sales','Profit']].sum().reset_index()
print("\n📊 Segment Analysis:")
print(seg)

# ── 6. DISCOUNT IMPACT ───────────────────────────────────
print("\n📊 Discount Impact on Profit:")
df['Discount Band'] = pd.cut(df['Discount'], 
    bins=[-0.1, 0, 0.2, 0.4, 1.0],
    labels=['No Discount', 'Low (0-20%)', 'Medium (20-40%)', 'High (40%+)'])
print(df.groupby('Discount Band')['Profit'].mean().round(2))

print("\n✅ All charts saved to data/charts/")