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

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(BinarySearch_easy(arr,-1,0,len(arr)-1))
