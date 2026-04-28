# Day 6 - Reading File Line by Line

with open("sample_report.txt", "r") as file:
    lines = file.readlines()

print("Line by line output:")

for line in lines:
    print(line.strip())
