# bounce.py
#
# Exercise 1.5
start = 100
ratio = 3/5

for i in range(10):
    start = start * ratio
    print(i + 1, round(start, 4))
