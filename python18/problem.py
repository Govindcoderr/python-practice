def subset_sum_baacktrack(arr, traget, index=0, path=[]):
    if sum(path)==traget:
        print(path)

        return
    
    if sum(path)> traget or index >=len(arr):
        return
    
    for i in range(index, len(arr)):
        subset_sum_baacktrack(arr,traget,i+1, path+[arr[i]])
    
    arr = [2,3,5,7]
    traget= 7
    subset_sum_baacktrack(arr,traget)