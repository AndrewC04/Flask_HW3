# Name: Andrew Chau
# Date: 20 March 2022
# Course: CMPE 131
# Description: This program involves a sort function, sort_list, that returns a sorted list 
# from user input using nested while loops

def sort_list(list):
    n = len(list)

    #n = int(input('Enter the number of elements in list: '))
    #for i in range(1, n + 1):
    #    num = int(input('Enter the element(s) in the number array: '))
    #    list.append(num)

    i = 0
    while(i < n):
        y = 0
        while(y < n-i-1):
            if(list[y] > list[y+1]):
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp
            y+=1
        i+=1
    return list

list = [1, 3, 2, 7]
sort_list(list)
print(list)

# Input: 
# Enter the number of elements in list: 4
# Enter the element(s) in the number array: 1
# Enter the element(s) in the number array: 3
# Enter the element(s) in the number array: 2
# Enter the element(s) in the number array: 7
# Output:
# [1, 2, 3, 7]  
