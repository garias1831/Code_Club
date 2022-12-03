from os import chdir
from itertools import islice

chdir(r'C:\Users\Gabriel\Downloads\Python\advent2022\day1')

elf_cal_sets = []
cal_totals = []

def list_to_int(lst):
    return [int(i) for i in lst]

with open('input.txt') as f:
    lines = f.read().split('\n')
    cutoffs = [i for i, x in enumerate(lines) if x == '']

    old_cut = -1
    for cut in cutoffs:  
        cal_set = list(islice(lines,old_cut+1,cut))
        cal_set = list_to_int(cal_set)
        elf_cal_sets.append(cal_set)
        old_cut = cut


cal_totals = [sum(cal) for cal in elf_cal_sets]
max_cal = max(cal_totals)
print (f'The maximum calorie total is: {max_cal}')

