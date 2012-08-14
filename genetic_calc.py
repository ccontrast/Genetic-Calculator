import re
import itertools

MORPH_DICT = {"bumblebee":["pastel", "spider"], "pastave":["mojave", "pastel"], "pastel":["pastel","normal"], "super pastel":["pastel", "pastel"]}

# checks what morphs you can breed with your current stock
# gender? -- will be important to check
def process_collection(collection):
    collection_list = re.findall(r'\w+', collection)
    for k,v in MORPH_DICT.items():
        common = list(set(v) & set(collection_list)
	if common == MORPH_DICT[k]:
            print "FOUND: ", k
	else:
	    print ("can't create %s") % k

# simple punnett square - calculates what traits may be present in offspring
# how do i deal with more than two traits? 
# for example -- super pastel can also be het while expressing a homo co-dom
def punnett_square(parents):
    return list(itertools.product(*parents))

# returns percentages for likelyhood of offspring expressing trait
def trait_percentage(parents):
    genes = punnett_square(parents)
    total = float(len(genes))
    for each in genes:
        percentage = (1/total) * 100
        print ("%s : %s %s") % (percentage, each[0], each[-1])

# combine with the morph dictionary to further define traits
# ie pastel pastel is super pastel, pastel mojave is pastave

p = [['pastel','het albino', 'normal'],['pastel','normal']]
c = "pastel, spider, normal"
print trait_percentage(p)