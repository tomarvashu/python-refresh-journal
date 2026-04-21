# Day 2 - Tuples and Sets Practice

branch_codes = ("DEL", "CHE", "BLR")
print("Branch codes tuple:", branch_codes)
print("First branch:", branch_codes[0])

models = {"JK-900", "JK-900", "A4", "A4B", "JK-900"}
print("Unique models:", models)
print("Number of unique models:", len(models))

models.add("JTK")
print("After add:", models)

models.discard("A4")
print("After discard:", models)
