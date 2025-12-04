# We need to check the roles of papers that the forklift can access
# To know if a role of paper can be accessed, we must check if there are LESS than 4 roles of paper adjacent to those
# We need to check around the role of paper, like a square.
# All lines are the same length

# For part 2, after the papers have been identified, we need to remove them (by replacing is a good idea)
# After removing, check again how many can be forklifts and remove them
# Repeat the process until the number of forklifts available is 0

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.utils import parse_input

def checkAdjacent(line_idx, line, element_idx, grid):
    adj_papers = 0

    # Check up -> (check in grid[i-1] element[j])
    if line_idx != 0:
        if grid[line_idx-1][element_idx] == '@':
            adj_papers += 1

    # Check up,left -> (check in grid[i-1] element[j-1])
    if line_idx != 0 and element_idx != 0:
        if grid[line_idx-1][element_idx-1] == '@':
            adj_papers += 1
    
    # Check up,right -> (check in grid[i-1] element[j+1])
    if line_idx != 0 and element_idx != len(line)-1:
        if grid[line_idx-1][element_idx+1] == '@':
            adj_papers += 1
    
    # Check left -> (check element[j-1])
    if element_idx != 0:
        if line[element_idx-1] == '@':
            adj_papers += 1
    
    # Check right -> (check element[j+1])
    if element_idx != len(line)-1:
        if line[element_idx+1] == '@':
            adj_papers += 1

    # Check down -> (check in grid[i+1] element[j])
    if line_idx != len(grid)-1:
        if grid[line_idx+1][element_idx] == '@':
            adj_papers += 1

    # Check down,left -> (check in grid[i+1] element[j-1])
    if line_idx != len(grid)-1 and element_idx != 0:
        if grid[line_idx+1][element_idx-1] == '@':
            adj_papers += 1

                
    # Check down,right -> (check in grid[i+1] element[j+1])
    if line_idx != len(grid)-1 and element_idx != len(line)-1:
        if grid[line_idx+1][element_idx+1] == '@':
            adj_papers+=1
    
    return adj_papers

def replace_forklifts(grid, positions):
    for i, j in positions:
        line = list(grid[i])
        line[j] = 'x'
        grid[i] = ''.join(line)

def part1():
    grid = parse_input('input.txt')
    num_papers = 0
    num_adj = 0

    for i, line in enumerate(grid):
        for j, element in enumerate(line):
            num_adj = checkAdjacent(i,line,j,grid)
            
            if num_adj < 4 and element == '@':
                num_papers += 1

    print(num_papers)

def part2():
    grid = parse_input('input.txt')
    no_forklifts = 0
    num_adj = 0
    num_papers = 0
    forklifts_present = 0

    while no_forklifts == 0:
        forklifts_present = 0
        positions = []
        for i, line in enumerate(grid):
            for j, element in enumerate(line):
                num_adj = checkAdjacent(i,line,j,grid)

                if num_adj < 4 and element == '@':
                    num_papers += 1
                    forklifts_present = 1
                    positions.append((i,j))

        if forklifts_present != 1:
            no_forklifts = 1
        else:
            replace_forklifts(grid,positions)

    print(num_papers)

part1()
part2()

