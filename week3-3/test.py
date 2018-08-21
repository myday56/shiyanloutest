import getopt,sys,socket
opts,args = getopt.getopt(sys.argv[1:],"h:p:",["host=","port="])
host_ip = opts[0][1]
host_port = opts[1][1]

def connect_socket(host,port):
    host = host_ip
    port = host_port
    s = socket.socket()
    s.settimeout(0.1)
    if int(s.connect_ex((host,port))) == 0:
        print(port,'open')
    else:
        print(port,'closed')

if len(host_ip.split('.')) == 4:
   if len(args) == 0:
        if '-' not in host_port:
        	connect_socket(host_ip,host_port)
            # print(host_port)
        else:
            a = host_port.split('-')
            # print(a[0],a[1])
            for i in range(int(a[0]),int(a[1])+1):
                connect_socket(host_ip,host_port)
else:
    print('sth wrong')