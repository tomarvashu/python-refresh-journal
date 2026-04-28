# Day 6 - Reading a File

# This example reads from sample_report.txt

with open("sample_report.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)
