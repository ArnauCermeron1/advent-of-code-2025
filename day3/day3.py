# Batteries (the input) is arranged into lines with breaks (I can use my parse_input function)
# I have to achieve the highest joltage
# In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
# I cannot rearrange the batteries

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.utils import parse_input

def part1():
    batteries = parse_input('input.txt')
    joltage = 0
    
    for battery in batteries:
        max_1 = 0
        max_1_idx = 0
        max_2 = 0
        i = 0

        # Check for highest value in the battery excluding the last number
        for ch in battery[:len(battery)-1]:
            num = int(ch)
            if num > max_1:
                max_1 = num
                max_1_idx = i
            i += 1

        # Prepare string to check from the index where the highest number was found onwards
        battery2 = battery[max_1_idx+1:]

        # Check for highest number after first highest value was found
        for ch in battery2:
            num = int(ch)
            if num > max_2:
                max_2 = num
            
        # Finally, add them together so 9,8 becomes 98
        str1 = str(max_1) + str(max_2)
        joltage += int(str1)
    
    print(joltage)


part1()