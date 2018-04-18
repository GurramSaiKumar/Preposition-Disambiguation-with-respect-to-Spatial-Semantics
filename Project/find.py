import nltk
import pprint
import StanfordDependencies
import sys
#import xlrd 
import re
#import xlsxwriter
#import xlwt
from nltk import word_tokenize
from bllipparser import RerankingParser
from bllipparser import RerankingParser, tokenize
from nltk.tree import Tree
rrp = RerankingParser.from_unified_model_dir('/home/sai/.local/share/bllipparser/WSJ-PTB3')
rrp.load_reranker_model('/home/sai/.local/share/bllipparser/WSJ-PTB3/reranker/features.gz', '/home/sai/.local/share/bllipparser/WSJ-PTB3/reranker/weights.gz')


sents=[]
def foo(s1):                           #function for adding '' to the beginning and end of string i.e parsed output
 return "%s" % s1 

'''book1 = xlwt.Workbook(encoding="utf-8")
traj_sheet=book1.add_sheet("Sheet 1")
spind_sheet=book1.add_sheet("Sheet 2")
landmark_sheet=book1.add_sheet("Sheet 3")'''

'''book = xlrd.open_workbook("/home/sandeep/CLEF PROGRAMS/train.xlsx",on_demand = True)       #this line will open sheet from the excel workbook
sent_sheet=book.sheet_by_index(1)
for row in range(sent_sheet.nrows):
 row=row+1
 if row<sent_sheet.nrows:
  sent_in=str(sent_sheet.cell(row,0).value)
  sents.append(sent_in)'''

'''book.release_resources()
del book'''

#with open('/home/sai/Downloads/setall.txt'',"r") as fr:
with open('/home/sai/Downloads/setall.txt',"r") as fr:
 sents=list(fr)

'''workbook1=xlsxwriter.Workbook('features.xlsx') # for writing the features
traj_sheet=workbook1.add_worksheet()   
spind_sheet=workbook1.add_worksheet() 
landmark_sheet=workbook1.add_worksheet()'''


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


with open('lm_data.txt',"w") as fn:
 with open ('si_data.txt', "w") as fp:
  with open ('tr_data.txt', "w") as ft:
   in_list=[]
   cp = nltk.RegexpParser(grammar)
   sent_count=0
   row=0
   for i in sents:
    pp_node=[]
    sent_count+=1
    text = word_tokenize(i)
    parse_sent= nltk.pos_tag(text)
               # tag_sent=nltk.pos_tag(i)
                #tag_sent=rrp.tag(i)
    chunk=cp.parse(parse_sent)
    tree = chunk
    #parse_sent=rrp.parse(i)
    for node in tree:
     if type(node) is nltk.Tree:
      if node.label()=='NP':
        npnode=foo(node)
        npnew=nltk.Tree.fromstring(npnode,read_leaf=lambda x: x.split("/")[0])
        parse_sent=rrp.parse(i)
        sub_ind=0                # subject indicator or rootNN indicator
        for te in parse_sent[0].ptb_parse.sd_tokens():
          if te.deprel=='nsubj' and te.form==npnew.leaves()[-1]:
           sub_ind=1
          if te.deprel=='root' and te.form==npnew.leaves()[-1] and (te.cpos=='NN' or te.cpos=='NNS'):
           sub_ind=1
        print(sent_count,","," ".join(npnew.leaves()),npnew.leaves()[-1],sub_ind, file = ft)
      
      if node.label()=='PP':
        nodetemp=foo(node)
       # print " ".join(nltk.Tree.fromstring(nodetemp,read_leaf=lambda x: x.split("/")[0]).leaves())
        print(sent_count,",",node[0][0], file = fp)
        node_new=foo(node[1])
        node_new_mod=nltk.Tree.fromstring(node_new,read_leaf=lambda x: x.split("/")[0])
        lm_ind=0
        for w in parse_sent[0].ptb_parse.sd_tokens():
         if w.form==node[0][0] and w.cpos=='IN': 
           dep_head=w.head
          
        for w1 in parse_sent[0].ptb_parse.sd_tokens():
         if (w1.index==dep_head) and (w1.cpos=='NN'or w1.cpos=='NNS' or w1.cpos=='PRP') and (w1.form==node_new_mod.leaves()[-1]):
           lm_ind=1          

        print(sent_count,","," ".join(node_new_mod.leaves()),node_new_mod.leaves()[-1],lm_ind, file = fn)
       





        '''if npnew.leaves():
         tr_length=len(str(" ".join(npnew.leaves())))
        if node_new_mod.leaves():
         lm_length=len(str(" ".join(node_new_mod.leaves())))
        if tr_length>0:
         traj_sheet.write_string(row, col," ".join(npnew.leaves()))
         traj_sheet.write_string(row, col+1,str(sent_count))
        col=0
        spind_sheet.write_string(row,col,node[0][0])
        spind_sheet.write_string(row, col+1,str(sent_count))
        col=0
        if lm_length>0:
         landmark_sheet.write_string(row, col," ".join(node_new_mod.leaves()))
         landmark_sheet.write_string(row, col+1,str(sent_count))
        row+=1 
#book1.save("features.xls")     
workbook1.close()  '''

fp.close()
fn.close()
fr.close()
 

'''        if (sub_ind==1 and lm_ind==1):
         print " ".join(npnew.leaves()),node[0][0]," ".join(node_new_mod.leaves())
        if (sub_ind==1 and lm_ind==0):
         print " ".join(npnew.leaves()),node[0][0]
        if (sub_ind==0 and lm_ind==1):
         print node[0][0]," ".join(node_new_mod.leaves())'''
 


'''with open ('np_data.txt', "r") as f3:
  text1 = f3.read()
  np_sents=nltk.sent_tokenize(text1)
  for line in np_sents:
   print line'''

def foo(s):
 return "%s",s












