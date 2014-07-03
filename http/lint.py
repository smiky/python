# coding=utf-8
#!/usr/bin/env python

import json
import xml.etree.ElementTree as xmlET

import requests

import utils.io as cio

__author__ = 'Will.H'


def main():
    tree = xmlET.parse('unit.xml')
    root = tree.getroot()
    for item in root:
        url = item.find('url').text
        user = ''
        dt = {}
        for e in list(item.find('element')):
            dt[e.tag] = e.text
            if e.tag == 'u':
                user = e.text
        header = {'Content-type': item.get('type'), 'Accept': 'text/plain'}
        if item.find('method').text == 'POST':
            if item.find('auth-user') is None:
                r = requests.post(url, data=json.dumps(dt), headers=header)
            else:
                r = requests.post(url, data=json.dumps(dt), headers=header,
                                  auth=(item.find('auth-user').text, item.find('auth-pass').text))
        else:
            if item.find('auth-user') is None:
                r = requests.get(url, params=json.dumps(dt))
            else:
                r = requests.get(url, params=json.dumps(dt),
                                 auth=(item.find('auth-user').text, item.find('auth-pass').text))
        h = cio.IO(user + '.json')
        cio.IO.write(h, r.text)
        print(h)


if __name__ == '__main__':
    print('The App Create By %s' % __author__)
    main()