# Day 4 - Mini Exercise: Service Summary

def calculate_closure_rate(closed, total):
    if total == 0:
        return 0
    return round((closed / total) * 100, 2)


def get_status(rate):
    if rate >= 90:
        return "Strong"
    elif rate >= 75:
        return "Good"
    else:
        return "Needs Attention"


def generate_service_summary(branch, closed, total):
    rate = calculate_closure_rate(closed, total)
    status = get_status(rate)
    return f"{branch}: {closed}/{total} tickets closed | Closure Rate: {rate}% | Status: {status}"


print(generate_service_summary("Delhi", 82, 100))
print(generate_service_summary("Chennai", 45, 60))
print(generate_service_summary("Bangalore", 30, 50))
