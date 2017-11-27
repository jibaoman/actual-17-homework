#!/usr/bin/env python
# -*- coding:utf-8 -*-
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]
max1=list[0]
max2=list[0]
for i in list:
    if i > max1:
        max1 = i

for j in list:
    if j > max2 and j < max1:
        max2 = j

print "max number %s" %max1
print "second number %s" %max2
