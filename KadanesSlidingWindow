def max_subarray_sum(arr):
    if not arr:
        return 0

    max_sum = curr_sum = arr[0]
    start_idx = 0

    for end_idx in range(1, len(arr)):
        if curr_sum + arr[end_idx] > arr[end_idx]:
            curr_sum += arr[end_idx]
        else:
            curr_sum = arr[end_idx]
            start_idx = end_idx

        while start_idx >= 0 and curr_sum > max_sum:
            max_sum = curr_sum
            start_idx -= 1
            if start_idx >= 0:
                curr_sum += arr[start_idx]

    return max_sum
