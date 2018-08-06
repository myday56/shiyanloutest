import sys
import csv
from multiprocessing import Process,Queue 

class Args:
    def __init__(self):
        try:
            l = sys.argv[1:]
            self.c = l[l.index('-c')+1]
            self.d = l[l.index('-d')+1]
            self.o = l[l.index('-o')+1]
        except (ValueError, AttributeError) as e:
            print("somethine wrong")
            exit()


class Config:
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        conf_file = Args().c
        with open(conf_file, 'r') as file:
            content = file.readlines()
            for line in content:
                v = line.strip().split(' = ')
                config[v[0]] = v[1]
        return config


class UserData():
    def __init__(self,q1):

        self.userdata = self._read_user_data(q1)

    def _read_user_data(self,q1):
        userdata = []
        user_data_file = Args().d
        with open(user_data_file, 'r') as file:
            content = file.readlines()
            for line in content:
                v = line.strip().split(',')
                userdata.append(v)
        q1.put(data)


class IncomeTaxCalculator:
    def calc_for_all_userdata(self,q1,q2):
        jishul = float(Config().config['JiShuL'])
        jishuh = float(Config().config['JiShuH'])
        yanglao = float(Config().config['YangLao'])
        yiliao = float(Config().config['YiLiao'])
        shiye = float(Config().config['ShiYe'])
        gongshang = float(Config().config['GongShang'])
        shengyu = float(Config().config['ShengYu'])
        gongjijin = float(Config().config['GongJiJin'])
        jishu_sum = yanglao+yiliao+shiye+gongshang+shengyu+gongjijin
        userdata_after_calc = []
        userdata_list = UserData()._read_user_data()
        userdata_list_len = len(userdata_list)
        for id,num in q1.get():
        # for i in range(userdata_list_len):
        #     id = userdata_list[i][0]
        #     num = userdata_list[i][1]
            try:
                x = float(num)  # å·¥èµ
            except ValueError:
                print("Parameter Error")
            else:
                if x <= jishul:  # å¦æå·¥èµä½äºç¤¾ä¿åºæ°
                    y = jishul * jishu_sum
                elif x >= jishuh:
                    y = jishuh * jishu_sum
                else:
                    y = x * jishu_sum
                a = x - 3500  # å·¥èµé«äº3500æèèç¼´ç¨
                h = x - y - 3500  # åºçº³ç¨æå¾é¢å¨æ£é¤ç¤¾ä¿åèµ·å¾ç¹ä¹åæè®¡ç®
                if a <= 0:
                    z = 0
                elif a <= 1500:
                    z = h*0.03
                elif a <= 4500:
                    z = h*0.10 - 105
                elif a <= 9000:
                    z = h*0.20 - 555
                elif a <= 35000:
                    z = h*0.25 - 1005
                elif a <= 55000:
                    z = h*0.30 - 2755
                elif a <= 80000:
                    z = h*0.35 - 5505
                else:
                    z = h*0.45 - 13505
                m = x - y - z
                result = []
                result = id, format(x, ".2f"), format(
                    y, ".2f"), format(z, ".2f"), format(m, ".2f")
                userdata_after_calc.append(result)
        q2.put(userdata_after_calc)

    def export(self, q2):
        # result = self.calc_for_all_userdata()
        output_file = Args().o
        with open(output_file, 'w') as file:
            for w in q2.get():
                writer = csv.writer(file)
                writer.writerows(w)


def main():
    Process(target=UserData()._read_user_data, args=(queue1,)).start()
    Process(target=IncomeTaxCalculator().calc_for_all_userdata, args=(queue2, queue1)).start()
    Process(target=IncomeTaxCalculator().export, args=(queue2,)).start()


if __name__ == '__main__':
   queue1 = Queue()
   queue2 = Queue()
   # args = Args()
   # config = Config().config
   # newdata = []
   main()

# if __name__ == '__main__':
#     # IncomeTaxCalculator()
#     IncomeTaxCalculator().export()

