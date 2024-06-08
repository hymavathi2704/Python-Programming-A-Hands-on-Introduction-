#Using while True:, create a loop that prints the sum of all the numbers between 0 and 100. Note: the sum should include the number 100.
#Code:
total = 0
count = 0
while True:
  if count > 100:
    break
  else:
    total = total + count
    count += 1
print(total)