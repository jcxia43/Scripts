#!/usr/bin/python
# -*- coding: utf-8 -*-

# Capitalize all the filename in the directory

import os
import sys
def capitalize_filename(dirname):
    """
    Capitalize all filename in the dirname
    Arguments:
    - `dirname`: directory name
    """
    for root, dirs, files in os.walk(dirname):
        os.chdir(root)
        for filename in files:
            print 'rename file: %s/%-20s \t to \t %s/%s' % (root, filename, root, filename.upper())
            os.rename(filename, filename.upper())
    print 'FINISHED'

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print 'Usage: capitalize directory_name'
    else:
        capitalize_filename(sys.argv[1])
    






