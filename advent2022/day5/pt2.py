from os import chdir
chdir(r'C:\Users\gabri\OneDrive\Desktop\Python\advent2022\day5')

#Sets the initial position of the boxes in rows and cols
def set_cargo_data():
    rows = []
    columns = []
    with open('cargo.txt') as c:
        lines = c.readlines()
    lines = [line.split(' ') for line in lines]

    for line in lines[0:8]:
        row = clean_row(line)
        rows.append(row)
    for i in range(9):
        column = set_column(rows, i)
        columns.append(column)
    return columns
    

#Cleans the cargo data and seperates it into rows
def clean_row(line):
    space_count = 0
    row = []
    #There are four spaces in between each 'box'
    for i in line: 
        if i == '':
            space_count +=1
            if space_count == 4:
                row.append(i)
                space_count = 0
        else:
            row.append(i) 

    return row

#Based on the cleaned row, determines the column layout
def set_column(rows, column_no):
    column = []
    for row in rows:
        #Removing vertical whitespace
        if row[column_no] != '':
            column.append(row[column_no])
    return column
    
#Store the quantity, origin, and desination of the boxes    
def read_directions():
    with open('directions.txt') as d:
        lines = d.read()
    lines = [int(i) for i in lines.split() if i.isdigit()]
    directions = [lines[x:x+3] for x in range(0, len(lines), 3)]
    
    return directions

#Shuffle the boxes
def begin_loading(columns, directions):
    for quantity, origin, destination in directions: 
        moved_items = columns[origin-1][0:quantity]
        for item in moved_items:
            columns[origin-1].remove(item)
        
        #Items must be stacked one by one (in reverse order)
        #reversed_moved_items = moved_items[::-1]
        print(columns[destination-1])

        print('movin: ', moved_items)
        for item in moved_items[::-1]:
            columns[destination-1].insert(0, item)
        print(columns[destination-1])

    find_top_crates(columns)
    
#Returns a string based on the top crates of each stack    
def find_top_crates(columns):
    crates = []
    for column in columns:
        crates.append(column[0].strip('[]\n'))
    crates_str = ''.join(crates)
    print(f'The crate string is: {crates_str}')

columns = set_cargo_data()
for col in columns:
    print(col)
directions = read_directions()
begin_loading(columns, directions)
    

