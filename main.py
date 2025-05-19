
import random
import time
import matplotlib.pyplot as plt


# Function to perform selection sort on a table based on the first column
def selection_sort(table):
   for i in range(len(table)):
      min_idx = i
      for j in range(i + 1, len(table)):
         if table[j][0] < table[min_idx][0]:
            min_idx = j
      table[i], table[min_idx] = table[min_idx], table[i]

# Function to perform insertion sort on a table based on the first column
def insertion_sort(table):
   for i in range(1, len(table)):
      key = table[i]
      j = i - 1
      while j >= 0 and key[0] < table[j][0]:
         table[j + 1] = table[j]
         j -= 1
      table[j + 1] = key

# Function to perform bubble sort on a table based on the first column
def bubble_sort(table):
   n = len(table)
   for i in range(n):
      for j in range(0, n - i - 1):
         if table[j][0] > table[j + 1][0]:
            table[j], table[j + 1] = table[j + 1], table[j]

# Function to merge two sorted tables based on the first column
def merge(left, right):
   result = []
   i = j = 0
   while i < len(left) and j < len(right):
      if left[i][0] < right[j][0]:
         result.append(left[i])
         i += 1
      else:
         result.append(right[j])
         j += 1
   result.extend(left[i:])
   result.extend(right[j:])
   return result

# Function to perform merge sort on a table based on the first column
def merge_sort(table):
   if len(table) <= 1:
      return table
   mid = len(table) // 2
   left = table[:mid]
   right = table[mid:]
   left = merge_sort(left)
   right = merge_sort(right)
   return merge(left, right)


# Create 10 tables of each size
sizes = [100, 200, 300, 400]
sort_algorithms = ["Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort"]
num_tables_per_size = 10
tables = []
execution_times = []
for sort_algorithm in [selection_sort, insertion_sort, bubble_sort, merge_sort]:
   times = []
   for size in sizes:
      for _ in range(num_tables_per_size):   
         table = [random.randint(1, 100) for _ in range(size)]
         tables.append(table)
         start_time = time.time()
         sort_algorithm(tables)
         end_time = time.time()
         execution_time = end_time - start_time
         times.append(execution_time)
   execution_times.append(times)


# Create graphs
for i, algorithm in enumerate(execution_times):
    plt.plot(sizes, algorithm, label=sort_algorithms[i])

plt.xlabel('Table Size')
plt.ylabel('Execution Time (s)')
plt.title('Sorting Algorithm Complexity')
plt.legend()
plt.show()

# Write the tables to a text file
with open("tables.txt", "w") as file:
   for table in tables:
      for row in table:
         row_str = str(row)
         file.write(row_str + "\t")
      file.write("\n")
      file.write("\n##################################################################################################################\n")
      file.write("\n")
