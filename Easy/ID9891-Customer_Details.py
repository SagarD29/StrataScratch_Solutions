import pandas as pd

customers.merge(
    orders,
    how = "outer",
    left_on = "id",
    right_on = "cust_id"
    )[["first_name", "last_name", "city", "order_details"]].sort_values("first_name")