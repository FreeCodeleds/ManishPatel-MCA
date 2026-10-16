def peakElement(arr, n):
    if n == 1:
        return arr[0]
    
    if arr[0] >= arr[1]:
        return arr[0]
    
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]
    
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
    
    return None 

# Example usage:
arr = [1, 3, 20, 4, 1, 54]
n = len(arr)
peak = peakElement(arr, n)
if peak is not None:
    print(f"The peak element is: {peak}")       