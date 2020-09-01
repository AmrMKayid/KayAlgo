t = int(input())
for i in range(t):
  s = input()
  n = len(s)
  s_even = ''
  s_odd = ''
  for i in range(n):
    if i % 2 == 0:
      s_even += s[i]
    else:
      s_odd += s[i]

  print(s_even + ' ' + s_odd)
