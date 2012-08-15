from __future__ import division
import re
import itertools


MORPH_DICT = {"bumblebee":["pastel", "spider"], "pastave":["mojave", "pastel"], "pastel":["pastel","normal"], "super pastel":["pastel", "pastel"]}

# checks what morphs you can breed with your current stock
# gender? -- will be important to check
# def process_collection(collection):
#     collection_list = re.findall(r'\w+', collection)
#     for k,v in MORPH_DICT.items():
#         common = list(set(v) & set(collection_list)
#         if common == MORPH_DICT[k]:
#             print "FOUND: ", k
#         else:
#             print ("can't create %s") % k

# simple punnett square - calculates what traits may be present in offspring
# how do i deal with more than two traits? 
# for example -- super pastel can also be het while expressing a homo co-dom
def punnett_square(parents):
    return list(itertools.product(*parents))

# returns percentages for likelyhood of offspring expressing trait
def trait_percentage(parents):
    genes = [list(i) for i in punnett_square(parents)]
    total = float(len(genes))
    count = {}
    for traits in genes:
        traits.sort()
        traits = tuple(traits)
        count[traits] = count.get(traits,0) + 1
    for k,v in count.items():    
        percentage = (count[k]/total) * 100
        print ("%s%% : %s") % (percentage, k)

# combine with the morph dictionary to further define traits
# ie pastel pastel is super pastel, pastel mojave is pastave

# p = [['pastel', 'het albino'],['pastel','normal']]
p = [['normal', 'normal', 'het albino'], ['normal', 'normal']]
c = "pastel, spider, normal"
d = {"trait1":[['A', 'a'],['A', 'a']], "trait2":[['B', 'b'], ['b', 'b']]}
trait_percentage(p)