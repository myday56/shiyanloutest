import pandas as pd
from matplotlib import pyplot as plt

filename = 'user_study.json'
df = pd.read_json(filename)
def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    df1 = df[['user_id','minutes']].groupby('user_id').sum()
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    x = df1.index
    y = df1
    ax.plot(x,y)
    plt.show()
    return ax

if __name__ == '__main__':
    data_plot()

