import pandas as pd
import numpy as np

merge = pd.merge(customers, orders, left_on="id", right_on="cust_id")
cust = ["Jill", "Eva"]
result = merge[merge["first_name"].isin(cust)][
    ["first_name", "order_date", "order_details", "total_order_cost"]
]
