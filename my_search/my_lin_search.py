def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1

if __name__ == "__main__":
   numbers = [1,3,5,6,8,2,9,7]
   a = 9
   print(linear_search(numbers, a))