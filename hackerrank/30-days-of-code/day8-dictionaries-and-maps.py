n = int(input())
phoneBook = {}
for i in range(n):
  line = input().split(' ')
  phoneBook[line[0]] = line[1]
  # print(line)

for i in range(n):
  name = input()
  if name in phoneBook.keys():
    print(name + "=" + phoneBook[name])
  else:
    print("Not found")
