# Heap Sort -- <Introduction to Algorithems 3rd> P87

# vs InsertSort & MergeSort

# step 3: sort the heap
def Heap_sort(arr):
    Build_max_heap(arr)
    heap_size = len(arr)-1

    for i in range(heap_size,-1,-1):
        # from the latest non-leaf node to adjust
        arr[0],arr[i] = arr[i],arr[0]
        Max_heap(arr,0,i)
        #print(i,heap_size,arr)


# step 2: build a max heap
def Build_max_heap(arr):
    heap_size = len(arr)-1
    for i in range(int(heap_size/2),-1,-1):
        #print(heap_size,int(heap_size/2))
        # heap_size/2 is the lastest non-leaf root node
        Max_heap(arr,i,heap_size)

# step 1: maintain the max heap
def Max_heap(arr, i,heap_size):
    l,r = 2*i+1,2*(i+1)
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        #print(arr[i],arr[largest])
        #print("root:%s,left:%s,right:%s,largest:%s" % (str(arr[i]), str(arr[l]), str(arr[r]), str(arr[largest])))
        arr[i],arr[largest] = arr[largest],arr[i]
        Max_heap(arr,largest,heap_size)

if __name__ == '__main__':
    arr = [10,8,9,6,7,4,5,1,2,11]
    #Max_heap(arr,1,1)
    Build_max_heap(arr)
    #Heap_sort(arr)
    print(arr)