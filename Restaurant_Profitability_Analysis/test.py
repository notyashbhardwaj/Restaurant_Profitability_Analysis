from src.data_loader import load_data
from src.kpi_calculator import *
from src.visualization import *
from src.profit_analysis import (
    total_revenue,
    total_profit,
    best_channel,
    worst_channel
)

df = load_data("data/restaurant_data.csv")

print("Revenue")
print(total_revenue(df))

print("\nProfit")
print(total_profit(df))

print("\nBest Channel")
print(best_channel(df))

print("\nWorst Channel")
print(worst_channel(df))



print("\nNet Profit Per Order")
print(net_profit_per_order(df))

print("\nChannel Margin (%)")
print(channel_margin(df))

print("\nCommission Drag Index")
print(commission_drag_index(df))

print("\nSelf Delivery ROI")
print(self_delivery_roi(df))



revenue_chart(df)
profit_chart(df)
margin_chart(df)