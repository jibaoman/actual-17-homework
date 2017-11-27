#!/usr/bin/env python
# -*- coding: UTF-8 -*-

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]

max_1st = list[0]
max_2nd = list[0]

for tmp in list:
    if tmp > max_1st:
        max_1st = tmp

for tmp in list:
    if tmp > max_2nd and tmp < max_1st:
        max_2nd = tmp

print 'the max_num is %s' %(max_1st)
print 'the sec_num is %s' %(max_2nd)
