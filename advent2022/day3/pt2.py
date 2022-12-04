from os import chdir
chdir(r'C:\Users\Gabriel\Downloads\Python\advent2022\day3')


def seperate_groups(sacks):
    for i in range(0,len(sacks),3):
        yield sacks[i:i+3]


#Finds the element that is common between three different sacks
def find_duplicate(group):
    sack1 = set(group[0])
    sack2 = set(group[1])
    sack3 = set(group[2])
    duplicate = sack1.intersection(sack2, sack3)
    return (''.join(duplicate))


#Finds the priority value associated with each item
def get_priority_value(item):
    items = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
        )
    score = items.index(item.lower()) + 1
    if item.lower() != item:
        score += 26

    return score

priority_sum = 0
with open('contents.txt') as f:
    lines = f.read().split('\n')

sacks = [list(line) for line in lines]
elf_groups = list(seperate_groups(sacks))
for group in elf_groups:
    duplicate = find_duplicate(group)
    priority_value = get_priority_value(duplicate)
    priority_sum += priority_value
print(f'The sum of each group\'s priority values is: {priority_sum}')

#print(elf_groups)
