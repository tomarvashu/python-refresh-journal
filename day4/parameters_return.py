# Day 4 - Parameters and Return Practice

def calculate_closure_rate(closed_tickets, total_tickets):
    if total_tickets == 0:
        return 0
    return (closed_tickets / total_tickets) * 100


closure_rate = calculate_closure_rate(82, 100)
print("Closure rate:", closure_rate)


def classify_performance(closure_rate):
    if closure_rate >= 90:
        return "Excellent"
    elif closure_rate >= 80:
        return "Good"
    else:
        return "Needs Improvement"


performance = classify_performance(closure_rate)
print("Performance:", performance)


def create_summary(branch_name, closure_rate, performance):
    return f"{branch_name} has a closure rate of {closure_rate}% and performance is {performance}."


summary = create_summary("Delhi", closure_rate, performance)
print(summary)
