from collections import deque

d = deque()
print(d)

d.append('right')
d.appendleft('left')
print(d)

d.pop()
d.popleft()
print(d)

d.extend(['a', 'b', 'c'])
d.extendleft(['1', '2', '3'])
print(d)

d.rotate(3)
print(d)