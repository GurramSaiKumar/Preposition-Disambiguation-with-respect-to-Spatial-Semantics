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
                tag_sent= nltk.pos_tag(text)
               # tag_sent=nltk.pos_tag(i)
                #tag_sent=rrp.tag(i)
                chunk=cp.parse(tag_sent)
                tree = chunk
                parse_sent=rrp.parse(i)
                for node in tree:
                    if type(node) is nltk.Tree:
                        if node.label()=='NP':
                            npnode=foo(node)
                            #a=str(npnode)
                            # npnode= nbest_list[0].ptb_parse
                            #npnode=str(nbest_list[0].ptb_parse)
                            npnew=nltk.Tree.fromstring(npnode,read_leaf=lambda x: x.split("/")[0])

                           # npnew=nltk.Tree.fromstring(npnode,read_leaf=lambda x: x.split("/")[0])

                            
                            sub_ind=0
                            #b=parse_sent[0].ptb_parse
                           # text = nltk.word_tokenize(b)
                            #c=list(text)
                             # subject indicator or rootNN indicator
                            #t=tree(parse_sent[0].ptb_parse)
                            
                            
                            for te in parse_sent[0].ptb_parse.sd_tokens():
                                if (te.deprel == 'nsubj') and (te.form==npnew.leaves()[-1]):
                                    sub_ind=1
                                if (te.deprel=='root') and (te.form==npnew.leaves()[-1]) and (te.cpos=='NN' or te.cpos=='NNS'):
                                    sub_ind=1
                            print(sent_count,npnew.leaves()[-1], file=ft)
                             #print(sent_count,",",npnew.leaves()[-1],sub_ind, file=ft)

           
                        if node.label()=='PP':
                            nodetemp=foo(node)
                     # print " ".join(nltk.Tree.fromstring(nodetemp,read_leaf=lambda x: x.split("/")[0]).leaves())
                            print(sent_count,node[0][0], file=fp)
                            node_new=foo(node[1])
                            node_new_mod=nltk.Tree.fromstring(str(node_new),read_leaf=lambda x: x.split("/")[0])
                            lm_ind=0
                            for w in parse_sent[0].ptb_parse.sd_tokens():
                                if w.form==node[0][0] and w.cpos=='IN': 
                                    dep_head=w.head
                                      
                                    for w1 in parse_sent[0].ptb_parse.sd_tokens():
                                        if (w1.index==dep_head) and (w1.cpos=='NN'or w1.cpos=='NNS' or w1.cpos=='PRP') and (w1.form==node_new_mod.leaves()[-1]):
                                            lm_ind=1
                                    print(sent_count,node_new_mod.leaves()[-1], file=fn)


fp.close()
fn.close()
fr.close()
