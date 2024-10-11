s = input()
small = s.lower()
cnt = 1
max = 0

for i in range(len(s)):
  if small[i] == small[i-1] == 'н':
    cnt += 1
    if cnt >= max:
      max = cnt

print(max)