#!/usr/bin/env python
# -*- coding: UTF-8 -*-

for i in range(1,10):
    for j in range(1,10):
        if i >= j:
            print '%s x %s = %s\t' %(i,j,i*j),
    print '\n'
