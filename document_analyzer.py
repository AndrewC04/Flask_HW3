# Name: Andrew Chau
# Date: 10 March 2022
# Course: CMPE 131
# Description: This program reads an input to words of a document and prints out the the top 5
# most frequent words sorted from most to least with no duplicates

file = open("document.txt", "r")
# document.txt contains: "hello hello Hello Drive good test Day day morning morning drive"

dict = {}

for word in file.read().lower().split():
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

sort = sorted(dict, key = dict.get, reverse=True)[:5]

print(" ")  

for key in sort:  
    print(key, ":", dict[key])

# Output: 
# 
# hello : 3
# drive : 2
# day : 2
# morning : 2
# good : 1