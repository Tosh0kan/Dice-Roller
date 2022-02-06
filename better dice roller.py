from random import choice
from re import split
    
def splitter(string: str):
    string = string.lower()
    a = split(r"\s|(\d+)", string)
    while '' in a:
        a.remove('')
    while None in a:
        a.remove(None)
    
    return a

def get_vars(list: list):
    numDice = int(list[list.index('d')-1])
    numSides = int(list[list.index('d') +1])
    if '+' in list:
        operator = '+'
    else:
        operator = ''

    if '+' in list:
        modifier = int(list[list.index('+') +1])
    elif '-' in list:
        modifier = int(list[list.index('-') +1]) * -1
    else:
        modifier = 0

    if '>' in list:
        threshold = int(list[list.index('>') +1])
        threshold_op = '>'
    elif '<' in list:
        threshold = int(list[list.index('<') +1])
        threshold_op = '<'
    elif '>=' in list:
        threshold = int(list[list.index('>=') +1])
        threshold_op = '>='
    elif '<=' in list:
        threshold = int(list[list.index('<=') +1])
        threshold_op = '<='
    else:
        threshold = 0
        threshold_op = ''

    repeat_value = 0 if ('repeat' not in list) else int(list[list.index('repeat') +1])
        
    return numDice, numSides, operator, modifier, repeat_value, threshold, threshold_op

def rollDice():
    results = []
    for x in range(numDice):
        results.append(choice(range(1,numSides+1)))
    return results, sum(results, modifier)

def get_roll():
    results, summation = rollDice()
    if modifier != 0:
        output_message = f"""{results} {operator}{modifier} = {summation}"""
    else:
        output_message = f"""{results} = {summation}"""
        
    return output_message, summation, results

while True:
    roll_input = input('Roll? ')
    processed_input = splitter(roll_input)
    numDice, numSides, operator, modifier, repeat_value, threshold, threshold_op = get_vars(processed_input)
    loop_count = 0
    while loop_count <= repeat_value:
        output_message, summation, results = get_roll()
        if threshold_op == '<':
            while summation >= threshold:
                output_message, summation, results = get_roll()

        elif threshold_op == '>':
            while summation <= threshold:
                output_message, summation, results = get_roll()

        print(output_message)
        loop_count = loop_count +1