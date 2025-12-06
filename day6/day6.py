# For the first part, I will need to parse the data to get rid of trailing spaces, I will also convert each value (except operators into a int)
# Later I will simply loop through the data (columns first) and extract each number
# Depending on the operator, I will add or subtract each number in the column and then reset

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.utils import parse_input

def part1():
    input = parse_input('input.txt')
    curr_sum = 0
    curr_mult = 1
    grand_total = 0

    # Split input to get rid of trailing white spaces (' ') so that indexing is easier
    for i in range(len(input)):
        input[i] = input[i].split()
    
    # Convert every number in the matrix into an int except the last row (operators) 
    for i in range(len(input)-1):
        for j in range(len(input[i])):
            input[i][j] = int(input[i][j])
    
    n = len(input)
    j = 0

    num_rows = len(input) - 1
    num_columns = len(input[0])

    for j in range(num_columns):
        operation = input[-1][j] # -1 is the last input where the operation is
        
        for i in range(num_rows):
            if operation == '*':
                curr_mult *= input[i][j]
            else:
                curr_sum += input[i][j]
            
        if operation == '*':
            grand_total += curr_mult
            curr_mult = 1
        else:
            grand_total += curr_sum
            curr_sum = 0
    
    print(grand_total)
        
part1()