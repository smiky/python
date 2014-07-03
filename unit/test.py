# coding=utf-8
#!/usr/bin/python
__author__ = 'Will.H'

import unittest
import database.mssql as msdb


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_db(self):
        db = msdb.DBConnector('MSSQL')
        dt = msdb.DBConnector.exec_query(db, 'SELECT * FROM AccountProfile WHERE RoleId = %d', 2)
        for r in dt:
            print('Name is [%s], Password is [%s]' % (r['AccountName'], r['Password']))


if __name__ == '__main__':
    unittest.main()
