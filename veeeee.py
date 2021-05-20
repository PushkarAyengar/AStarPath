# def bubblesort(clist):
#     for i in range(len(clist)-1):
#         for j in range(len(clist)-1):
#             if clist[j] > clist[j+1]:
#                 clist[j], clist[j+1] = clist[j+1], clist[j]
#     print(clist)
# list = [1, 8, 2, 4, 3, 7, 6 ,9, 5]
# bubblesort(list)
#
# def selectionSort(clist):
#     for i in range(len(clist)):
#         min_index = i
#         for j in range(i+1, len(clist)):
#             if clist[min_index] > clist[j]:
#                 min_index = j
#         clist[i], clist[min_index] = clist[min_index], clist[i]
#     print(clist)
#
# list = [1, 8, 2, 4, 3, 7, 6 ,9, 5]
# selectionSort(list)


# def insertionSort(clist):
#     for i in range(1, len(clist)):
#         key = clist[i]
#         j = i - 1
#         while j >=0 and key < clist[j]:
#             clist[j+1] = clist[j]
#             j -= 1
#         clist[j+1] = key
#     print(clist)
#
# list = [1, 8, 2, 4, 3, 7, 6 ,9, 5]
# insertionSort(list)


# def merge(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#
#         L = arr[:mid]
#         R = arr[mid:]
#         merge(L)
#         merge(R)
#
#         i=j=k=0
#
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i +=1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k +=1
#         while i <len(L):
#             arr[k] = L[i]
#             i +=1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#
# def printList(arr):
#         for i in range(len(arr)):
#             print(arr[i], end=" ")
#         print()
#
#
# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is", end="\n")
#     printList(arr)
#     merge(arr)
#     print("Sorted array is: ", end="\n")
#     printList(arr)

# def merge(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#
#         L = arr[:mid]
#         R =  arr[mid:]
#
#         merge(L)
#         merge(R)
#
#         i = j = k = 0
#
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i+=1
#             else:
#                 arr[k] = R[j]
#                 j +=1
#             k +=1
#
#         while i < len(L):
#             arr[k] = L[i]
#             i +=1
#             k +=1
#         while j < len(R):
#             arr[k] = R[j]
#             j +=1
#             k +=1
#
# def printl(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=' ')
#     print()
#
# arr1 = [1, 5, 2, 58, 2, 7, 9, 4, 6, 2, 3, 58, 7, 64]
# print("initial value")
# printl(arr1)
# merge(arr1)
# print("final value")
# printl(arr1)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quiclsort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quiclsort(arr, low, pi-1)
        quiclsort(arr, pi+1, high)

arr1 = [1, 5, 2, 58, 2, 7, 9, 4, 6, 2, 3, 58, 7, 64]
n = len(arr1)
quiclsort(arr1, 0, n-1)
print (arr1)

