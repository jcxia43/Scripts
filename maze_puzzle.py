#!/usr/bin/python
# -*- coding: utf-8 -*-

# puzzle source:  http://weibo.com/1915548291/z4eTPtAnv 
# solution : Breadth-First Search
# The total idea is making every status a tuple ( No. status, operation, value), which is a 
# basic element in a path. A path is a combination of amount of choices of status, of which 
# length is related to current depth the program goes. Paths list is a collection of all 
# possible paths under current depth. Cutting branches is extremely important for improve 
# the efficiency of this script.


from timing import *

ADD, SUB, MUL, DIV = (0, 1, 2, 3) # denote four operations
# status map of the whole maze
MAP = {
   1:[(2,ADD), (2,DIV)],
   2:[(1,ADD), (1,DIV), (3,MUL), (3,SUB)],
   3:[(2,MUL), (2,SUB)]
}

def parse_path(path, value):
   '''
   parse the path and return the relative expression
   Eg of path:
     [(1, -1, 132), (2, ADD, 139), (4, DIV, 69)]
   return the parse result:
     ((value+7)÷2)
   '''
   # for constructing the expression string
   OPLIST = ['+7)', '-5)', '*3)', '/2)']
   # get the second column of the path, which should be a list of operations
   ops = list(zip(*path)[1])
   # eliminate the first -1 which means nothing
   ops.pop(0)
   # exp = '((((...(value'
   exp = '(' * len(ops) + str(value)
   for op in ops:
      exp += OPLIST[op]         
   return exp

@timing
def solve(start, end):
   paths = [[(1, -1, start)]]                # initial path is [(1, -1, start_value)]
   result = {}                               # 
   depth = 0                                 # storing depth
   while True:                               # Broadth-first search
      depth += 1                             # go further
      new_paths = []                         # temp for storing new_paths
      for path in paths:                     # walk all path and get new paths
         status = path[-1][0]
         value = path[-1][2]
         for branches in MAP[status]:        # all branches under current status
            new_status, op = branches
            new_value = eval('(' + str(value) + OPLIST[op]) # get the value
            new_path = path + [(new_status, op, new_value)] # new path
            if new_value == end and new_status is 3 and op != path[-1][1]: # terminate condition
               return parse_path(new_path, start) 
            if (new_value,op) not in result.get(new_status,[]) and new_value <= 6000 and op != path[-1][1]: # cutting branches
               if result.get(new_status) is None:
                  result[new_status] = []
               result[new_status].append((new_value, op)) # new value in new status, update result
               new_paths.append(new_path)
      paths = new_paths
      print 'depth: %d, nbr_paths: %d' % (depth, len(paths))
print solve(2011,2012)
    
    

