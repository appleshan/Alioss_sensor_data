# -*- coding:utf-8 -*-#
"""
Created on Fri Aug 18 15:02:37 2017

@author: 刘睿

@mail:liurui@codoon.com
"""
import json


class config():

    def __init__(self,config_file = "config.json"):
        with open(config_file,'r') as f:
            self.configs = json.load(f)
        f.close()

    def get_config_by_key(self,key):
        return self.configs[key]

def main():

    c = config("../config.json")
    print(c.get_config_by_key('ssh'))


if __name__ == '__main__':
    main()


