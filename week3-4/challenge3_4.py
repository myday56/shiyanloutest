import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
            r'(\d+.\d+.\d+.\d+)\s-\s-\s'
            r'\[(.+)\]\s'
            r'"GET\s(.+)\s\w+/.+"\s'
            r'(\d+)\s'
            r'(\d+)\s'
            r'"(.+)"\s'
            r'"(.+)"'
            )
        parsers = re.findall(pattern,logfile.read())
    return parsers

def main():
    logs = open_parser('/home/shiyanlou/Code/nginx.log')

    pass
    return ip_dict,url_dict

if __name__ == '__main__':
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)