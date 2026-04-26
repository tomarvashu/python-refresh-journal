# Day 5 - Dictionaries Basics

employee = {
    "name": "Vashu",
    "role": "Operations & Technology Lead",
    "department": "Operations & Technology"
}

print("Employee:", employee)
print("Name:", employee["name"])
print("Role:", employee["role"])

employee["location"] = "New Delhi"
print("After adding location:", employee)

employee["role"] = "Manager - Operations & Technology"
print("After updating role:", employee)

print("Department using get:", employee.get("department"))
print("Salary using get:", employee.get("salary", "Not available"))
