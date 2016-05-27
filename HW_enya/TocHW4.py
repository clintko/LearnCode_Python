"""
Homework 4
"""
import sys
import operator

# read in arguments
#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

k = sys.argv[1]
fileName = sys.argv[2]
#k = 5
#fileName = "HW4_Data.txt"
terms = dict()

# read in the file and count the first item of each line
with open(fileName, 'r') as f:
    for line in f:
        term = line.strip().split("\t")[0]
        if term in terms:
            terms[term] += 1
        else:
            terms[term] = 0

# sort by frequency of each item
result = sorted(terms.items(), key=operator.itemgetter(1), reverse=True)

# print out the top k
for idx in range(min([int(k), len(result)])):
    print(str(result[idx][0]) + "," + str(result[idx][1]))

# decide whether print k+1, ... etc
for idx in range(k, len(result)):
    if (result[idx][1] == result[k-1][1]):
        print(str(result[idx][0]) + "," + str(result[idx][1]))
    else:
        break
        
