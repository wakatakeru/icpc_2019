while (1):
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  print(a)
  c = []
  for i in range(n):
    c[i] = b[i] - a[i]
    if c[i] < 0:
      c[i] += m

  sa = max(c) - min(c)
  while (1):
    tmp = (m + min(c)) - max(c)
    if tmp < sa:
      sa = tmp
      c[c.index(min(c))] += m
    else:
      break
    
  ans = 0
  while (1):
    kari = c[i]
    kari.sort()
    for i in range(n):
      if kari[i] < 0:
        continue
      else:
        minc = kari[i]
      
    if min(c) > 0:
      for i in range(n):
        c[i] = c[i] - minc
    else:
      for i in range(n):
        if c[i] == minc:
          minin = i
        
      left = 0
      right = n-1
      for x in range(minin, -1, -1):
        if c[x] < 0:
          left = x + 1
      for y in range(minin, n, 1):
        if c[y] < 0:
          right = y - 1
      for z in range(left, right):
        c[z] = c[z] - minc

      ans += minc

  print(ans)