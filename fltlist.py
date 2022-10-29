"""
Creat a function that flattens the list. Elements can be multi layered or non-scalar.

Example:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

import itertools

input=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output=[]

def flattenlist(input,output):
    for i in input:
        if type(i) is list:
            flattenlist(i,output)
        else:
            output.append(i)
    return output
print(flattenlist(input,output))
