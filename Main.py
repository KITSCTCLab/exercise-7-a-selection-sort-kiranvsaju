from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for point in range (len(array):
   check = point 
   for sort in range (point+1,len(array)):
     if array[sort]<array[point]:
       check=sort
    array[point],array[check] = array[check],array[point]
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
