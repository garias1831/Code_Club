from os import chdir

chdir(r'C:\Users\Gabriel\Downloads\Python\advent2021\day1')

#depth_vals = {'last_depth': 169, 'depth': 0}
last_depth = 169
depth = 0
increases = 0

with open('input.txt') as file:
    for line in file:
        depth = int(line)

        if depth > last_depth:
            increases += 1

        last_depth = depth
            
print(f'Number of depth increases: {increases}')       