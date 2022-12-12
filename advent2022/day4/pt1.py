from os import chdir
chdir(r'C:\Users\1110177\Downloads\Python\advent2022\day4')

def find_full_intersection(section1, section2):
    section1 = section1.split('-')
    section2 = section2.split('-')
    section1 = [int(i) for i in section1]
    section2 = [int(i) for i in section2]
    section1 = {i for i in range(section1[0], section1[1] + 1)}
    section2 = {i for i in range(section2[0], section2[1] + 1)}
    print(section1, section2)
    large_section, small_section = get_section_size(section1, section2)
    
    if (large_section & small_section) == small_section:
        return True


def get_section_size(section1, section2):
    if len(section1) > len(section2):
        large_section = section1
        small_section = section2
    else:
        large_section = section2
        small_section = section1
    return large_section, small_section
    
def split_sections(section_pair):
    section1 = section_pair[0]
    section2 = section_pair[1]
    return section1, section2


full_intersections = 0
with open('input.txt') as f:
    lines = f.read().split('\n')

section_pairs = [line.split(',') for line in lines]
for i in range(len(section_pairs)):
    section1, section2, = split_sections(section_pairs[i])
    intersection = find_full_intersection(section1, section2)
    if intersection:
        full_intersections += 1
        
print(f'The number of complete intersections is: {full_intersections}')