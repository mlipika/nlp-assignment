import nltk
import odia
from wordsDic
suffixes={'ରେ','ଥିଲେ','କୁ','ଥଲେ'}


def hi_stem(word, clean=False,chars=None):
    if clean == True:
        word = clean_text(word, chars)

    ans = word
    bl = False

    if word in wordsDic.keys():
        return wordsDic[word]

   for L in 3:
            for suf in suffixes[L]:
                if word.endswith(suf):
                    ans = word[:-L]
                    bl =True
        if bl == True:
            break

   

    return ans