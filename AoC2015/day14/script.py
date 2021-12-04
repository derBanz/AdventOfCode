#!/usr/local/bin/python3
import os

# Part 1
print("------- Part 1 -------")

data = []
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        line = line.split()
        data.append([line[0], int(line[3]), int(line[6]), int(line[13])])


def travel_distance(reindeer, time):
    travel = reindeer[0] * reindeer[1]
    full_intervals = int((time / (reindeer[1] + reindeer[2])))
    remainder = (time - full_intervals * (reindeer[1] + reindeer[2]))
    distance = travel * full_intervals
    half_interval = reindeer[0] * remainder if remainder < reindeer[1] else travel
    return distance + half_interval


best = max([[reindeer, travel_distance(reindeer[1:], 2503)] for reindeer in data], key=lambda x: x[1])

print(f'After 2503 seconds, {best[0][0]} wins the race with {best[1]}km.')

# Part 2
print("------- Part 2 -------")

race = [[x, 0, 0] for x in data]

for i in range(2503):
    for j, reindeer in enumerate(race):
        race[j][1] = travel_distance(reindeer[0][1:], i + 1)
    race[race.index(max(race, key=lambda x: x[1]))][2] += 1
best = max(race, key=lambda x: x[2])

print(f'After 2503 seconds, {best[0][0]} wins the race with {best[1]}km and a score of {best[2]}.')
