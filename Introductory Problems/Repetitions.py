string = input()
max_count = count = 1
for i in range(len(string)-1):
  if string[i] == string[i+1]:
    count += 1
  else:
    count = 1
  if count > max_count:
    max_count = count
print(max_count)
