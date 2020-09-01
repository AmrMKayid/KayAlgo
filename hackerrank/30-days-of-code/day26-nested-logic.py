actual_date = list(map(int, input().split(' ')))
expected_date = list(map(int, input().split(' ')))
# print(actual_date, expected_date)
if actual_date[2] < expected_date[2]:
  print(0)
elif actual_date[2] > expected_date[2]:
  print(10000)
elif actual_date[1] > expected_date[1]:
  print(500 * (actual_date[1] - expected_date[1]))
elif actual_date[0] > expected_date[0]:
  print(15 * (actual_date[0] - expected_date[0]))
else:
  print(0)
