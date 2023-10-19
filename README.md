# Kadane's Sliding Window
Combines Kadane's Algorithm With a Sliding Window

The ‘Kadane’s Sliding Window’ algorithm is a novel approach to finding the maximum sum of a subarray within an array, which may contain both positive and negative numbers. This algorithm is a fusion of the classic Kadane’s algorithm and the sliding window technique, both of which are well-established methods in computer science for solving array-based problems.

The algorithm works by initializing three variables: max_sum (which holds the maximum subarray sum found so far), curr_sum (which holds the current maximum subwindow sum), and start_idx (which marks the start of the current subwindow). The algorithm then iterates over the array from the second element to the end. For each element, it checks if adding this element to the current subwindow would increase curr_sum. If so, it adds the current element to curr_sum; otherwise, it resets curr_sum to be equal to the current element.

The unique aspect of this algorithm is its dynamic adjustment of the start index of the subwindow. While keeping the end index fixed, it moves the start index towards the left until either start_idx becomes less than 0 or adding the subarray starting from start_idx and ending at end_index produces a smaller sum compared to max_sum.

This method provides an efficient way to handle larger arrays as it only needs to iterate through the array twice, rather than comparing every possible pairing of elements like brute force methods do. However, its efficiency can still be influenced by factors such as the size of the array and the distribution of elements within it.

The ‘Kadane’s Sliding Window’ algorithm is a promising alternative to traditional approaches for finding maximum subarray sums and could be particularly useful in scenarios where data is streamed or memory is limited
