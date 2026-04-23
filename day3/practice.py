# Day 3 - Mixed Practice

tickets_closed = [5, 8, 6, 10]
total_closed = 0

for ticket_count in tickets_closed:
    total_closed += ticket_count

print("Total closed tickets:", total_closed)

if total_closed >= 25:
    print("Strong performance")
else:
    print("Needs more effort")
