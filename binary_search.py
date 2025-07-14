
# def binary_search(arr,target):
#     size=len(arr)

#     start =0
#     end=size-1

#     while start<=end:
#         mid = (start + end)//2

#         if(arr[mid]== target):
#             return mid
        
#         elif(arr[mid]>target):
#             end = mid-1
#         elif(arr[mid]<target):
#             start = mid+1

#     return -1




# sorted_list = [10,23,35,45,50,70,85]

# target = 85

# result = binary_search(sorted_list,target)

# print(result)

## bubble sort


def bubble_sort(arr):
    n = len(arr)
    for passes in range(0,n):
        for j in range(0 ,n-1-passes):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr






unsortedList = [5,4,3,2,1]#[54,99,12,45,7,88,90,99]

sortList = bubble_sort(unsortedList)

print("element ",sortList)