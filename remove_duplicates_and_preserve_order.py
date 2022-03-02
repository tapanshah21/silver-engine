#!/usr/bin/env python
# using OrderedDict to preserve the order of insertion
from collections import OrderedDict
import time
times = 0

# loop to generate a list of emails including duplicates
items = []
i = 0
size = 10
half = size/2
for i in range(size):
    if i < half:
        items.insert( i, str(i) + "@mail.com")     
    else:
        items.insert(i, str(int(i/2)) + "@mail.com")   

# prints the entire list
print("List with duplicates" + str(items))

# prints the list of unique email addresses in the original order
print(" List without duplicated" + str(list(OrderedDict.fromkeys(items))))