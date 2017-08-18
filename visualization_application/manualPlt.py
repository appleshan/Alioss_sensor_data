# -*- coding:utf-8 -*-#
"""
Created on Fri Aug 16 11:30:38 2017

@author: 刘睿

@mail:liurui@codoon.com

"""

from visualization_application.analysis import dataprocess
import urllib2
import json
from util.loadsconfig import config


class route_id_json:

    def __init__(self):
        tempc = config()

        self.head=tempc.get_config_by_key("route_head")

    def getroute(self,id):
        json_id = urllib2.urlopen(self.head + id)
        # print(json_id)
        return json.load(json_id, encoding='utf-8')

    def print_route(self,route):
        phone = route['data']['model']
        print("phone:" + phone)
        if phone.find('iPhone') ==-1:
            print("时间:%d " % (route['data']['TotalTime'] / 1000.0))
        else:
            print("时间:%d " % (route['data']['total_time'] / 1000.0))
        print('距离:%f 米' % route['data']['total_length'])
        nc =route['data']['user_info']['nick']
        print('昵称: ')
        print(nc)
        return phone


def main():
    datapro = dataprocess()
    with open('data/road_id.txt', 'r') as f:
        temp = f.read().split("\n")
        user_dic = datapro.readfromstream(temp[0])
        r_json = route_id_json()
        route = r_json.getroute(user_dic['route_id'])
        r_json.print_route(route)
        datapro.plt_svm(user_dic,is_all= True)
    f.close()


if __name__ == "__main__":
    main()