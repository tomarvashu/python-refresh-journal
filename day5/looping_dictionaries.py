# Day 5 - Looping Through Dictionaries

engineer = {
    "name": "Amit",
    "branch": "Delhi",
    "tickets_closed": 35,
    "rating": "Good"
}

print("Keys:")
for key in engineer.keys():
    print(key)

print("\nValues:")
for value in engineer.values():
    print(value)

print("\nKey-value pairs:")
for key, value in engineer.items():
    print(key, ":", value)

branches = {
    "Delhi": 82,
    "Chennai": 76,
    "Bangalore": 88,
    "Ludhiana": 91
}

print("\nBranch performance:")
for branch, closure_rate in branches.items():
    print(branch, "closure rate:", closure_rate)
