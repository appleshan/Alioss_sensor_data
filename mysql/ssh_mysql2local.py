# -*- coding:utf-8 -*-#
"""
Created on Fri Aug 14 10:02:37 2017

@author: 刘睿

@mail:liurui@codoon.com
"""


import pymysql
from sshtunnel import SSHTunnelForwarder
from util.loadsconfig import config


white_user_id = "select * from white_user"
upload_data_key = "select data_key,update_time from sensor_data where update_time > '2017-08-16' and update_time < '2017-08-17' "

class ssh_mysql:

  def __init__(self,database):
      self.database = database
      tempc = config()
      self.ssh = tempc.get_config_by_key('ssh')
      self.mysql = tempc.get_config_by_key('mysql')
      self.connect()

  def connect(self):
    '''
    self.client = MySQLdb.connect(host=self.server, port=self.port, user=self.user,
                                  passwd=self.password, db=self.database,
                                  charset=self.charset)
    # log.info('Connect to MySQL Server: ' + self.server)
    '''

    tssh = self.ssh
    tmysql = self.mysql
    print(tssh)
    server = SSHTunnelForwarder(
        (tssh['ssh_ip'],tssh['ssh_port']),
        ssh_username=tssh['ssh_username'],
        remote_bind_address=(tmysql['mysql_ip'],tmysql['mysql_port'])
    )
    server.start()


    self.client = pymysql.connect(host='127.0.0.1',
                                  port=server.local_bind_port,
                                  user=tmysql['mysql_username'],
                                  passwd=tmysql['mysql_password'],
                                  db=self.database,
                                  charset='utf8'
                       )

    self.cursor = self.client.cursor()


  def query(self,sql):
        # 执行SQL，并返回收影响行数
        size = self.cursor.execute(sql)
        row = self.cursor.fetchall()

        return size,row

  def execute(self, sql):
      # 执行SQL，并返回收影响行数
      self.cursor.execute(sql)

  def close(self):
      self.cursor.close()
      # 关闭连接
      self.client.close()

def main():
    #ssh_mysql使用
    mysql = ssh_mysql('sensor_sport')
    size,rows = mysql.query(upload_data_key)

    for row in rows:
        print(row[0])

    print("size:%d" % size)
    print(row)

    mysql.close()


if __name__=='__main__':
    main()

