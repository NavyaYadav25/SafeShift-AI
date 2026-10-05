def generate_recovery_plan(exception):

    if exception == "ZeroDivisionError":
        return [
            "Locate division operation",
            "Validate denominator value",
            "Add input validation",
            "Run unit tests",
            "Deploy fix after approval"
        ]

    if exception == "ConnectionError":
        return [
            "Verify database credentials",
            "Check database connectivity",
            "Restart connection pool",
            "Run health checks",
            "Monitor for 15 minutes"
        ]

    if exception == "MemoryError":
        return [
            "Identify memory-consuming process",
            "Inspect loops and allocations",
            "Release unused objects",
            "Restart affected service",
            "Monitor memory usage"
        ]

    return [
        "Investigate logs",
        "Identify root cause",
        "Create fix",
        "Test solution",
        "Deploy after approval"
    ]