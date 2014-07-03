# coding=utf-8
#!/usr/bin/python
__author__ = 'Will.H'
import sys
import platform


class IO:
    def __init__(self, name):
        self.name = name

    def write(self, content):
        try:
            if platform.python_version().startswith('3'):
                fn = open(self.name, "w", newline='')
            else:
                fn = open(self.name, "w")
            fn.writelines(content)
        except IOError as err:
            print("I/O error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        finally:
            fn.close()

    def __del__(self):
        self.name = ''

    def __str__(self):
        return '{0} file was be generated!'.format(self.name)