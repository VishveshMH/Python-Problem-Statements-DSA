def BinSrch(arr, k):
    low = 0
    high = len(arr)-1
    

    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid+1
    
arr = [0,1,2,2,2,3,3,3,3,4,5,6,7,8,9]
ind = BinSrch(arr,3)
print("The searched digit lies at index",ind, "the value of which is ",arr[ind])