# Day 5 - Dictionary Practice with Branch Records

branch = {
    "name": "Delhi",
    "total_tickets": 100,
    "closed_tickets": 82,
    "pending_tickets": 18
}

closure_rate = (branch["closed_tickets"] / branch["total_tickets"]) * 100

print("Branch:", branch["name"])
print("Total Tickets:", branch["total_tickets"])
print("Closed Tickets:", branch["closed_tickets"])
print("Pending Tickets:", branch["pending_tickets"])
print("Closure Rate:", closure_rate)

if closure_rate >= 90:
    print("Status: Excellent")
elif closure_rate >= 80:
    print("Status: Good")
else:
    print("Status: Needs Attention")
