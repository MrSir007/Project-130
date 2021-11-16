import csv
import pandas as pd

getData = pd.read_csv("final.csv")
"""print(getData.shape)"""

# To remove unnecessary columns from the data
del getData["Unnamed: 0"]

# To rename the columns
getData = getData.rename({
  "Star_name": "name"
}, axis="columns")

getData.to_csv("result.csv")