# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:34:30 2017

@author: 刘睿

@mail:liurui@codoon.com
"""


import oss2
import json
from util.loadsconfig import config



class ossmanager():
   def __init__(self):
        tempc = config()
        toss = tempc.get_config_by_key('oss')
        self.id = toss['oss_id']
        self.key = toss['oss_key']
        self.endpoints = toss['endpoints']
        self.bucket = toss['bucket']


   def connect(self):

       bucket = oss2.Bucket(oss2.Auth(self.id, self.key), self.endpoints, self.bucket, enable_crc=False)
       return bucket



def main(_):
    oss = ossmanager()
    bucket = oss.connect()
    key = '302c8c91-e3c2-42eb-b8cd-e65caa7739fc/2017-08-17T19:57:17.752/origin_43_3695887798'
    #print(bucket.get_object(key).read())
    print json.load(bucket.get_object(key))
    print "ok"

if __name__ == '__main__':

    main(1)

