def selection_sort(lst):
    # Your code goes here
    n = len(lst)
    
    for passes in range(0,n):
            for i in range(0,n-1):
                if lst[i]>lst[i+1]:
                    lst[i]= lst[i+1]

    return lst







lst1 = [1,2,4,6,7] 
sortlist = selection_sort(lst1)

print(sortlist)