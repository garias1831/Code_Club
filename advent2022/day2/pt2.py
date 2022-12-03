score = 0
def get_choice_score(opponent_choices, choices):
    choice_score = 0
    for (oc, c) in zip(opponent_choices, choices):
        if oc == 'A' and c == 'X':
            choice_score += 3
        elif oc == 'A' and c == 'Y':
            choice_score += 1
        elif oc == 'A' and c == 'Z':
            choice_score += 2     
        if oc == 'B' and c == 'X':
            choice_score += 1
        elif oc == 'B' and c == 'Y':
            choice_score += 2
        elif oc == 'B' and c == 'Z':
            choice_score += 3
        if oc == 'C' and c == 'X':
            choice_score += 2
        elif oc == 'C' and c == 'Y':
            choice_score += 3
        elif oc == 'C' and c == 'Z':
            choice_score += 1
    return choice_score    

def check_win(choices):
    match_score = 0
    for choice in choices:
        if choice == 'Y':
            match_score += 3
        elif choice == 'Z':
            match_score += 6
    return match_score

        
with open('strat.txt') as f:
    lines = f.read().split('\n')
    opponent_choices = [x[0] for x in lines]
    choices = [x[2] for x in lines]

score += check_win(choices)
score += get_choice_score(opponent_choices, choices)

print(f'The total score is: {score}')