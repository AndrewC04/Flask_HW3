def sort_list(list):
    list = [1, 3, 2, 7]
    n = len(list)

    #n = int(input('Enter the number of elements in list: '))
    #for i in range(1, n + 1):
    #    num = int(input('Enter the element(s) in the number array: '))
    #    list.append(num)

    i = 0
    while(i < n-1):
        y = 0
        while(y < n-i-1):
            if(list[y] > list[y+1]):
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp
            y+=1
        i+=1

    print(list)

# sort_list(list)

# Input: 
# Enter the number of elements in list: 4
# Enter the element(s) in the number array: 1
# Enter the element(s) in the number array: 3
# Enter the element(s) in the number array: 2
# Enter the element(s) in the number array: 7
# Output:
# [1, 2, 3, 7] 
