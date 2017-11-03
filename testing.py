from BanglishGen import Banglish
import pickle,os
dict_path=os.getcwd()+"\\dictionary\\bdict.dat"

converter=Banglish()

with open(dict_path,"rb") as dfile:
    bdict=pickle.load(dfile)

for i in range(2,100,3):
    words=bdict[i].split()
    for word in words:
        takla=converter.BanglaToBanglish(word)
        print(word,":",takla)
    
