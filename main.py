import os, glob, string

def FileList(path):
    return glob.glob(path+"/*.txt")

def CheckForN(line):
    if string.find(line,": N") == -1 :
      return False
    else :
      return True  

def FixFile(fname) :
    F = open(fname)   
    lines = F.readlines()
    F.close()
    F = open(fname,'w')
    for line in lines :
        if not CheckForN(line) :
            F.write(line)
        else :
            F.write("Sex: M\n")
    F.close()  

Flist = FileList('cleandata')
for Fname in Flist :
    F = open(Fname)
    for line in F :
        if CheckForN(line) :
             print Fname, line
             FixFile(Fname)
             break
    F.close()
 

