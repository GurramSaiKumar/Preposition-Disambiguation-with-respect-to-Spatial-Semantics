with open('/home/sai/Downloads/setall.txt',"r") as fr:
	se=list(fr)
import nltk
from nltk import pos_tag, word_tokenize
df1=open("differnt1.txt","w")
with open("/home/sai/Desktop/Project/lm_data.txt","r") as rd:
	for l in rd:
		tokens=l.split()
		a=int(tokens[0])-1
		list_of_words=se[a].split()
		next_word=list_of_words[list_of_words.index(tokens[1]) + 1]
		pre_word=list_of_words[list_of_words.index(tokens[1]) - 1]
		if next_word == '.' or next_word == ',':
			t=word_tokenize(pre_word)
			tagd=nltk.pos_tag(t)
			tags =  [ e[1] for e in tagd]
			print("null","null",pre_word,','.join(tags), file=df1)
		elif pre_word == '.' or pre_word == ',':
			t1=word_tokenize(next_word)
			tagd1=nltk.pos_tag(t1)
			tags1 =  [ e[1] for e in tagd1]
			print(next_word,', '.join(tags1),"null","null", file=df1)
		else:
			t3=word_tokenize(next_word)
			t4=word_tokenize(pre_word)
			tagd2=nltk.pos_tag(t3)
			tagd3=nltk.pos_tag(t4)
			tags3 =  [ e[1] for e in tagd2]
			tags4 =  [ e[1] for e in tagd3]
			print(next_word,','.join(tags3),pre_word,', '.join(tags4), file=df1)