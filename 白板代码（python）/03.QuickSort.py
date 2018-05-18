# Quick Sort -- <Introduction to Algorithems 3rd>

def QuickSort(arr, start, end):
    if start < end:
        k = Partition(arr, start, end)
        print(k,arr)
        QuickSort(arr,0,k - 1)
        QuickSort(arr,k + 1,end)

def Partition(arr,start, end):
    x = arr[end] # devide into 3 parts [ < x] [= x] [ >x ]
    i = start - 1
    for j in range(start,end):
        if arr[j] <= x:
            print(i,j,x,arr,arr[i+1],arr[j])
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]  # [arr[i] > x exchange arr[j] < x
    arr[i+1],arr[end] = arr[end],arr[i+1]  # puts x in the middle of arr which position is [i+1]
    return i + 1

if __name__ == '__main__':
    arr = [10,8,9,6,7,4,5,1,2]
    QuickSort(arr,0,len(arr)-1)
    print(arr)