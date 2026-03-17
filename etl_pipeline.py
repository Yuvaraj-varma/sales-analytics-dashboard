import pandas as pd
import os

# ── 1. EXTRACT ──────────────────────────────────────────
# Change this path to where your CSV is saved on your PC
RAW_FILE = "data/raw/Sample - Superstore.csv"

df = pd.read_csv(RAW_FILE, encoding='latin-1')
print(f"✅ Loaded {len(df)} rows, {len(df.columns)} columns")
print(f"Columns: {list(df.columns)}")

# ── 2. TRANSFORM ─────────────────────────────────────────

# Fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

# Create new useful columns
df['Order Year']        = df['Order Date'].dt.year
df['Order Month']       = df['Order Date'].dt.month
df['Order Month Name']  = df['Order Date'].dt.strftime('%B')
df['Days to Ship']      = (df['Ship Date'] - df['Order Date']).dt.days
df['Profit Margin %']   = (df['Profit'] / df['Sales'] * 100).round(2)

# Check for missing values
print(f"\n Missing values:\n{df.isnull().sum()}")

# Drop duplicates
before = len(df)
df = df.drop_duplicates()
print(f"\n Removed {before - len(df)} duplicates")

# Remove rows where Sales is 0 or negative
df = df[df['Sales'] > 0]
print(f"✅ Clean rows remaining: {len(df)}")

# ── 3. LOAD ───────────────────────────────────────────────
os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/superstore_clean.csv", index=False)
print(f"\n✅ Clean data saved to data/clean/superstore_clean.csv")

# ── 4. QUICK SUMMARY ─────────────────────────────────────
print("\n📊 Quick Business Summary:")
print(f"Total Sales    : ${df['Sales'].sum():,.2f}")
print(f"Total Profit   : ${df['Profit'].sum():,.2f}")
print(f"Avg Profit Margin: {df['Profit Margin %'].mean():.2f}%")
print(f"Total Orders   : {df['Order ID'].nunique()}")
print(f"Total Customers: {df['Customer ID'].nunique()}")
print(f"\nTop 3 Categories by Sales:")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False).head(3))