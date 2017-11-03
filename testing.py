from taklaGen import MuradTakla
import pickle,os
dict_path=os.getcwd()+"\\dictionary\\bdict.dat"

converter=MuradTakla()

with open(dict_path,"rb") as dfile:
    bdict=pickle.load(dfile)

for i in range(2,100,3):
    word=bdict[i]
    takla=converter.BanglaToTakla(word)
    print(word,":",takla)
    