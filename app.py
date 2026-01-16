import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import pickle

# page config
st.set_page_config(
    page_title="Super Store Management Dashboard",
    layout="wide"
)

# CSS 
st.markdown("""
<style>
body {background-color:#0e1117;}
.dashboard-title {
    font-size:38px;
    font-weight:700;
    color:#00e5ff;
}
.dashboard-subtitle {
    font-size:18px;
    color:#9ca3af;
    margin-bottom:20px;
}
.kpi {
    background:#1f2933;
    padding:20px;
    border-radius:12px;
    text-align:center
}
.kpi h1 {color:#00e5ff}
</style>
""", unsafe_allow_html=True)


#Dashbord header
st.markdown("<div class='dashboard-title'>🏬 Super Store Management Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='dashboard-subtitle'>Sales • Profit • Customer Insights • ML Prediction</div>", unsafe_allow_html=True)
st.markdown("---")


BASE_PATH = r"C:\Users\kavi vala\Desktop\superstore dashbord"


#Load data
conn = sqlite3.connect(f"{BASE_PATH}\\database\\superstore.db")
df_full = pd.read_sql("SELECT * FROM orders", conn)


#Sidebar Filters
st.sidebar.title("📊 Super Store Dashboard")
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Region",
    df_full["Region"].unique(),
    default=df_full["Region"].unique()
)

category = st.sidebar.multiselect(
    "Category",
    df_full["Category"].unique(),
    default=df_full["Category"].unique()
)

#Filter data
df = df_full[
    (df_full["Region"].isin(region)) &
    (df_full["Category"].isin(category))
]


#KPIs
col1, col2, col3 = st.columns(3)

col1.markdown(
    f"<div class='kpi'><h4>Total Sales</h4><h1>₹{df.Sales.sum():,.0f}</h1></div>",
    unsafe_allow_html=True
)

col2.markdown(
    f"<div class='kpi'><h4>Total Profit</h4><h1>₹{df.Profit.sum():,.0f}</h1></div>",
    unsafe_allow_html=True
)

col3.markdown(
    f"<div class='kpi'><h4>Total Orders</h4><h1>{df.shape[0]}</h1></div>",
    unsafe_allow_html=True
)
#charts
col4, col5 = st.columns(2)

fig1 = px.bar(
    df.groupby("Category").sum().reset_index(),
    x="Category",
    y="Sales",
    title="Sales by Category"
)

fig2 = px.pie(
    df,
    names="Region",
    values="Profit",
    title="Profit by Region"
)

col4.plotly_chart(fig1, use_container_width=True)
col5.plotly_chart(fig2, use_container_width=True)


# ML prediction
st.markdown("---")
st.subheader("📈 Super Store Sales Prediction (ML Model)")

model = pickle.load(open(f"{BASE_PATH}\\model\\sales_model.pkl", "rb"))

# AUTO UPDATE Quantity & Discount BASED ON FILTER
avg_qty = int(df["Quantity Sold"].mean()) if not df.empty else 1
avg_disc = float(round(df["Discount"].mean(), 2)) if not df.empty else 0.0

qty = st.slider(
    "Quantity (Auto from Filters)",
    1, 20,
    value=min(max(avg_qty, 1), 20)
)

disc = st.slider(
    "Discount (Auto from Filters)",
    0.0, 0.8,
    value=min(max(avg_disc, 0.0), 0.8)
)

pred = model.predict([[qty, disc]])

st.success(f"Predicted Sales: ₹{pred[0]:,.2f}")

st.caption(
    "🔍 Quantity & Discount values automatically adapt based on selected Region & Category filters."
)
