import json
import pandas as pd
import sys
def analysis(file,user_id):
    times = 0
    minutes = 0
    filename = file
    df = pd.read_json(filename)
    times = len(df[df['user_id'] == int(user_id)])
    minutes = df[df['user_id'] == int(user_id)]['minutes'].sum()
    return times,minutes

if __name__ == '__main__':
    print(analysis(sys.argv[1],sys.argv[2]))


