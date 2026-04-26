# Day 5 - Dictionary Practice

service_records = [
    {"branch": "Delhi", "total": 100, "closed": 82},
    {"branch": "Chennai", "total": 60, "closed": 50},
    {"branch": "Bangalore", "total": 80, "closed": 70},
    {"branch": "Ludhiana", "total": 40, "closed": 38}
]

for record in service_records:
    rate = round((record["closed"] / record["total"]) * 100, 2)
    record["closure_rate"] = rate

print(service_records)

for record in service_records:
    print(record["branch"], "-", record["closure_rate"], "%")
