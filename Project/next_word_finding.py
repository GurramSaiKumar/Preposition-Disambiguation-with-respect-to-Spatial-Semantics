with open('/home/sai/Downloads/setall.txt',"r") as fr:
	se=list(fr)
df1=open("differnt1.txt","w")
with open("/home/sai/Desktop/Project/lm_data.txt","r") as rd:
	for l in rd:
		tokens=l.split()
		a=int(tokens[0])-1
		list_of_words=se[a].split()
		next_word=list_of_words[list_of_words.index(tokens[1]) + 1]
		pre_word=list_of_words[list_of_words.index(tokens[1]) - 1]
		if next_word == '.':
			print("null",pre_word, file=df1)
		else:
			print(next_word,pre_word, file=df1)