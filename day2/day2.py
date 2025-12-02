"""
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124

"""
# These are ranges of ids, they are sepparated by commas.
# The first number in each range is the starting id, and the second number is the ending id.
# An invalid id is one that contains any digit more than twice. (so in 95-115, 99 is invalid because it contains the digit 9 twice)
# 1188511880-1188511890 has one invalid ID, 1188511885.
# The task is to add up all the invalid IDs, for the example the answer should be 1227775554.

# For part two an id is invalid if it is made only of some sequence of difits repeated at least twice
# So, 12341234 (1234 two times)

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.utils import parse_input_commas

def valid(num):
    if len(num) %2 != 0:
        return 0

    mid = len(num) // 2
    first = num[:mid]
    second = num[mid::]

    if first == second:
        return num
    else:
        return 0

def valid_2(num: str) -> int:
    n = len(num)

    if n < 2:
        return 0

    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len != 0:
            continue

        block = num[:pattern_len]
        repetitions = n // pattern_len

        if repetitions >= 2 and block * repetitions == num:
            return int(num)

    return 0


def part1():
    ranges = parse_input_commas('input.txt')
    print(ranges)
    sum_invalid = 0

    for rangee in ranges:
        first_id, second_id = rangee.split('-')
        first_id_int = int(first_id)
        second_id_int = int(second_id)

        for i in range(first_id_int, second_id_int+1):
            num = valid(str(i))
            invalid = int(num)
            if invalid > 0:
                sum_invalid += invalid

    print(sum_invalid)

def part2():
    ranges = parse_input_commas('input.txt')
    print(ranges)
    sum_invalid = 0

    for rangee in ranges:
        first_id, second_id = rangee.split('-')
        first_id_int = int(first_id)
        second_id_int = int(second_id)

        for i in range(first_id_int, second_id_int + 1):
            invalid = valid_2(str(i))
            if invalid > 0:
                sum_invalid += invalid

    print(sum_invalid)


part1()
part2()