#!/usr/local/bin/python3
import os


# Part 1
print("------- Part 1 -------")

conversion = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
packet = ""
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
    for char in file.readline():
        try:
            packet += conversion[char]
        except KeyError:
            break


def get_packet_type(packet):
    res = {}
    res["Version"] = int(packet[:3], 2)
    res["Type"] = int(packet[3:6], 2)
    if len(packet) > 6 and res["Type"] != 4:
        if packet[6] == "0":
            res["Length-type"] = "bits"
            res["Length"] = int(packet[7:22], 2)
            return res, packet[22:]
        else:
            res["Length-type"] = "amount"
            res["Length"] = int(packet[7:18], 2)
            return res, packet[18:]
    return res, packet[6:]


def parse_literal(packet):
    num = ""
    while True:
        num += packet[1:5]
        if packet[0] == "0":
            packet = packet[5:]
            break
        packet = packet[5:]
    return (int(num, 2), packet)


def parse_operator(packet, bits=None, packets=None):
    res = []
    if bits:
        target = len(packet) - bits
        while len(packet) > target:
            tmp_res, packet = parse_packet(packet)
            res.append(tmp_res)
    else:
        while len(res) < packets:
            tmp_res, packet = parse_packet(packet)
            res.append(tmp_res)
    return res, packet


def parse_packet(packet):
    res, packet = get_packet_type(packet)
    if res["Type"] == 4:
        num, remainder = parse_literal(packet)
        res["Value"] = num
    elif res["Length-type"] == "bits":
        packets, remainder = parse_operator(packet, bits=res["Length"])
        res["Packets"] = packets
    elif res["Length-type"] == "amount":
        packets, remainder = parse_operator(packet, packets=res["Length"])
        res["Packets"] = packets
    return res, remainder


def get_version_numbers(packet):
    res = packet["Version"]
    if packet["Type"] != 4:
        for pack in packet["Packets"]:
            res += get_version_numbers(pack)
    return res


structure = parse_packet(packet)[0]
print(f"The version numbers of all packets add up to {get_version_numbers(structure)}.")


# Part 2
print("------- Part 2 -------")


def calculate(packet):
    if packet["Type"] == 0:
        res = 0
        for pack in packet["Packets"]:
            res += calculate(pack)
    elif packet["Type"] == 1:
        res = 1
        for pack in packet["Packets"]:
            res *= calculate(pack)
    elif packet["Type"] == 2:
        res = []
        for pack in packet["Packets"]:
            res.append(calculate(pack))
        res = min(res)
    elif packet["Type"] == 3:
        res = []
        for pack in packet["Packets"]:
            res.append(calculate(pack))
        res = max(res)
    elif packet["Type"] == 5:
        res = int(calculate(packet["Packets"][0]) > calculate(packet["Packets"][1]))
    elif packet["Type"] == 6:
        res = int(calculate(packet["Packets"][0]) < calculate(packet["Packets"][1]))
    elif packet["Type"] == 7:
        res = int(calculate(packet["Packets"][0]) == calculate(packet["Packets"][1]))
    else:
        res = packet["Value"]
    return res


print(f"The encoded transmission evaluates to {calculate(structure)}.")
