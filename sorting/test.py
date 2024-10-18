#rotate strings

name = "pradeep"
rotatedname = "deeepra"
concatedname = name + name
print (concatedname)
if len(name)!=len(rotatedname):
    print (False)
if rotatedname in concatedname:
    print(True)
else:
    print(False)