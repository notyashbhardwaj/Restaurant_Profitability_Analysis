import matplotlib.pyplot as plt
from src.profit_analysis import total_revenue, total_profit
from src.kpi_calculator import channel_margin


def revenue_chart(df):

    revenue = total_revenue(df)

    plt.figure(figsize=(8, 5))
    plt.bar(revenue.keys(), revenue.values())
    plt.title("Revenue by Channel")
    plt.ylabel("Revenue")
    plt.show()


def profit_chart(df):

    profit = total_profit(df)

    plt.figure(figsize=(8, 5))
    plt.bar(profit.keys(), profit.values())
    plt.title("Profit by Channel")
    plt.ylabel("Profit")
    plt.show()


def margin_chart(df):

    margin = channel_margin(df)

    plt.figure(figsize=(8, 5))
    plt.bar(margin.keys(), margin.values())
    plt.title("Profit Margin (%)")
    plt.ylabel("Margin %")
    plt.show()