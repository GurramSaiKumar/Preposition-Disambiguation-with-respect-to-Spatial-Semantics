import nltk
import StanfordDependencies
from nltk import word_tokenize
from bllipparser import RerankingParser
from nltk.tree import Tree
from bllipparser import RerankingParser, tokenize
rrp = RerankingParser.from_unified_model_dir('/home/sai/.local/share/bllipparser/WSJ-PTB3')
rrp.load_reranker_model('/home/sai/.local/share/bllipparser/WSJ-PTB3/reranker/features.gz', '/home/sai/.local/share/bllipparser/WSJ-PTB3/reranker/weights.gz')

with open('/home/sai/Downloads/setall.txt',"r") as fr:
    sents=list(fr)

for i in sents:

    nbest_list=rrp.parse(i)
    sents1=[]
    sents1+=nbest_list[0].ptb_parse.sd_tokens()
    for node in sents1:
        print('{}({}-{},{}-{})'.format(
            node.deprel,
            sents1[node.head - 1].form if node.head != 0 else 'ROOT',
            node.head,
            node.form,
            node.index))
    # print()





#npnew=nltk.Tree.fromstring(npnode,read_leaf=lambda x: x.split("/")[0])

# for te in sents1:
#     if (te.deprel == 'nsubj'):
#         print(sents1[te.head - 1].form if te.head != 0 else 'ROOT',te.form)

# list=[]
# df3=open("different2.txt","w")



# if sents1[0].form == 'About':
	# print("1")


# df2=open("different2.txt","w")
# for dep in sents1:

#    print(dep, file=df2)

      #dep_list.append(s[s.find(start)+len(start):s.rfind(end)])
      #print(dep_list)