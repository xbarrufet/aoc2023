"""
https://adventofcode.com/2023/day/5

--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
"""

from itertools import groupby
import os

with open(os.path.dirname(__file__) + "/input.txt") as f:
    lines = f.read().splitlines()

groups = [tuple(group) for not_empty, group in groupby(lines, bool) if not_empty]

seeds, *categories = groups
seeds_ranges = tuple(map(int, seeds[0].split()[1:]))
seeds_numbers = [
    (seeds_ranges[i], seeds_ranges[i] + seeds_ranges[i + 1])
    for i in range(0, len(seeds_ranges), 2)
]

for category in categories:
    ranges = [tuple(map(int, numbers.split())) for numbers in category[1:]]

    sources = []
    while seeds_numbers:
        start, end = seeds_numbers.pop()
        for destination, source, length in ranges:
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)
            if overlap_start < overlap_end:
                sources.append(
                    (
                        overlap_start - source + destination,
                        overlap_end - source + destination,
                    )
                )
                if overlap_start > start:
                    seeds_numbers.append((start, overlap_start))
                if end > overlap_end:
                    seeds_numbers.append((overlap_end, end))
                break
        else:
            sources.append((start, end))

    seeds_numbers = sources

print(min(seeds_numbers)[0])