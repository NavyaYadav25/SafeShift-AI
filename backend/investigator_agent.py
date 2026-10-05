def investigate_incident(exception, stack_trace):

    exception = exception.lower()
    stack_trace = stack_trace.lower()

    if "zerodivisionerror" in exception:
        return {
            "root_cause":
            "Application attempted division using a value equal to zero.",
            "severity_score": 8,
            "fix_suggestion":
            "Validate denominator before division."
        }

    elif "connection" in stack_trace:
        return {
            "root_cause":
            "Database connection failure detected.",
            "severity_score": 9,
            "fix_suggestion":
            "Verify database credentials and network."
        }

    elif "memory" in stack_trace:
        return {
            "root_cause":
            "Possible memory leak detected.",
            "severity_score": 10,
            "fix_suggestion":
            "Inspect loops and object allocations."
        }

    return {
        "root_cause":
        "Unknown incident.",
        "severity_score": 5,
        "fix_suggestion":
        "Manual investigation required."
    }