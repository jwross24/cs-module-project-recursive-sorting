# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    # Start at the beginning of each sub-array
    arrA_idx = 0
    arrB_idx = 0

    arrA_len = len(arrA)
    arrB_len = len(arrB)

    for _ in range(arrA_len + arrB_len):
        if arrA_idx < arrA_len and arrB_idx < arrB_len:
            # Check which value at the start of the sub-array is smaller:
            # If the value at the beginning of array A is smaller, add it to the sorted array
            if arrA[arrA_idx] <= arrB[arrB_idx]:
                merged_arr.append(arrA[arrA_idx])
                arrA_idx += 1
            # Else, add the value at the beginning of array B to the sorted array
            else:
                merged_arr.append(arrB[arrB_idx])
                arrB_idx += 1
        # If we reached the end of array A, add elements from array B
        elif arrA_idx == arrA_len:
            merged_arr.append(arrB[arrB_idx])
            arrB_idx += 1
        # If we reached the end of array B, add elements from array A
        elif arrB_idx == arrB_len:
            merged_arr.append(arrA[arrA_idx])
            arrA_idx += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # If the list is empty or a single element, do nothing and return it
    if len(arr) <= 1:
        return arr

    # Get the midpoint
    middle = len(arr) // 2

    # Sort and merge each half of the array
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    # Merge the lists into a new one
    return merge(left_arr, right_arr)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
