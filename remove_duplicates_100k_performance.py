#!/usr/bin/env python
from collections import OrderedDict
import time
times = 0

# run the function 10 times to prove that time taken is consistently under 1 second
for times in range(10):
    items = []
    i = 0
    size = 100000
    half = size/2

    # generate a list of emails with 50% duplicates
    for i in range(size):
        if i < half:
            items.insert( i, str(i) + "@mail.com")     
        else:
            items.insert(i, str(int(i/2)) + "@mail.com")   

    # capture the start time of processing the list
    start = time.time()

    # using OrderedDict to preserve the order
    list(OrderedDict.fromkeys(items))

    # capture the end time of processing 
    end = time.time()

    # print the lenght of the original list
    print("Original list: " + str(len(items)))

    # print the length of list after deduplication
    print("Distinct list:" + str(len(list(dict.fromkeys(items)))))

    # print total time take to process
    time_taken = end - start
    print("Time taken:"+ str(time_taken))