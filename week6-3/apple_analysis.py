import pandas as pd


def quarter_volume():
    df = pd.read_csv('apple.csv',header=0)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df1 = df.resample('Q').sum().to_period('Q')
    second_volume = df1['Volume'].sort_values()[-2]
    return second_volume

if __name__ == '__main__':
    quarter_volume()
