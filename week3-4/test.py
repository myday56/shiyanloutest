import re
from datetime import datetime

filename = '/home/shiyanlou/Code/nginx1.log'
with open(filename) as logfile:
    pattern = (r''
        r'(\d+.\d+.\d+.\d+)\s-\s-\s'    #ip
        r'\[(.+)\]\s'                   #time
        r'"GET\s(.+)\s\w+/.+"\s'        #path
        r'(\d+)\s'                      #state code
        r'(\d+)\s'                      #date size
        r'"(.+)"\s'                     #request head
        r'"(.+)"'                       #client
        )
    parsers = re.findall(pattern,logfile.read())
print(parsers)
print(parsers[0][0],parsers[0][3])