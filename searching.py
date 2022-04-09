def linear_search_iterative(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
        else:
            return False


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


def binary_search_recursive(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive_helper(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive_helper(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


def binary_search_recursive(arr, x):
    return binary_search_recursive_helper(arr, 0, len(arr)-1, x)

def linear_search_recursive_helper( arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return linear_search_recursive_helper(arr, l+1, r-1, x)

def linear_search_recursive(arr, x):
    return linear_search_recursive_helper(arr, 0, len(arr) - 1, x)
# arr1 = [-10, -5, -3, -1, 0, 5, 8, 10]
# print("searching using linear search iterative  ", str(arr1), "  for 8  -->  ", str(linear_search_iterative(arr1, 8)))
# print("searching using linear search iterative  ", str(arr1), "  for 2  -->  ", str(linear_search_iterative(arr1, 2)))
# print("searching using binary search iterative  ", str(arr1), "  for -5  -->  ", str(binary_search_iterative(arr1, -5)))
# print("searching using binary search iterative  ", str(arr1), "  for -8  -->  ", str(binary_search_iterative(arr1, -8)))
# print("searching using binary search recursive  ", str(arr1), "  for -3  -->  ", str(binary_search_recursive(arr1, -3)))
# print("searching using binary search recursive  ", str(arr1), "  for 6  -->  ", str(binary_search_recursive(arr1, 6)))
