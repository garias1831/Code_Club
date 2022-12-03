score = 0
def get_choice_score(choices):
    choice_score = 0
    
    for choice in choices:
        if choice == 'X':
            choice_score += 1
        elif choice == 'Y':
            choice_score += 2
        elif choice == 'Z':
            choice_score += 3
    return choice_score    

def check_win(opponent_choices, choices):
    match_score = 0
    for (oc, c) in zip(opponent_choices, choices):
        if oc == 'A' and c == 'X':
            match_score += 3
        elif oc == 'B' and c == 'Y':
            match_score += 3
        elif oc == 'C' and c == 'Z':
            match_score += 3

        if oc == 'A' and c == 'Y':
            match_score += 6
        elif oc == 'B' and c == 'Z':
            match_score += 6
        elif oc == 'C' and c == 'X':
            match_score += 6
    return match_score
        
with open('strat.txt') as f:
    lines = f.read().split('\n')
    opponent_choices = [x[0] for x in lines]
    choices = [x[2] for x in lines]

score += get_choice_score(choices)
score += check_win(opponent_choices, choices)

print(f'The total score is: {score}')