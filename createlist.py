#!/usr/bin/python -tt

"""A tiny Python program to check
"""

import sys
import random
import string

def createlist(filename):
  f = open(filename,'w')
  for i in range(20):
    ran1 = random.choice(string.letters)
    ran2 = random.choice(string.letters)
    ran3 = random.choice(string.letters)
    ranw = str(i) + ' ' + ran1 + ran2 + ran2 + ran3
    f.write(ranw)
    f.write('\n')
  f.close
  

def main():
  if len(sys.argv) >= 2:
    filename = sys.argv[1]
    createlist(filename)
    
  else:
    print 'argv filename is required '


if __name__ == '__main__':
  main()
