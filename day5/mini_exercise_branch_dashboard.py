# Day 5 - Mini Exercise: Branch Dashboard

branches = [
    {"branch": "Delhi", "total": 100, "closed": 82},
    {"branch": "Chennai", "total": 60, "closed": 50},
    {"branch": "Bangalore", "total": 80, "closed": 70},
    {"branch": "Ludhiana", "total": 40, "closed": 38}
]


def calculate_rate(closed, total):
    if total == 0:
        return 0
    return round((closed / total) * 100, 2)


def classify_branch(rate):
    if rate >= 90:
        return "Strong"
    elif rate >= 80:
        return "Good"
    else:
        return "Needs Attention"


for branch in branches:
    rate = calculate_rate(branch["closed"], branch["total"])
    status = classify_branch(rate)
    print(branch["branch"], "| Closure Rate:", rate, "% | Status:", status)
