import numpy as np
import pandas as pd
def clean():
    df_clean = None
    df = pd.read_csv("earthquake.csv")
    col_n = ['time','latitude','longitude','depth','mag','place']
    a = pd.DataFrame(df,columns=col_n)
    b=pd.DataFrame(a['place'].str.split(',',1).tolist(),columns=['loc','region'])
    col_clean = ['time','latitude','longitude','depth','mag','region']
    result = a.join(b)
    df_clean = pd.DataFrame(result,columns=col_clean)
    df_clean = df_clean.dropna()
    df_clean = df_clean.drop_duplicates()
    return df_clean
print(clean())
