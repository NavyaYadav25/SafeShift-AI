def generate_reasoning(exception, service):

    observation = ""
    analysis = ""
    hypothesis = ""
    confidence = "80%"

    if "ZeroDivision" in exception:

        observation = (
            "Arithmetic exception detected in service execution."
        )

        analysis = (
            "The application attempted a division operation "
            "using a zero denominator."
        )

        hypothesis = (
            "Input validation was missing before the calculation."
        )

        confidence = "92%"

    elif "Connection" in exception:

        observation = (
            "Database connectivity failure detected."
        )

        analysis = (
            "The service could not establish a connection "
            "to a required dependency."
        )

        hypothesis = (
            "Network timeout or invalid credentials."
        )

        confidence = "89%"

    elif "Memory" in exception:

        observation = (
            "Abnormal memory consumption detected."
        )

        analysis = (
            "Memory usage exceeded safe operating limits."
        )

        hypothesis = (
            "Potential memory leak or infinite processing loop."
        )

        confidence = "87%"

    return {
        "observation": observation,
        "analysis": analysis,
        "hypothesis": hypothesis,
        "confidence": confidence
    }