def net_profit_per_order(df):

    total_orders = df["MonthlyOrders"].sum()

    total_profit = (
        df["InStoreNetProfit"].sum()
        + df["UberEatsNetProfit"].sum()
        + df["DoorDashNetProfit"].sum()
        + df["SelfDeliveryNetProfit"].sum()
    )

    return round(total_profit / total_orders, 2)


def channel_margin(df):

    return {
        "InStore": round(
            (df["InStoreNetProfit"].sum() /
             df["InStoreRevenue"].sum()) * 100, 2
        ),

        "UberEats": round(
            (df["UberEatsNetProfit"].sum() /
             df["UberEatsRevenue"].sum()) * 100, 2
        ),

        "DoorDash": round(
            (df["DoorDashNetProfit"].sum() /
             df["DoorDashRevenue"].sum()) * 100, 2
        ),

        "SelfDelivery": round(
            (df["SelfDeliveryNetProfit"].sum() /
             df["SelfDeliveryRevenue"].sum()) * 100, 2
        )
    }


def commission_drag_index(df):

    return round(
        (df["CommissionRate"].mean() * 100),
        2
    )


def self_delivery_roi(df):

    profit = df["SelfDeliveryNetProfit"].sum()

    cost = df["SD_DeliveryTotalCost"].sum()

    return round((profit / cost) * 100, 2)