import re

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("inputs/day1.txt", "r") as f:
    inputs = f.read().split("\n")

test_inputs_pt1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
test_digits_pt1 = [list(map(int, re.findall(r"\d+", i))) for i in test_inputs_pt1]
test_calibration_values_pt1 = [int((str(d[0])[0] + str(d[-1])[-1])) for d in test_digits_pt1]
assert sum(test_calibration_values_pt1) == 142

digits_pt1 = [list(map(int, re.findall(r"\d+", i))) for i in inputs]
calibration_values_pt1 = [int((str(d[0])[0] + str(d[-1])[-1])) for d in digits_pt1]
print(sum(calibration_values_pt1))

