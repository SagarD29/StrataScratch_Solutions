import pandas as pd

finance_sector = forbes_global_2010_2014[
    forbes_global_2010_2014["sector"] == "Financials"
]

finance_sector["rank"] = finance_sector["profits"].rank(
    method="min", ascending=False
)

result = finance_sector[finance_sector["rank"] == 1][["company", "continent"]]
