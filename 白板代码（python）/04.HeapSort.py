# Heap Sort -- <Introduction to Algorithems 3rd> P87

# step 3: sort the heap
def Heap_sort(arr):
    Build_max_heap(arr)
    heap_size = len(arr)-1
    for i in range(heap_size,1,-1):
        #print(i)
        arr[0],arr[heap_size] = arr[heap_size],arr[0]
        heap_size = heap_size - 1
        Max_heap(arr,0)
    #arr[2],arr[1] = arr[1],arr[2]

# step 2: build a max heap
def Build_max_heap(arr):
    heap_size = len(arr)-1
    for i in range(int(heap_size/2),0 ,-1):
        #print(i,heap_size)
        Max_heap(arr,i)

# step 1: maintain the max heap
def Max_heap(arr, i):
    l,r = 2*i+1,2*(i+1)
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < len(arr) and arr[r] > largest:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        Max_heap(arr,largest)

if __name__ == '__main__':
    arr = [10, 6, 7, 4, 5, 1, 2, 8 , 9]
    #Build_max_heap(arr)
    Heap_sort(arr)
    print(arr)