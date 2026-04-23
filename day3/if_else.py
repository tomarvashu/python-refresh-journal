# Day 3 - Conditions Practice

ticket_status = "Pending"
pending_tickets = 12

if ticket_status == "Pending" and pending_tickets > 10:
    print("High pending workload")
elif ticket_status == "Pending":
    print("Pending tickets are manageable")
else:
    print("No pending issue")

service_closure_rate = 82

if service_closure_rate >= 90:
    print("Excellent closure rate")
elif service_closure_rate >= 80:
    print("Good closure rate")
else:
    print("Need improvement")
