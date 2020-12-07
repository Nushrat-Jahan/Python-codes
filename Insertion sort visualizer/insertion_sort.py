import time

def insertion_sort(arr, displayBar, animSpeed): 
   
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        displayBar(arr, ['purple' if a == i or a ==j+1 else 'green' for a in range(len(arr))])
        time.sleep(animSpeed)
    displayBar(arr, ['purple' for a in range(len(arr))])