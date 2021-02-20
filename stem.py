odia_text ='''କଲେଜରେ ଅଧ୍ୟାପନା କରୁଥୁଲେ ରାଧାକ୍ରିଷ୍ଣନ । ଶିଶୁ ପରି ସରଳ କିନ୍ତୁ ବଜ୍ରପରି କଠୋର । ଦର୍ଶନ ଶାସ୍ତ୍ର ଭଳି ଜଟିଳ
ବିଷୟକୁ ଏପରି ସରଳ ଭାବେ ବୁଝାଇ ପାରୁଥ୍ଲେ ଯେ ତାଙ୍କ କ୍ଲାସ୍‌ ବେଳେ ପାଖ କକ୍ଷର ପିଲାମାନେ ପାଠ ଶୁଣିବାକୁ
ଉଠି ଆସୁଥଲେ । ଚୁମ୍ବକ ଲୁହାକୁ ଟାଣେ, ଗୁଣିଆ ସୁନାକୁ ଜାଣେ । ରାଧାକ୍ରିଷ୍ଣନ ଡକ୍ଟରେଟ୍‌ ଲାଭ କଲେ । ମହୀଶୁର
ବିଶ୍ବବିଦ୍ୟାଳୟର ମୁଖ୍ୟ ଅଧ୍ଯାପକ ହେଲେ ! କଥା କମ୍‌ କହୁଥୁଲେ | କାମ ବେଶୀ କରୁଥୂଲେ | ମଣିଷକୁ ଦେବତା ପରି
ଭଲ ପାଉଥ୍‌ଲେ । ଛାତ୍ରମାନଙ୍କ ସହିତ ଆତ୍ମୀୟ ପରି ମିଶୁଥୂଲେ | IAMGOING YUO'''
from nltk.tokenize import sent_tokenize,word_tokenize
tokenized_text=sent_tokenize(odia_text)
print(tokenized_text)
tokens=word_tokenize(odia_text)
print(tokens)
#def word_tokenize(odia_text,language="odia",preserve_line=False)
#for w word_tokenize(odia_text):
 #   print(w)
from nltk.stem import PorterStemmer
ps = PorterStemmer()
#def prepare_odia_text(odia):
    
    tokens=word_tokenize(odia_text)
    for word in tokens:
    print(word," : ", ps.stem(word))
    

