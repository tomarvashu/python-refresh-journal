# Day 6 - Appending to a File

new_update = "\nSecond update: Follow-up assigned to service team."

with open("daily_report.txt", "a") as file:
    file.write(new_update)

print("Update appended successfully.")
