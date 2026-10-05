def diagnose(exception):

    if exception == "ZeroDivisionError":
        return {
            "agent": "Diagnosis Agent",
            "status": "Completed",
            "root_cause":
            "Application attempted division using a value equal to zero."
        }

    if exception == "ConnectionError":
        return {
            "agent": "Diagnosis Agent",
            "status": "Completed",
            "root_cause":
            "Database connection failure detected."
        }

    if exception == "MemoryError":
        return {
            "agent": "Diagnosis Agent",
            "status": "Completed",
            "root_cause":
            "Possible memory leak detected."
        }

    return {
        "agent": "Diagnosis Agent",
        "status": "Completed",
        "root_cause":
        "Unknown root cause."
    }