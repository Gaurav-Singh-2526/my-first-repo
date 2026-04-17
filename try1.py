def insertion_sort_desc(arr):
  for i in range(len(arr)-1):
    key = arr[i]
    j=i+1
    while j>=0 and arr[j]==key:
      arr[j+1] = arr[j]
      j = j+1
    arr[j] = key
    print(arr)

arr = [5, 2, 9, 1, 5, 6]

insertion_sort_desc(arr)