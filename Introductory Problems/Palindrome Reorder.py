from collections import Counter
in_string = input()
count_dict = Counter(in_string)
keys = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
odd_dict = { x: count_dict[x] for x in keys if count_dict[x] % 2 != 0 }
even_dict = { x: count_dict[x] for x in keys if count_dict[x] != 0 and count_dict[x] % 2 == 0 }
if len(odd_dict) == 0:
  for key in sorted(even_dict, reverse = False):
    print(key * (even_dict[key] // 2), end = '')
  for key in sorted(even_dict, reverse = True):
    print(key * (even_dict[key] // 2), end = '')
elif len(odd_dict) == 1:
  for key in sorted(even_dict, reverse = False):
    print(key * (even_dict[key] // 2), end = '')
  for key, value in odd_dict.items():
    print(key * value, end = '')
  for key in sorted(even_dict, reverse = True):
    print(key * (even_dict[key] // 2), end = '')
else:
  print("NO SOLUTION")
