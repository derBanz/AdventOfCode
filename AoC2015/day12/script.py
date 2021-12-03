#!/usr/local/bin/python3
import os
import json

# Part 1
print("------- Part 1 -------")

script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    data = json.load(file)


def check_data(data):
    result = 0
    if type(data) == dict:
        for k, v in data.items():
            try:
                result += k
            except TypeError:
                pass
            try:
                iter(v)
                result += check_data(v)
            except TypeError:
                try:
                    result += v
                except TypeError:
                    pass
    elif type(data) == list:
        for item in data:
            try:
                iter(item)
                result += check_data(item)
            except TypeError:
                try:
                    result += item
                except TypeError:
                    pass
    return result


result = check_data(data)
print(f'All numbers in the data set add up to {result}.')

# Part 2
print("------- Part 2 -------")


def check_data_without_red(data):
    result = 0
    if type(data) == dict:
        if 'red' in data or 'red' in data.values():
            return 0
        for k, v in data.items():
            try:
                result += k
            except TypeError:
                pass
            try:
                iter(v)
                result += check_data_without_red(v)
            except TypeError:
                try:
                    result += v
                except TypeError:
                    pass
    elif type(data) == list:
        for item in data:
            try:
                iter(item)
                result += check_data_without_red(item)
            except TypeError:
                try:
                    result += item
                except TypeError:
                    pass
    return result


result = check_data_without_red(data)
print(f'All numbers in the data set disregarding red add up to {result}.')
