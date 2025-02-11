# Problem 1: Merge K sorted arrays
import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []
    
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
    
    while min_heap:
        val, arr_idx, ele_idx = heapq.heappop(min_heap)
        result.append(val)
        
        if ele_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1))
    
    return result

# Problem 2: Remove duplicates from sorted array
def remove_duplicates(arr):
    if not arr:
        return []
    
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    
    return arr[:write_index]

# Example
print(merge_k_sorted_arrays([[1,3,5,7], [2,4,6,8], [0,9,10,11]]))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5, 5]))