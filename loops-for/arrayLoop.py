def insert_squares(arr, num):
  # add square of numbers from 1 to num to the list named arr and return list
  for i in range(1, num+1):
    arr.append(i * i)
  return arr

# arr = [1, 2, 3]
# print(insert_squares(arr, 5))
