def generate_fix(exception, file_name):

    reasoning_steps = []

    confidence_score = "75%"
    suggested_fix = "Manual investigation required."

    if "ZeroDivision" in exception:

        reasoning_steps.append(
            "Detected arithmetic operation failure."
        )

        reasoning_steps.append(
            "Potential denominator value equals zero."
        )

        reasoning_steps.append(
            "Input validation required before division."
        )

        suggested_fix = """
if cart_total != 0:
    return discount / cart_total
else:
    return 0
"""

        confidence_score = "92%"

    elif "Connection" in exception:

        reasoning_steps.append(
            "Detected service connectivity issue."
        )

        reasoning_steps.append(
            "Database or network timeout suspected."
        )

        reasoning_steps.append(
            "Retry and reconnection strategy recommended."
        )

        suggested_fix = """
try:
    db.connect()
except:
    reconnect_database()
"""

        confidence_score = "89%"

    elif "Memory" in exception:

        reasoning_steps.append(
            "Memory usage exceeded threshold."
        )

        reasoning_steps.append(
            "Potential infinite loop or leak detected."
        )

        reasoning_steps.append(
            "Resource cleanup required."
        )

        suggested_fix = """
clear_unused_memory()
restart_worker()
"""

        confidence_score = "86%"

    return {
        "suggested_fix": suggested_fix,
        "confidence_score": confidence_score,
        "reasoning_steps": reasoning_steps
    }