# Day 2 - Lists Practice

machines = ["Lockstitch", "Overlock", "Flatlock"]

print("Original list:", machines)

machines.append("Button Sewing")
print("After append:", machines)

machines.insert(1, "Feed Off Arm")
print("After insert:", machines)

machines.remove("Overlock")
print("After remove:", machines)

print("First machine:", machines[0])
print("Last machine:", machines[-1])
print("List length:", len(machines))

for machine in machines:
    print("Machine:", machine)
