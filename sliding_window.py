# def find_averages_of_subarrays(K, arr):
#   result = []
#   windowSum, windowStart = 0.0, 0
#   for windowEnd in range(len(arr)):
#     windowSum += arr[windowEnd]  # add the next element
#     # slide the window, we don't need to slide if we've not hit the required window size of 'k'
#     if windowEnd >= K - 1:
#       result.append(windowSum / K)  # calculate the average
#       windowSum -= arr[windowStart]  # subtract the element going out
#       windowStart += 1  # slide the window ahead

#   return str(result)[1:-1].replace(",", "")


# def main():
#   k = int(input())
#   arr = [int(i) for i in input().split()]
#   result = find_averages_of_subarrays(k, arr)
#   print("Averages of subarrays of size K: {}".format(result))


# main()


def max_sub_array_of_size_k(k, arr):
  max_sum , window_sum = 0, 0
  window_start = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead
  return max_sum


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()