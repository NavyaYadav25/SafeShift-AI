def get_agent_activity(exception):

    if exception == "ZeroDivisionError":
        return [
            {
                "agent": "Investigator Agent",
                "status": "Completed",
                "output": "Root cause isolated in checkout-service"
            },
            {
                "agent": "Diagnosis Agent",
                "status": "Completed",
                "output": "ZeroDivisionError confirmed"
            },
            {
                "agent": "Fix Agent",
                "status": "Completed",
                "output": "Patch generated and validated"
            },
            {
                "agent": "Approval Agent",
                "status": "Awaiting Approval",
                "output": "Low risk deployment"
            }
        ]

    if exception == "ConnectionError":
        return [
            {
                "agent": "Investigator Agent",
                "status": "Completed",
                "output": "Database connectivity issue found"
            },
            {
                "agent": "Diagnosis Agent",
                "status": "Completed",
                "output": "Connection timeout confirmed"
            },
            {
                "agent": "Fix Agent",
                "status": "Completed",
                "output": "Reconnect strategy generated"
            },
            {
                "agent": "Approval Agent",
                "status": "Awaiting Approval",
                "output": "Medium risk deployment"
            }
        ]

    return [
        {
            "agent": "Investigator Agent",
            "status": "Completed",
            "output": "Memory leak pattern detected"
        },
        {
            "agent": "Diagnosis Agent",
            "status": "Completed",
            "output": "MemoryError validated"
        },
        {
            "agent": "Fix Agent",
            "status": "Completed",
            "output": "Memory optimization patch generated"
        },
        {
            "agent": "Approval Agent",
            "status": "Awaiting Approval",
            "output": "High risk deployment"
        }
    ]