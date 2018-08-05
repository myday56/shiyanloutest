import sys
try:
    n = int(sys.argv[1])
except ValueError:
    print("Parameter Error")
else:
    a = n - 3500
    if a <= 0:
        x = 0
    elif a <= 1500:
        x = a*0.03
    elif a <= 4500:
        x = a*0.10 - 105
    elif a <= 9000:
        x = a*0.20 - 555
    elif a <= 35000:
        x = a*0.25 - 1005
    elif a <= 55000:
        x = a*0.30 - 2755
    elif a <= 80000:
        x = a*0.35 - 5505
    else:
        x = a*0.45 - 13505
    print(format(x,".2f"))
