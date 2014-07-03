# coding=utf-8
#!/usr/bin/env python

import configparser

import _mssql

__author__ = 'Will.H'


class DBConnector:
    ini = '../database/db.ini'

    def __init__(self, node):
        config = configparser.ConfigParser()
        config.read(self.ini)
        sub = config[node]
        self.conn = _mssql.connect(server=sub.get('server'), user=sub.get('username'), password=sub.get('password'),
                                   database=sub.get('database'))

    def exec_query(self, command, param):
        self.conn.execute_query(command, param)
        return self.conn

    def __del__(self):
        self.conn.close()
