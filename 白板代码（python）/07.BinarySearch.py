#  BinarySearch

# situation 1:
def BinarySearch_easy(arr, k, start, end):
    while start <= end:
        mid = (start + end ) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return BinarySearch_easy(arr,k,start,mid-1)
        elif arr[mid] < k:
            return BinarySearch_easy(arr,k,mid+1,end)
    # return the index of k

# situation 2:
def ReverseBinarySearch(arr, k, start, end):
    while start <= end:
        mid = ( start + end ) // 2
        if arr[mid] > arr[start] and arr[mid] < arr[end]:
            return BinarySearch_easy(arr,k,start,end)

        print(start,end,mid,arr[mid])
        if arr[mid] == k:
            return mid
        if arr[mid] > k and arr[start] < k and arr[mid] > arr[start]: # left is in order , and k is in left
            return BinarySearch_easy(arr,k,start,mid-1)
        elif arr[start] > k and arr[mid] > arr[start]:
            # left is in order, and k is in right
            return ReverseBinarySearch(arr,k,mid+1,end)
        if arr[mid] < k  and arr[end] > k and arr[mid] < arr[end]: # right is in order, and k is in right
            return BinarySearch_easy(arr,k,mid+1,end)
        elif arr[end] < k and arr[mid] < arr[end]:
            # right is in order, and k is in left
            return ReverseBinarySearch(arr, k, start, mid-1)

def reverseArrFindMin(arr, start, end):
    while start <= end:
        mid = (start + end )//2
        print(start,end,mid,arr[mid])
        if arr[mid] < arr[end] and arr[mid] > arr[start]:
            return arr[start]
        if arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
            return arr[mid]
        if arr[mid] < arr[end] and arr[mid] < arr[start]:
            # right is in order
            return reverseArrFindMin(arr,start,mid-1)
        if arr[mid] > arr[start] and arr[mid] > arr[end]:
            # left is in order
            return reverseArrFindMin(arr,mid+1, end)

if __name__ == '__main__':
    # situation 1:
    # arr = [1,2,3,4,5,6,7,8,9,10]
    # print(BinarySearch_easy(arr,-1,0,len(arr)-1))
    #arr = [1,2,3,4,5,6]
    arr = [8,9,10,11,12,13,15,16,1,2,3,4,5,6,7]
    #print(ReverseBinarySearch(arr, 6, 0, len(arr)-1))

    #print(ReverseBinarySearch_inde(arr,6,0,len(arr)-1))

    print(reverseArrFindMin(arr,0,len(arr)-1))