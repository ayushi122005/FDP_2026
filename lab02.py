import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# 🌟 App Configuration
# -------------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard (CSV Interactive App)")
st.write("Upload a CSV file or use the sample data below to explore your sales interactively.")

# -------------------------------
# 🧾 Upload CSV File
# -------------------------------
uploaded_file = st.file_uploader("📁 Upload CSV file", type=["csv"])

# -------------------------------
# 📂 Sample Data (if no file uploaded)
# -------------------------------
sample_data = {
    "date": [
        "2025-01-01", "2025-01-03", "2025-01-05", "2025-01-07",
        "2025-01-09", "2025-01-11", "2025-01-13", "2025-01-15",
        "2025-01-20", "2025-01-25"
    ],
    "product": [
        "Widget A", "Widget B", "Widget C", "Widget A",
        "Widget B", "Widget C", "Widget A", "Widget B",
        "Widget C", "Widget A"
    ],
    "region": [
        "North", "South", "East", "West",
        "East", "South", "North", "West",
        "North", "South"
    ],
    "quantity": [5, 3, 8, 6, 4, 7, 5, 3, 9, 4],
    "unit_price": [20, 30, 10, 20, 30, 10, 20, 30, 10, 20]
}

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
else:
    st.info("⚠️ No file uploaded — using sample sales data.")
    df = pd.DataFrame(sample_data)

# -------------------------------
# 🧮 Data Preprocessing
# -------------------------------
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["sales"] = df["quantity"] * df["unit_price"]

# -------------------------------
# 🎛️ Sidebar Filters
# -------------------------------
st.sidebar.header("Filter Options")

# Products Filter
products = st.sidebar.multiselect(
    "Select Product(s):",
    options=df["product"].unique(),
    default=df["product"].unique()
)

# Regions Filter
regions = st.sidebar.multiselect(
    "Select Region(s):",
    options=df["region"].unique(),
    default=df["region"].unique()
)

# Date Range Filter
start_date = st.sidebar.date_input("Start Date", df["date"].min())
end_date = st.sidebar.date_input("End Date", df["date"].max())

# -------------------------------
# 🔍 Apply Filters
# -------------------------------
filtered_df = df[
    (df["product"].isin(products)) &
    (df["region"].isin(regions)) &
    (df["date"].between(pd.to_datetime(start_date), pd.to_datetime(end_date)))
]

# -------------------------------
# 📋 Show Filtered Data
# -------------------------------
st.subheader("📄 Filtered Data Preview")
st.dataframe(filtered_df, use_container_width=True)

# -------------------------------
# 📈 Charts Section
# -------------------------------
st.markdown("---")
st.subheader("📊 Visualizations")

col1, col2 = st.columns(2)

# --- Chart 1: Sales Over Time ---
with col1:
    st.markdown("### Sales Over Time")
    sales_over_time = filtered_df.groupby("date")["sales"].sum().reset_index()
    fig_line = px.line(
        sales_over_time, x="date", y="sales",
        markers=True, title="Sales Trend Over Time",
        color_discrete_sequence=["#007bff"]
    )
    st.plotly_chart(fig_line, use_container_width=True)

# --- Chart 2: Sales by Product ---
with col2:
    st.markdown("### Sales by Product")
    sales_by_product = filtered_df.groupby("product")["sales"].sum().reset_index()
    fig_bar = px.bar(
        sales_by_product, x="product", y="sales",
        color="product", title="Sales by Product",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- Chart 3: Sales by Region (Pie Chart) ---
st.markdown("### Sales by Region")
sales_by_region = filtered_df.groupby("region")["sales"].sum().reset_index()
fig_pie = px.pie(
    sales_by_region, names="region", values="sales",
    title="Sales Distribution by Region",
    color_discrete_sequence=px.colors.sequential.RdBu
)
st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------------
# 📊 Summary Metrics
# -------------------------------
st.markdown("---")
st.subheader("📈 Summary Metrics")

total_sales = filtered_df["sales"].sum()
total_orders = len(filtered_df)
avg_order_value = filtered_df["sales"].mean()

colA, colB, colC = st.columns(3)
colA.metric("💰 Total Sales", f"₹{total_sales:,.2f}")
colB.metric("📦 Total Orders", f"{total_orders}")
colC.metric("📉 Avg. Order Value", f"₹{avg_order_value:,.2f}")