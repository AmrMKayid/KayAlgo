# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, E):
  # write your code in Python 3.6
  S = sorted(S)
  min_chairs = 1
  party = dict(zip(S, E))
  party = {
      person: party[person]
      for person in dict.fromkeys(sorted([person for person in party]))
  }
  seated = [S[0]]
  for person in S[1:]:
    char = min(seated)
    if person - party[char] < 0:
      seated.append(person)
      min_chairs += 1
    else:
      seated.append(person)
      seated.pop(char)

  return min_chairs


print(solution([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))
