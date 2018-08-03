import sys,getopt
class Args:
    def __init__(self):
        self.agrs = sys.argv[1:]
        opts,args = getopt.getopt(self.agrs,"c:d:o:")
        for option, value in opts:
            if option in ("-c"):
                configfile = value
                print(configfile)
            elif option in ("-d"):
                userdatafile = value
                print(userdatafile)
            elif option in ("-o"):
                outputfile = value


class Config(object):
    """docstring for Config"""
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        configfile = self.configfile
        with open(configfile,'r') as file:
            content = file.readlines()
            for line in content:
                v = line.strip().split(' = ')
                config[v[0]] = v[1]
        return config

config = Config()
config.config