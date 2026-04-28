# Day 6 - Mini Exercise: Service Log Summary

service_updates = [
    "Delhi - 12 tickets closed",
    "Chennai - 8 tickets closed",
    "Bangalore - 10 tickets closed",
    "Ludhiana - 6 tickets closed"
]

with open("service_log.txt", "w") as file:
    for update in service_updates:
        file.write(update + "\n")

print("Service log created.")

with open("service_log.txt", "r") as file:
    lines = file.readlines()

print("\nService Log Summary:")
for line in lines:
    print(line.strip())
