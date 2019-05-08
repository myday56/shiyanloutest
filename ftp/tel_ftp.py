from ftplib import FTP
ftp = FTP()
ftp.connect("192.168.1.120")
ftp.login("pi", "leletou")
# print(ftp.getwelcome())
path = "/home/pi/Desktop/record/"
ftp.cwd(path)
list_day = ftp.nlst()
for day in list_day:
    ftp.cwd(path+day)
    list_tel = ftp.nlst()
    for tel in list_tel:
        # print(path+day+"/"+tel)
        if tel == "1":
            ftp.cwd(path+day+"/"+tel)
            list_file = ftp.nlst()
            for file in list_file:
                filename = "RETR " + file
                ftp.retrbinary(filename,open(file,"wb"))
