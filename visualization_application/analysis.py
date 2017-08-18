# -*- coding:utf-8 -*-#
"""
Created on Fri Aug 15 16:05:30 2017

@author: 刘睿

@mail:liurui@codoon.com
"""

import json
import os
import numpy as np
import  matplotlib.pyplot as plt
from oss.ossopeations import ossmanager



class dataprocess(object):

    def __init__(self):
        oss = ossmanager()
        self.bucket = oss.connect()

    def maybe_downloads(directory,filename,self):
        direc= 'data'+os.path.sep+ directory
        if not os.path.exists(direc):
            os.mkdir(direc)
        bucket =self.bucket
        bucket.get_object_to_file(directory, direc)

    def readfromdata(self,directory):
        with open(directory, 'r') as f:
            self.data = json.load(f)

    def readfromstream(self,direct):
        bucket = self.bucket
        stream = bucket.get_object(direct)
        return json.load(stream)


    def get_sensor(self,datas):
        gsensor = np.array(datas['gs_points'])
        return gsensor[:,0],np.array(gsensor[:,1]),np.array(gsensor[:,2]),np.array(gsensor[:,3])


    def plt_svm(self,datas,title='svm',l=100,r=1000,is_all=False):

        time, x, y, z = self.get_sensor(datas)
        print('gensor点个数: %d' %len(time))
        time = time/1000.0
        svm = (x ** 2 + y ** 2 + z ** 2) / 1e8
        if is_all:
            plotimage(title, time, svm)
        else:
            plotimage(title, time[l:r], svm[l:r])

    def show_plt(self):
        showplt()


def plotimage(title,x,y):
    plt.figure(title)
    plt.plot(x,y)
    plt.show()

def showplt():
    plt.show()



def main():
    dataset = dataprocess()
    dataset.readfromdata()
    time,x,y,z = dataset.get_sensor()
    time=(time-time[0])/1000.0
    svm = (x**2+y**2+z**2)/1e8
    l=500
    r=200000
    print(len(time))
    plotimage('svm',time[l:r],svm[l:r])
    print(svm)
    print(time[1])


if __name__ == "__main__":
    main()


###
