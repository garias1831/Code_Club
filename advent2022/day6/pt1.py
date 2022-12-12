from os import chdir
chdir(r'C:\Users\1110177\Downloads\Python\advent2022\pt6')

def load_signals():
    with open('signals.txt') as s:
        signal = s.read().strip('\n')
    return signal

def find_packet_marker(string):
    char_window = []
    packet_marker = ''
    for x in range(len(string)):
        char_window = string[x:x+4]
        if len(char_window) == len(set(char_window)):
            char = ''.join(char_window)
            packet_marker = char
            break
    #+1 for index, +3 for end of the substring
    marker_location = string.find(packet_marker) + 4
    return marker_location
        


signal = load_signals()
marker_location = find_packet_marker(signal)
print(f'The location of the packet marker is: {marker_location}')