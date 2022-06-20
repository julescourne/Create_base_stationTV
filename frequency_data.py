import pandas as pd
import os
import numpy as np
from common import get_channel_name_by_code


df = pd.read_csv(r"meta_data.csv")

# get other information by hashcode
def get_by_hashcode(h):
    case = {}
    duration = []
    for row in df.itertuples():
        if(row.Hashcode == h):
            duration.append(int(row.Length))           
            case = {
            "Channel_Code": row.Channel_Code,
            "Channel_Name": get_channel_name_by_code(row.Channel_Code),
            "Hashcode" : row.Hashcode,
            "Title": row.Title
            }    
    
    duration_array = np.asarray(duration, dtype=np.int64)
    mean_duration = np.mean(duration_array)
    total_duration = np.sum(duration_array)
    case["Mean_duration"] = mean_duration
    case["Total_duration"] = total_duration
    return case
# ---------------------------------------------------------
data_dict = {}
for row in df.itertuples():
    if(row.Hashcode in data_dict):
        data_dict[row.Hashcode] += 1
    else:
        data_dict[row.Hashcode] = 1

# print(data_dict)

d_list = []
for key, value in data_dict.items():    
    case = get_by_hashcode(key)    
    case["Frequency"] = value
    d_list.append(case)

df = pd.DataFrame(d_list)
df["Mean_duration"]  = df['Mean_duration'].map('{:,.2f}'.format)
df.to_csv("data.csv", index = False, header=True, encoding="utf-8-sig")