
# def find_sum(arr = [], sum = 0):
#   pt1 = 0
#   pt2 = len(arr) - 1
#   arr.sort()

#   while pt1 < len(arr) / 2:
#     if arr[pt1] + arr[pt2] > sum:
#       pt2 -=1

#     elif arr[pt1] + arr[pt2] == sum:
#       return [pt1, pt2]

#     else:
#       pt1 += 1

#   return [-1, -1]

def square_list(arr):
  pt1 = 0
  pt2 = len(arr) - 1
  while pt1 < len(arr) // 2:
    arr[pt1] = arr[pt1] * arr[pt1]
    arr[pt2] = arr[pt2] * arr[pt2]
    pt1, pt2 = pt1 + 1, pt2 - 1

  return arr


def main():
  arr = [int(i) for i in input().split()]
  # sum = int(input())
  # result = find_sum(arr,sum)
  result = square_list(arr)
  print(result)


main()