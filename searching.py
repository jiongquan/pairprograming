def linear_search_iterative(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
        else:
            return False
        
  
def linear_search_recursive(input_list, l, x, key):
    if x < l:
        return -1
    if input_list[l] == key:
        return l
    if input_list[x] == key:
        return x
    return linear_search_recursive(input_list, l+1, x-1, key)

# to execute program, input list and key go here
n = len(input_list)
result = linear_search_recursive(input_list, 0, n-1, key)
if result != -1:
    print ('Ture')
else:
    print ('False')


def binary_search_iterative(arr, x):
    high = len(arr) - 1
    low = 0
    undefined = -1

    while low <= high:
        mid = int(low + (high - low) / 2)
        if x == arr[mid]:
            return True

        elif x < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1
    return False


def binary_search_recursive(input_list, l, r, key): 
    if r >= l:
        n = l + (r - l) // 2
        if input_list[n] == key:
            return n
        elif input_list[n] > key:
            return binary_search_recursive(input_list, l, n-1, key)
        else:
            return binary_search_recursive(input_list, n + 1, r, key)
    else:
        return -1

# to execute program, input list and key go here
result = binary_search_recursive(input_list, 0, len(input_list)-1, key)
if result != -1:
    print('True')
else:
    print('False')
    
    
if __name__ == "__main__":
    
    # You can test your implementation here locally
    # anything outside this main section shall be executed when you import this file in
    # any other file such as in the analysis.py
