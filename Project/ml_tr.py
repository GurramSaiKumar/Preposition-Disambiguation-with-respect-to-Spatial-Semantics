import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

total_vector=[]
class_att=[]
tr_cand=[]

with open("tr_finalfeatures.txt","r") as fp:
	features=list(fp)
 

feature_sent=[]
for i in features:
	feature_sent.append(i.strip('\n'))


for j in feature_sent:
	ind_feature=j.split()
	lm1=ind_feature[1]
	lm2=ind_feature[2]
	lm3=ind_feature[3]
	lm4=ind_feature[4]
	lm5=ind_feature[5]
	lm6=ind_feature[6]
	lm7=ind_feature[7]
	lm8=ind_feature[8]
	lm9=ind_feature[9]
	lm10=ind_feature[10]
	lm11=ind_feature[11]
	lm12=ind_feature[12]
	lm13=ind_feature[13]
	lm14=ind_feature[14]
	lm15=ind_feature[15]
	lm16=ind_feature[16]
	lm17=ind_feature[17]
	lm18=ind_feature[18]
	lm19=ind_feature[19]
	lm20=ind_feature[20]
	lm21=ind_feature[21]
	lm22=ind_feature[22]
	lm23=ind_feature[23]
	lm24=ind_feature[24]
	lm25=ind_feature[25]
	lm26=ind_feature[26]
	lm27=ind_feature[27]
	class_att.append(ind_feature[28])
	individual_vector=" ".join((lm1,lm2,lm3,lm4,lm5,lm6,lm7,lm8,lm9,lm10,lm11,lm12,lm13,lm14,lm15,lm16,lm17,lm18,lm19,lm20,lm21,lm22,lm23,lm24,lm25,lm26,lm27))
	# individual_vector=" ".join((lm1,lm2,lm3,lm4,lm5,lm6))
	total_vector.append(individual_vector)
	

vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000)

train_data_features = vectorizer.fit_transform(total_vector)
train_data_features = train_data_features.toarray()
vocab = vectorizer.get_feature_names()
dist = np.sum(train_data_features, axis=0)
forest = RandomForestClassifier(n_estimators = 100) 
forest = forest.fit(train_data_features,class_att)
    
    
with open("tr_finalfeatures_test.txt","r") as fp1:
	features1=list(fp1)  

feature_sent1=[]
for i in features1:
	feature_sent1.append(i.strip('\n'))

total_vector_test=[]
test_id=[]
for j in feature_sent1:
	ind_feature=j.split()
	id=ind_feature[0]
	lm1=ind_feature[1]
	lm2=ind_feature[2]
	lm3=ind_feature[3]
	lm4=ind_feature[4]
	lm5=ind_feature[5]
	lm6=ind_feature[6]
	lm7=ind_feature[7]
	lm8=ind_feature[8]
	lm9=ind_feature[9]
	lm10=ind_feature[10]
	lm11=ind_feature[11]
	lm12=ind_feature[12]
	lm13=ind_feature[13]
	lm14=ind_feature[14]
	lm15=ind_feature[15]
	lm16=ind_feature[16]
	lm17=ind_feature[17]
	lm18=ind_feature[18]
	lm19=ind_feature[19]
	lm20=ind_feature[20]
	lm21=ind_feature[21]
	lm22=ind_feature[22]
	lm23=ind_feature[23]
	lm24=ind_feature[24]
	lm25=ind_feature[25]
	lm26=ind_feature[26]
	lm27=ind_feature[27]
	individual_vector1=" ".join((lm1,lm2,lm3,lm4,lm5,lm6,lm7,lm8,lm9,lm10,lm11,lm12,lm13,lm14,lm15,lm16,lm17,lm18,lm19,lm20,lm21,lm22,lm23,lm24,lm25,lm26,lm27))
	# individual_vector1=" ".join((lm1,lm2,lm3,lm4,lm5,lm6))
	total_vector_test.append(individual_vector1) 
    
    
test_data_features = vectorizer.transform(total_vector_test)
test_data_features = test_data_features.toarray()
result = forest.predict(test_data_features)

id=[]
with open("tr_finalfeatures_test.txt","r") as fp2:
	x=fp2.readlines()
	for l in x:
		s=l.split()
		id.append(s[0])


op=open("tr_result.txt","w")
for j,i in zip(range(0,len(result)),id):
	print(i,result[j], file=op)
	

    
    
    
   
	# l=len(ind_feature)-1
	# cand_sent=ind_feature[0]
    
 #    
 #    
	#  
	# total_vector.append(individual_vector)
	



# vectorizer = CountVectorizer(analyzer = "word",   \
#                              tokenizer = None,    \
#                              preprocessor = None, \
#                              stop_words = None,   \
#                              max_features = 5000)
 
# train_data_features = vectorizer.fit_transform(total_vector)
# train_data_features = train_data_features.toarray()
#print train_data_features.shape
# vocab = vectorizer.get_feature_names()
# #print vocab                             #this prints the vocabulary count of each word
# dist = np.sum(train_data_features, axis=0)
# #for tag, count in zip(vocab, dist):
# #    print count, tag
# # Initialize a Random Forest classifier with 100 trees
# forest = RandomForestClassifier(n_estimators = 100) 

# # Fit the forest to the training set, using the bag of words as 
# # features and the sentiment labels as the response variable
# #
# # This may take a few minutes to run
# forest = forest.fit(train_data_features,class_att)       #upto this the model is trained
