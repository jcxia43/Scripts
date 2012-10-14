
#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def timing(func):
    def calc_time(*args, **kwargs):
        time_stamp = time.clock()
        res = func(*args, **kwargs)
        print "running time for %s() is: " % (func.__name__)
        print "%6.4f seconds" % (time.clock() - time_stamp)
        return res
    return calc_time
        
        
