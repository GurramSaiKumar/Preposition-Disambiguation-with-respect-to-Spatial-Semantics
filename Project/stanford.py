import StanfordDependencies
sd = StanfordDependencies.get_instance(backend='subprocess')
penn_treebank_tree = str("Sun rises in the east") 
sd = StanfordDependencies.get_instance(jar_filename='point to Stanford Parser JAR file')