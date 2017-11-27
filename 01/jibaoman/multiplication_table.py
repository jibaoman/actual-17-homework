#!/usr/bin/env python
for i in range(1,10):
    for j in range(1,10):
        if i >= j:
            print "%s * %s=%s" %(i,j,i*j),
    print '\n'
