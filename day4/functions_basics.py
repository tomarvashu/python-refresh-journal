# Day 4 - Functions Basics

def greet_user(name):
    print("Hello", name)


def show_role(role):
    print("Current role:", role)


greet_user("Vashu")
show_role("Operations & Technology Lead")


def add_numbers(a, b):
    return a + b


total = add_numbers(10, 20)
print("Total:", total)


def calculate_pending(total_tickets, closed_tickets):
    return total_tickets - closed_tickets


pending = calculate_pending(100, 82)
print("Pending tickets:", pending)
