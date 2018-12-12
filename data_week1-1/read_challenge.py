import pandas as pd
import tables
def convert(file):
    obj = pd.read_json(file).head(1000)
    obj.to_hdf('user_study.h5',key='data')

convert("users_data.json")
