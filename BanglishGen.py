#-*- coding: utf-8-*-
class Banglish(object):
    def __init__(self):
        self.chardict={'ষ্ঞ': 'shn', 'দ্ধ': 'ddh', 'ন্ধ': 'ndh', 'ক্ষ': 'kkh', 'ঞ্জ': 'ngj','ঙ্গ': 'ngg','ঋ': 'ri', 'জ্ঞ': 'gg', 'ঢ়': 'r', 'ক্ত': 'kt', 'ব্দ': 'bd', 'ট্ট': 'tt', 'স্ম': 'sm', 'গ্ন': 'gn', 'ন্দ': 'nd', 'ং': 'ng', 'ৎ': 'th', 'ভ': 'v', 'ষ': 's', 'শ': 'sh', 'ফ': 'f', 'ঢ': 'dh', 'ঠ': 'th', 'ধ': 'dh', 'থ': 'th', 'ঙ': 'ng', 'ঞ': 'ng', 'ঘ': 'gh', 'ন্ত': 'nt', 'ঝ': 'jh', 'খ': 'kh', 'ছ': 'ch', 'ঔ': 'ou', 'ঐ': 'oi', 'অ': 'o', 'আ': 'a', 'ই': 'i', 'ঈ': 'i', 'উ': 'u', 'ঊ': 'u', 'এ': 'e', 'ও': 'o', 'ক': 'k', 'গ': 'g', 'চ': 'ch', 'জ': 'j', 'ট': 't', 'ড': 'd', 'ণ': 'n', 'ত': 't', 'দ': 'd', 'ন': 'n', 'প': 'p', 'ব': 'b', 'ম': 'm', 'য': 'z', 'র': 'r', 'ল': 'l', 'স': 's', 'হ': 'h', 'ড়': 'r', 'য়': 'y'}
        self.vioel={'ি':'i','া': 'a', 'ী': 'i', 'ু': 'u', 'ূ': 'u', 'ৃ': 'rri', 'ে': 'e', 'ৈ': 'oi', 'ো': 'o', 'ৌ': 'ou'}
        self.vioel2="aeiou"
        self.homoPhone={"sh":"s","z":"j","rri":"ri","z":"y","okse":"khe","kso":"kho","bzo":"ba","zogz":"zogg"}
        
    def BanglaToBanglish(self,word):
        word=self.__correction(word)
        vioelSwitch=0
        taklaWord=""
        for char in word:
            if char in self.chardict:
                taklaWord+=self.chardict[char]
                if self.chardict[char] not in self.vioel2:
                    vioelSwitch=1
            elif char in self.vioel:
                if taklaWord[-1:]=='o':
                    taklaWord=taklaWord[:-1]
                taklaWord+=self.vioel[char]
            if vioelSwitch==1:
                taklaWord+="o"
                vioelSwitch=0
            if char=="্":
                taklaWord=taklaWord[:-1]
        if taklaWord[-1:]=="o":
            taklaWord=taklaWord[:-1]
        if taklaWord[0]==taklaWord[1]:
            taklaWord=taklaWord[1:]
        version=self.__homoPhone_version(taklaWord)
        if version!=taklaWord:
            return version
        return [taklaWord]

    def __correction(self,word):
        need_to_correct=["্ব", "্ম"]
        corrected_word=""
        for item in need_to_correct:
            word=word.replace(item,"*")
        for char in word:
            if char=="*":
                char="্"+word[word.index("*")-1]
            corrected_word+=char
        return corrected_word
    
    def __homoPhone_version(self,word):
        version=[]
        for key in self.homoPhone:
            temp=word.replace(key,self.homoPhone[key])
            if temp not in version:
                version.append(temp)
        return version


if __name__=="__main__":
    test="কবিতা, এক যে ছিল মজার দেশ সব রকমের ভাল রাত্তিরেতে বেজায় রোদ দিনে চাদের আলো আকাশ সেথা সবুজবরণ গাছের পাতা নীল ডাঙ্গায় চরে রুই কাতলা জলের মাঝে চিল"
    dictionary=Banglish()
    for word in test.split():
        banglish_word=dictionary.BanglaToBanglish(word)
        print(banglish_word)
        
