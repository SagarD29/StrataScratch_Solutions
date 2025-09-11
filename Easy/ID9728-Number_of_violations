# Import your libraries
import pandas as pd

# Start writing code
sf = sf_restaurant_health_violations
sf=sf[sf.business_name=="Roxanne Cafe"]
sf.groupby((sf["inspection_date"]).dt.year)["violation_id"].count().reset_index()
