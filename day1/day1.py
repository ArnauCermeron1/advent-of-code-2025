# Advent of Code Day 1 Solution
# Position of dial at start is 50
# Turning the dial left from 0 goes to 99 (one click left)
# Turning the dial right from 99 goes to 0 (one click right)

# For part 2, during the turn I have to check if it passes through 0, not only at the end
# This can be checked by adding an if for every position (current position % 0 == 0)

"""
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.utils import parse_input

def part1():
    rotations = parse_input('input.txt')
    current_pos = 50
    password = 0

    for rotation in rotations:
        direction = rotation[0]
        clicks = int(rotation[1:])

        if direction == 'L':
            current_pos = (current_pos - clicks) % 100
            if current_pos == 0:
                password += 1

        if direction == 'R':
            current_pos = (current_pos + clicks) % 100
            if current_pos == 0:
                password += 1
    
    print(password)


def part2():
    rotations = parse_input('input.txt')                                              
    current_pos = 50
    password = 0

    for rotation in rotations:
        direction = rotation[0]
        clicks = int(rotation[1:])

        if direction == 'L':
            for i in range(clicks):
                if ((current_pos - (i+1)) % 100) == 0:
                    password += 1
            current_pos = (current_pos - clicks) % 100

        if direction == 'R':
            for j in range(clicks):
                if ((current_pos + (j+1)) % 100) == 0:
                    password += 1
            current_pos = (current_pos + clicks) % 100

    print(password)
    
part1()
part2()