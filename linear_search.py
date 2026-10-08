def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


marks = [56, 78, 90, 43, 67, 82, 71]

result = linear_search(marks, 67)
if result != -1:
    print("Found at index:", result)
else:
    print("Not found")
