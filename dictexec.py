#!/usr/bin/python -tt

"""A tiny Python program to check
   practice dict oper
"""

import sys
import random
import string
import operator

def createdict(filename):
  f = open(filename,'r')
  dict01 = {}
  for line in f:
    oneline = line.split()
    dict01[oneline[1]] = oneline[0]
  f.close
  return dict01


def listdict(dictname):
  for line in dictname:
    print line, dictname[line]
  print 'list dict complete'
  return

def sortdictbykey(dictname):
#  newdict = sorted(dictname.items(),key=operator.itemgetter(1))
  newdict = sorted(dictname.items(), key=lambda tup:int(tup[1]))

  for line in newdict:
    print line
  return

def main():
  if len(sys.argv) >= 2:
    filename = sys.argv[1]
    dict01 = createdict(filename)
    listdict(dict01)
    sortdictbykey(dict01)
  
    
  else:
    print 'argv filename is required '


if __name__ == '__main__':
  main()
