import requests
import pandas as pd


def issues(repo):
    url = 'https://api.github.com/repos/%s/issues'%(repo)
    raw = requests.get(url)
    issues = pd.DataFrame(raw.json())
    user_name = []
    lable = pd.DataFrame(issues)
    for i in range(len(lable)):
        user_name.append(lable.get('user')[i]['login'])

    user_name_series = pd.Series(user_name)
    # print(type(user_name_series))
    lable2 = lable.copy()
    lable2['user_name'] = user_name_series
    issues_df = lable2[['number','title','user_name']]
#     issues_df.set_index(['number'],inplace=True)
    # print(issues_df)
    return issues_df

issues("numpy/numpy")
