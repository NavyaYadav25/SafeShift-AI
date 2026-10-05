def generate_fix(exception):

    if exception == "ZeroDivisionError":
        return {
            "agent": "Fix Agent",
            "status": "Completed",
            "fix":
            "Validate denominator before division.",
            "severity_score": 8
        }

    if exception == "ConnectionError":
        return {
            "agent": "Fix Agent",
            "status": "Completed",
            "fix":
            "Verify database credentials and network.",
            "severity_score": 9
        }

    if exception == "MemoryError":
        return {
            "agent": "Fix Agent",
            "status": "Completed",
            "fix":
            "Inspect loops and object allocations.",
            "severity_score": 10
        }

    return {
        "agent": "Fix Agent",
        "status": "Completed",
        "fix":
        "Manual investigation required.",
        "severity_score": 5
    }