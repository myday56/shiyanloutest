import requests
from lxml import html
def user_info(user_id):
    user_id = user_id
    url = "https://www.shiyanlou.com/user/"
    content = requests.get(url+user_id)
    tree = html.fromstring(content.text)
    user_name = tree.xpath('//span[@class="username"]/text()')
    if user_name == []:
        user_name = None
        user_level = None
        join_date = None
    else:
        user_name = "".join(user_name)
        level = tree.xpath('//span[@class="user-level"]/text()')
        user_level = "".join(level)
        user_level = int(user_level[1:])
        join_date = tree.xpath('//span[@class="join-date"]/text()')
        join_date = "".join(join_date)
        join_date = join_date[:10]
    return user_name,user_level,join_date

user_info("214893")
print(user_info("214893"))
