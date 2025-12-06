# For the first part, I will need to parse the data to get rid of trailing spaces, I will also convert each value (except operators into a int)
# Later I will simply loop through the data (columns first) and extract each number
# Depending on the operator, I will add or subtract each number in the column and then reset

# For part 2, I will traverse the whole matrix from right to left in terms of columns but not in terms of rows
# Then go column by column parsing the ints in it depending on the length of the biggest number in the column

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

def part2():
    lines = parse_input("input.txt")
    grand_total = 0

    rows = [line.rstrip("\n") for line in lines]

    # Pad all rows to the same width so column indexing is valid
    width = max(len(row) for row in rows)
    rows = [row.ljust(width) for row in rows]

    num_rows = len(rows) - 1
    op_row = rows[-1]

    op_cols = []
    for c, ch in enumerate(op_row):
        if ch in "+*":
            op_cols.append(c)

    for idx in range(len(op_cols) - 1, -1, -1):
        op_col = op_cols[idx]
        op = op_row[op_col]

        span_start = op_col
        if idx == len(op_cols) - 1:
            span_end = width - 1
        else:
            span_end = op_cols[idx + 1] - 1

        nums = []
        for col in range(span_start, span_end + 1):
            digits = []
            for r in range(num_rows):
                if rows[r][col].isdigit():
                    digits.append(rows[r][col])
            if digits:
                nums.append(int("".join(digits)))

        # We want rightmost-number first, so reverse (cols are left->right)
        nums = nums[::-1]

        if op == "+":
            subtotal = sum(nums)
        else:
            subtotal = 1
            for n in nums:
                subtotal *= n

        grand_total += subtotal

    print(grand_total)

        
part1()
part2()