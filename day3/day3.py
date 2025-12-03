# Batteries (the input) is arranged into lines with breaks (I can use my parse_input function)
# I have to achieve the highest joltage
# In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
# I cannot rearrange the batteries

# For part 2, there will be 12 digits in each bank's joltage output instead of two.
# In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

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

def part2():
    batteries = parse_input('input.txt')
    joltage = 0
    
    for battery in batteries:
        # Select 12 digits to maximize the resulting number (greedy approach)
        n = len(battery)
        k = 12  # number of digits to select
        to_remove = n - k  # number of digits to skip
        
        result = []
        for digit in battery:
            # Remove smaller digits from result if we have room to skip them
            while result and result[-1] < digit and to_remove > 0:
                result.pop()
                to_remove -= 1
            result.append(digit)
        
        # Take only the first k digits
        max_value = int(''.join(result[:k]))
        joltage += max_value
    
    print(joltage)


part1()
part2()