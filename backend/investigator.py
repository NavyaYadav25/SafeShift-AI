def investigate_incident(exception, stack_trace):

    if "ZeroDivisionError" in exception:

        return {
            "root_cause":
            "Application attempted division using a value equal to zero."
        }

    if "KeyError" in exception:

        return {
            "root_cause":
            "Application tried to access a dictionary key that does not exist."
        }

    if "TypeError" in exception:

        return {
            "root_cause":
            "Application used incompatible data types."
        }

    return {
        "root_cause":
        f"Unknown exception detected: {exception}"
    }