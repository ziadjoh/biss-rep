from sys import getsizeof
from pickle import dumps,loads
global b
global tnum
global tnom
global tprenom
b=4
tnum = 10
tnom = 20
tprenom = 20
tetud = tnum+tnom+tprenom+1
tenrg ='#'*tetud
tbloc=[0, [tenrg]*b]
blocsize=getsizeof(dumps(tbloc))+len(tenrg)*(b-1)+(b-1)
print(blocsize)
def ecrirebloc(file,i,buf):
    dp=2*getsizeof(dumps(0))+i*blocsize
    file.seek(dp,0)
    file.write(dumps(buf))
