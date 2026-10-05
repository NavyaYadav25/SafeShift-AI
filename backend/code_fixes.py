def generate_code_fix(exception):

    if exception == "ZeroDivisionError":
        return {
            "old_code": """
result = total / count
""",
            "new_code": """
if count != 0:
    result = total / count
else:
    result = 0
"""
        }

    if exception == "ConnectionError":
        return {
            "old_code": """
db.connect()
""",
            "new_code": """
try:
    db.connect()
except:
    reconnect_database()
"""
        }

    if exception == "MemoryError":
        return {
            "old_code": """
while True:
    data.append(item)
""",
            "new_code": """
for item in items:
    process(item)

clear_unused_memory()
"""
        }

    return {
        "old_code": "",
        "new_code": ""
    }