n = int(input())
dic = {}
for i in range(n):
    line = input().split(' ')
    dic[line[0]] = line[1]
    #print(line)

for i in range(n):
    name = input()
    if name in dic.keys():
        print(name + "=" + dic[name])
    else:
        print("Not found")