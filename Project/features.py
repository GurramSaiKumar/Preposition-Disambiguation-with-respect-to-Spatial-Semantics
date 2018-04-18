import nltk
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
#a=lmtzr.lemmatize('plants')
#print(a)
count=0;

with open('/home/sai/Downloads/setall.txt',"r") as fr:
	se=list(fr)
df=open("differnt.txt","w")
with open("/home/sai/Desktop/Project/lm_data.txt","r") as rd:
	for line in rd:
		
		st=str(line)
		st1=st[2:len(st)]
		for i in st1.split():
			a=lmtzr.lemmatize(i)
			st2=nltk.word_tokenize(i)
			pos=nltk.pos_tag(st2)
		print(st[:2],a,pos, file=df)



		


