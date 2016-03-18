#! /usr/bin/python -tt
import sys
import os
import commands

def dirtest(dirname):
  print os.listdir(dirname)
  for name in os.listdir(dirname):
    path = os.path.join(dirname, name)
    print path
    print os.path.abspath(path)
  return 

def listdir(dirname):
  cmd = ''
  cmd = 'ls -l ' + dirname
  print cmd
  print 'abot to to this : ' , cmd

  (status, output) = commands.getstatusoutput(cmd)
  if status: 
    sys.stderr.write('there was an error:' + output)
    sys.exit(1)
  print output
  return

def main():
  if len(sys.argv) < 2 :
    print " usage cli  dir "
    sys.exit(1)
  else: 
    dirname = sys.argv[1]
    #dirtest(dirname)
    listdir(dirname)

if __name__ == '__main__' :
  main()
