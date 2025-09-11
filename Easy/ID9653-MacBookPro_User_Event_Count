import pandas as pd

macbook_device = playbook_events[playbook_events["device"] == "macbook pro"]
macbook_device.groupby(["event_name"])["location"].count().reset_index().rename(columns={"location": "event_count"})
