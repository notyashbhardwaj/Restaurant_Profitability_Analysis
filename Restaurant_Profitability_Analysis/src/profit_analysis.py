import pandas as pd

def total_revenue(df):

    return {
        "InStore": df["InStoreRevenue"].sum(),
        "UberEats": df["UberEatsRevenue"].sum(),
        "DoorDash": df["DoorDashRevenue"].sum(),
        "SelfDelivery": df["SelfDeliveryRevenue"].sum()
    }


def total_profit(df):

    return {
        "InStore": df["InStoreNetProfit"].sum(),
        "UberEats": df["UberEatsNetProfit"].sum(),
        "DoorDash": df["DoorDashNetProfit"].sum(),
        "SelfDelivery": df["SelfDeliveryNetProfit"].sum()
    }


def best_channel(df):

    profits = total_profit(df)

    return max(profits, key=profits.get)


def worst_channel(df):

    profits = total_profit(df)

    return min(profits, key=profits.get)