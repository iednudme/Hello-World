#!/usr/bin/python -tt
'''this is test string py, open a file and make a list of string, then 
   test string functions '''

import sys

def createlist(filename):
  newlist = []
  f = open(filename,'r')
  for line in f:
    linelist = line.split()
    newlist.append(linelist[1])
  f.close()
  return  newlist


# test startswith 

def teststring(listname):
  for line in listname:
    #print line
    if line.startswith('S'):
      print 'I found this ', line
    #else:
      #print 'not found '
  return
  
def main():
  mynewlist = []
  if len(sys.argv) >= 2:
    name = sys.argv[1]
    teststring(createlist(name))
    
  else:
    name = 'test'
    print 'usage : cli filename', name

if __name__ == '__main__' :
  main()
