"""
Homework 3
"""
import sys
import operator

#searchStr = sys.argv[1]
searchStr = "NowNew#abc,2014#abc"
#fileName = sys.argv[2]
fileName = 'HW3_Data.txt'
terms = dict()

#print(searchStr, fileName)

for term in searchStr.split(","):
    terms[term] = 0

# read in file and search for each pair of terms
with open(fileName, 'r') as f:
    for line in f:
        #print(line.strip())    
        for term in terms.keys():
            termSplit = term.split("#")
            if ((termSplit[0] in line) & (termSplit[1] in line)):
                terms[term] += 1

# output the frequency of each pair of terms
results = sorted(terms.items(), key=operator.itemgetter(1), reverse=True)
for result in results:
    print(str(result[0]) + "," + str(result[1]))
