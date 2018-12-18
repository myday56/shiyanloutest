import sqlite3
import pandas as pd

def count(file,user_id):
    sql_con = sqlite3.connect(file)
    sql_query = "select sum(minutes) from data where user_id='%s'"%(user_id)
    a = pd.read_sql(sql_query,sql_con)
    sum_minutes = a['sum(minutes)'][0]
    if sum_minutes == None:
        sum_minutes = 0
    else:
        sum_minutes = int(sum_minutes)
    return sum_minutes

a = count("users_data.sqlite",8490)
print(a)

