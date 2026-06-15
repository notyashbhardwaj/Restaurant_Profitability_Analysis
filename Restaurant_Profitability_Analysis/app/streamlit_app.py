import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import plotly.express as px
import pandas as pd

import streamlit as st
from src.kpi_calculator import channel_margin

from src.data_loader import load_data
from src.profit_analysis import (
    total_revenue,
    total_profit,
    best_channel,
    worst_channel
)

from src.kpi_calculator import (
    net_profit_per_order,
    commission_drag_index,
    self_delivery_roi
)
# st.title("🔥 TEST DASHBOARD")
# st.error("YASH TEST 123")
st.title("🍽️ Restaurant Profitability Dashboard")
st.caption(
    "Cost Structure & Channel-Wise Profitability Analysis"
)
# Load Data
df = load_data("data/restaurant_data.csv")

st.set_page_config(
    page_title="Restaurant Profitability Dashboard",
    layout="wide"
)

st.title("🍽 Restaurant Profitability Dashboard")

# KPIs
col1, col2, col3, col4 = st.columns(4)

filtered_df = df.copy()

revenue = total_revenue(filtered_df)
profit = total_profit(filtered_df)

with col1:
    st.metric(
        "Total Revenue",
        f"${sum(revenue.values()):,.0f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${sum(profit.values()):,.0f}"
    )

with col3:
    st.metric(
        "Best Channel",
        best_channel(df)
    )

with col4:
    st.metric(
        "Worst Channel",
        worst_channel(df)
    )

st.divider()

# Additional KPIs

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Profit Per Order",
        net_profit_per_order(df)
    )

with c2:
    st.metric(
        "Commission Drag %",
        commission_drag_index(df)
    )

with c3:
    st.metric(
        "Self Delivery ROI %",
        self_delivery_roi(df)
    )

st.divider()

st.subheader("🏆 Top 10 Most Profitable Restaurants")

filtered_df["TotalProfit"] = (
    filtered_df["InStoreNetProfit"]
    + filtered_df["UberEatsNetProfit"]
    + filtered_df["DoorDashNetProfit"]
    + filtered_df["SelfDeliveryNetProfit"]
)

top10 = filtered_df.nlargest(
    10,
    "TotalProfit"
)[["RestaurantName", "CuisineType", "TotalProfit"]]

st.dataframe(top10, use_container_width=True)

st.subheader("📊 Revenue by Channel")

revenue = total_revenue(filtered_df)

revenue_df = pd.DataFrame({
    "Channel": revenue.keys(),
    "Revenue": revenue.values()
})

fig = px.bar(
    revenue_df,
    x="Channel",
    y="Revenue",
    title="Revenue Comparison Across Channels"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("💰 Profit by Channel")

profit = total_profit(filtered_df)

profit_df = pd.DataFrame({
    "Channel": profit.keys(),
    "Profit": profit.values()
})

fig2 = px.bar(
    profit_df,
    x="Channel",
    y="Profit",
    title="Profit Comparison Across Channels"
)

st.plotly_chart(fig2, use_container_width=True)

# Revenue Table

st.subheader("Revenue by Channel")
st.write(revenue)

# Profit Table

st.subheader("Profit by Channel")
st.write(profit)

# Dataset Preview

st.subheader("Dataset Preview")
st.dataframe(df.head(20))

df = load_data("data/restaurant_data.csv")

st.sidebar.header("Filters")

selected_cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    ["All"] + sorted(df["CuisineType"].unique().tolist())
)

selected_segment = st.sidebar.selectbox(
    "Select Segment",
    ["All"] + sorted(df["Segment"].unique().tolist())
)
filtered_df = df.copy()


if selected_cuisine != "All":
    filtered_df = filtered_df[
        filtered_df["CuisineType"] == selected_cuisine
    ]

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]

st.subheader("📥 Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_restaurant_data.csv",
    mime="text/csv"
)
st.subheader("📈 Channel Margin (%)")

margin = channel_margin(filtered_df)

margin_df = pd.DataFrame({
    "Channel": margin.keys(),
    "Margin": margin.values()
})

fig3 = px.bar(
    margin_df,
    x="Channel",
    y="Margin",
    title="Profit Margin by Channel (%)"
)

st.plotly_chart(fig3, use_container_width=True)