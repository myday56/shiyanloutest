import sys
import csv


class Args:
    def __init__(self):
        self.args = sys.argv[1:]

    def get_args(self):
        if self.args[0] == '-c' and self.args[2] == '-d' and self.args[4] == '-o':
            conf_file = self.args[1]
            user_data_file = self.args[3]
            gongzi_file = self.args[5]
        else:
            print('Error')
        return conf_file, user_data_file, gongzi_file

class Config:
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        conf_file = Args().get_args()[0]
        with open(conf_file, 'r') as file:
            content = file.readlines()
            for line in content:
                v = line.strip().split(' = ')
                config[v[0]] = v[1]
        return config


class UserData:
    def __init__(self):
        self.userdata = self._read_user_data()

    def _read_user_data(self):
        userdata = []
        user_data_file = Args().get_args()[1]
        with open(user_data_file, 'r') as file:
            content = file.readlines()
            for line in content:
                v = line.strip().split(',')
                userdata.append(v)
        return userdata

class IncomeTaxCalculator:
    def calc_for_all_userdata(self):
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
        for i in range(userdata_list_len):
            id = userdata_list[i][0]
            num = userdata_list[i][1]
            try:
                x = float(num)  # 工资
            except ValueError:
                print("Parameter Error")
            else:
                if x <= jishul:  # 如果工资低于社保基数
                    y = jishul * jishu_sum
                elif x >= jishuh:
                    y = jishuh * jishu_sum
                else:
                    y = x * jishu_sum
                a = x - 3500  #工资高于3500才考虑缴税
                h = x - y - 3500  #应纳税所得额在扣除社保和起征点之后才计算
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
        return userdata_after_calc

    def export(self,default='csv'):
        result = self.calc_for_all_userdata()
        output_file = Args().get_args()[2]
        with open(output_file,'w') as file:
            writer = csv.writer(file)
            writer.writerows(result)

if __name__ == '__main__':
    # IncomeTaxCalculator()
    IncomeTaxCalculator().export()
