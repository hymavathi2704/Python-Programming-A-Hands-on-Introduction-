'''Create a nested loop that produces the output below.
....1
...2
..3
.4
5  '''

#Code:
for num in range(1,6):
  for dots in range(5-num, 0, -1):
    print(".", end='')
  print(num)