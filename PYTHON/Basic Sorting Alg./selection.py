def selection(arr):
    for i in range(0, len(arr) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j

        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]

arr = [9,8,7,6,4,3,2,1]
selection(arr)
print(arr)
