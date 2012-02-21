import os, glob, string

def FileList(path):
    return glob.glob(path+"/*.txt")

def CheckForN(line):
    if string.find(line,"Sex: N") == -1 :
      return False
    else :
      return True  

def FixFile(fname,i) :
    F = open(fname)   
    lines = F.readlines()
    F.close()
    lines[i] = "Sex: M\n"; 
    F = open(fname,'w')
    for line in lines :
        F.write(line)    
    F.close()  

Flist = FileList('cleandata')
for Fname in Flist :
    F = open(Fname)
    lines = F.readlines()
    for i in range(len(lines)):
        if CheckForN(lines[i]) :
             print Fname, lines[i]
             FixFile(Fname,i)
             break
    F.close()
 

