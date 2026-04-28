# Day 6 - Writing to a File

report_text = "Daily service review completed. Pending tickets need follow-up."

with open("daily_report.txt", "w") as file:
    file.write(report_text)

print("Report written successfully.")
