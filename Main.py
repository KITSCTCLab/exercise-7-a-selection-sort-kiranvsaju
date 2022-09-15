from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for point in range (size)
  check = point
  for sort in (point,size):
    if array[sort]<array[point]:
      array[sort],array[point] = array[point],array[sort]
      return array
  

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
