import pandas as pd
import numpy as np
def co2():
    df_data = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    df_country = pd.read_excel("ClimateChange.xlsx",sheetname='Country')
    df_series = pd.read_excel("ClimateChange.xlsx",sheetname='Series')

    df_data = df_data[df_data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    df_data.drop(labels = ['Country name','Series code','Series name','SCALE','Decimals'],axis=1,inplace=True)
    df_data.replace('..',np.nan,inplace=True)
    df_data = df_data.fillna(method='bfill',axis=1)
    df_data = df_data.fillna(method='ffill',axis=1)
    df_data.dropna(how='all',inplace=True)
    df_data['Sum emissions'] = df_data.sum(axis=1)
    df_data = df_data['Sum emissions']

    df_country.set_index('Country code',inplace=True)
    df_country.drop(labels=['Capital city','Region','Lending category'],axis=1,inplace=True)
    df_clean = pd.concat([df_data,df_country],axis=1)

    df_sum = df_clean.groupby('Income group').sum()

    df_max = df_clean.sort_values(by='Sum emissions',ascending=False).groupby('Income group').head(1).set_index('Income group')
    df_max.columns = ['Highest emissions','Highest emission country']
    df_max = df_max.reindex(columns=['Highest emission country','Highest emissions'])

    df_min = df_clean.sort_values(by='Sum emissions').groupby('Income group').head(1).set_index('Income group')
    df_min.columns = ['Lowest emissions','Lowest emission country']
    df_min = df_min.reindex(columns=['Lowest emission country','Lowest emissions'])

    results = pd.concat([df_sum,df_max,df_min],axis=1)
    return results

print(co2())