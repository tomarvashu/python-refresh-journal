# Day 4 - Function Practice

def calculate_total(values):
    total = 0
    for value in values:
        total += value
    return total


def calculate_average(values):
    if len(values) == 0:
        return 0
    return calculate_total(values) / len(values)


def find_highest(values):
    if len(values) == 0:
        return None

    highest = values[0]
    for value in values:
        if value > highest:
            highest = value
    return highest


weekly_ticket_counts = [18, 22, 19, 25, 20]

print("Total tickets:", calculate_total(weekly_ticket_counts))
print("Average tickets:", calculate_average(weekly_ticket_counts))
print("Highest tickets:", find_highest(weekly_ticket_counts))
