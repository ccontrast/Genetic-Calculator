from __future__ import division
import re
import itertools



class Parent():
    def __init__(self, trait):
        self.trait = trait



DESIGNER_DICT = {"bumblebee":["pastel", "spider"], 
"pastave":["mojave", "pastel"], "pastel":["pastel","normal"], 
"super pastel":["pastel", "pastel"]}

# creates a dictionary of het morphs
def morph_dictionary():
    morph_list = ["pastel", "butter", "mojave", "yellow belly", "mocha", "het. albino", "desert", "pinstripe", "het. pied", "het. hypo", "spider", "harlequin", "woma", "het. axanthic,", "het. ultra mel"]
    morph_dict = {}
    for each in morph_list:
        morph_dict[each] = [each, "normal"]
    return morph_dict


# checks what morphs you can breed with your current stock
# gender? -- will be important to check
def process_collection(collection):
    collection_list = re.findall(r'\w+', collection)
    for k,v in DESIGNER_DICT.items():
        common = list(set(v) & set(collection_list))
        if common == DESIGNER_DICT[k]:
            print ("able to create %s with %s and %s.") % (k, v[0], v[1])

# punnett square - calculates what traits may be present in offspring
def punnett_square(parents):
    return list(itertools.product(*parents))

# combines mother and father traits into one list and
# returns percentages for likelyhood of offspring expressing trait
def trait_percentage(mother, father):
    parent_list = []
    parent_list.append(mother.trait)
    parent_list.append(father.trait)
    genes = [list(i) for i in punnett_square(parent_list)]
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

#how can we make it faster?

# p = [['pastel', 'het albino'],['pastel','normal']]
p = [['pastel', 'pastel'], ['pastel', 'normal']]
# c = "pastel, spider, normal"
# d = {"trait1":[['A', 'a'],['A', 'a']], "trait2":[['B', 'b'], ['b', 'b']]}

first = Parent(['albino', 'normal'])
second = Parent(['normal', 'normal'])
trait_percentage(first, second)

