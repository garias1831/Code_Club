from os import chdir
from collections import deque
chdir(r'C:\Users\Gabriel\Downloads\Python\advent2021\day1')

last_window_sum = 0
current_sum = 0
increases = 0
window = deque([169, 150, 158])

with open('input.txt') as file:
    for line in file:
        depth = int(line)

        last_window_sum = sum(window)
        window.popleft()
        window.append(depth)
        current_sum = sum(window)

        if current_sum > last_window_sum:
            increases += 1
        #print(line, end='')

print(f'Total window increases: {increases}')



#lst = [4,4,8,1]
#print(sum(lst))

#dq = deque([4,7,8,1])
#print(dq)

#dq.popleft()
#dq.append(5)

#print(dq)