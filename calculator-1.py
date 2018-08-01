import sys
# money_list = {}
def input_num():
    l = []
    for arg in sys.argv[1:]:
        n = arg.split(':')
        l.append(n)
    return l
def shebao(x):
    x1 = 0.08
    x2 = 0.02
    x3 = 0.005
    x4 = 0.00
    x5 = 0.00
    x6 = 0.06
    x_sum = x1+x2+x3+x4+x5+x6
    shishou = float(x) *(1 - x_sum)
    return shishou


def geshui(x):  
    try:
        x = int(x)
    except ValueError:
        print("Parameter Error")
    else:
        a = x - 3500
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
        # print(format(x,".2f"))
        result = format(a-x,".2f")
        return result



l = input_num()
x = len(l)
for i in range(x):
    # print(l[i][1])
    a = shebao(l[i][1])
    print(l[i][0]+":"+geshui(a))
