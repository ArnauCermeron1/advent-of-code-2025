# In this problem I have to find out the fresh IDs
# The problem input is separated in two sections, the id ranges and the actual ids
# I need to add every id into a set (for O(1) lookup)
# Once added, simply check if the range we are looking at includes any id in the set (bottom <= id <= top)

# For part 2, I will sort the ranges in order (bottom part), and check if the next range is included in the current one
# If it is I will merge and do that until that block is unmergeable, once it is count the number of ids in that range (top-bottom + 1)

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.utils import parse_input

def part1():
    input = parse_input('input.txt')
    i = 0
    split_at = 0
    unique = set()
    ids = set()

    for val in input:
        if val == '':
            split_at = i
        i+=1
    
    ranges = input[:split_at]
    ids_raw = input[split_at+1:]

    for val in ids_raw:
        id = int(val)
        ids.add(id)
    
    intervals = []
    for rangee in ranges:
        bottom,top = rangee.split('-')
        intervals.append((int(bottom), int(top)))

    for idn in ids:
        for bottom,top in intervals:
            if bottom <= idn <= top:
                unique.add(idn)

    print(len(unique))


def part2():
    input = parse_input('input.txt')
    i = 0
    split_at = 0

    for val in input:
        if val == '':
            split_at = i
        i+=1
    
    ranges = input[:split_at]
    
    intervals = []
    for rangee in ranges:
        bottom,top = rangee.split('-')
        intervals.append((int(bottom), int(top)))
    
    # Sort intervals by starting point
    intervals.sort(key=lambda x: x[0])

    total_fresh = 0
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end + 1:
            # Overlaps or touches -> extend current interval
            current_end = max(current_end, end)
        else:
            # Disjoint -> close previous interval
            total_fresh += current_end - current_start + 1
            current_start, current_end = start, end

    total_fresh += current_end - current_start + 1

    print(total_fresh)


part1()
part2()