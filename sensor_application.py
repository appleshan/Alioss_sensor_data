# -*- coding:utf-8 -*-#
"""
Created on Fri Aug 16 11:30:38 2017

@author: 刘睿

@mail:liurui@codoon.com

"""
from mysql.ssh_mysql2local import ssh_mysql
from visualization_application.analysis import dataprocess
from visualization_application.manualPlt import route_id_json

upload_data_key = "select data_key,route_id from sensor_data " \
                  "where update_time > '2017-08-17' " \
                  "and update_time < '2017-08-19' " \
                  "and user_id = 'da817769-429c-4f1a-b3f2-5184d01c08a2'"
                  #"and  user_id = '302c8c91-e3c2-42eb-b8cd-e65caa7739fc'"


mysql = ssh_mysql('sensor_sport')
size,rows = mysql.query(upload_data_key)

datapro = dataprocess()
r_json = route_id_json()

for row in rows:
    #print(row)
    user_dic = datapro.readfromstream(row[0])
    route_dic = r_json.getroute(row[1])

    phone = r_json.print_route(route_dic)

    datapro.plt_svm(user_dic,title=phone,is_all= True)
    print("----------------\n")

#datapro.show_plt()
