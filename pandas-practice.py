# myDict = {}

# valList = [1,2,3]

# # use setdefault(key, [default_value])
# # param: key to be search in the dictionary
# for val in valList: 
#     for ele in range(int(val), int(val) + 2):
#         myDict.setdefault(ele, []).append(val)


# print(myDict)

## Using setdefault() method
# myDict = {}

# listVal = [1,2,3] 

# for val in listVal: 
#     for ele in range(int(val), int(val) + 2):
#         myDict.setdefault(ele, []).append(val) 

# print(myDict)


## Using list comprehension
# d = dict((val, range(int(val), int(val) +2))
#         for val in ['1','2','3'])

# print(d)

## Using defaultdict
# from collections import defaultdict

# lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)]
# # defaultdict(list): use to add default value if the key added doesn't exist
# # Add method is same as list
# orDict = defaultdict(list)

# # iterating over list of tuples
# for key, val in lst: 
#     orDict[key].append(val)

# print(orDict)


# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")

# print(d)


## Using JSON

import json

lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)] 

dic = {}

hashed = json.dumps(lst)
print(hashed)
dic[hashed] = 'converted'
print(dic)