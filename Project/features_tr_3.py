import nltk
import StanfordDependencies
from nltk import word_tokenize
from bllipparser import RerankingParser
from nltk.tree import Tree
from bllipparser import RerankingParser, tokenize

rrp = RerankingParser.from_unified_model_dir('/home/sai/.local/share/bllipparser/WSJ-PTB3')
rrp.load_reranker_model('/home/sai/.local/share/bllipparser/WSJ-PTB3/reranker/features.gz', '/home/sai/.local/share/bllipparser/WSJ-PTB3/reranker/weights.gz')
#sd = StanfordDependencies.get_instance(backend='subprocess')


with open('/home/sai/Downloads/setall.txt',"r") as fr:
    sents=list(fr)

grammar = r"""
  NP:         
      {<PRP>}
      {<RB>?<DT>?<JJ>*<NN>+}  # Chunk sequences of DT, JJ, NN
      {<DT>?<JJ>*<NN>+}
      #{<CD><NNS>+}
      {<RB>?<CD>?<NNS>+}
      {<NP>?<CC>?<NP>}
      
      

  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  PPing: {<PP><VPing>}

  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
      {<VBD><VBN>}
      {<VB>|<VBP>}
      {<VBZ>}
      {<VBD><PPing>}
      
  VPing: 
      {<VBG>}

  CLAUSE: {<NP><VP>}         # Chunk NP, VP
  """

def foo(s):
    return str(s)
 

d={}
years_dict = dict()
with open("tr_data.txt","r") as op1:
  for l in op1:
    tok=l.split()
    if tok[0] in years_dict:

        # append the new number to the existing array at this slot
        years_dict[tok[0]].append(tok[1])
    else:
        # create a new array in this slot
        years_dict[tok[0]] = [tok[1]]

 
# for i in years_dict[str(count)]:
#   print(i)
lis=[]
lis.append("advomd")
lis.append("nummod")
lis.append("nsubj")
lis.append("case")
lis.append("amod")
lis.append("nmod")
lis.append("cc")
lis.append("conj")
lis.append("root")
lis.append("nmod")
lis.append("punct")
lis.append("det")
lis.append("nsubjpass")
lis.append("mark")
lis.append("aux")
lis.append("auxpass")
lis.append("neg")
lis.append("ccomp")
lis.append("compound:prt")
lis.append("compound")
lis.append("dobj")
lis.append("parataxis")
df3=open("features_tr_3.txt","w")
count=1  
for i in sents:
  flag=1
  parse_sent=rrp.parse(i)
  sents1=[] 
  sents1+=parse_sent[0].ptb_parse.sd_tokens()
    # print(sents1)
    
  # for io in years_dict[str(count)]:
  #   print(io)
  # count=count+1
  
  for io in years_dict[str(count)]:
    for l in lis:
      f=0
      for node in sents1:
        if (node.deprel == l) and ((sents1[node.head - 1].form if node.head != 0 else 'ROOT') == io):
          f=1
          print("1", end = " ", file=df3)
      if not f:
        print("0", end = " ",file=df3)
    print(file=df3)
  count=count+1

      
        
          
           
          
            
      
    