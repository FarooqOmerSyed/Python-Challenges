def count_elem(arr):
    count = 0
    s = set(arr)
    for i in arr:
        if i + 1 in s:
            count += 1
    return count


print(count_elem([1, 2, 3]))
