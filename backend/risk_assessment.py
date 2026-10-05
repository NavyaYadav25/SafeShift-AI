def assess_risk(exception):

    if exception == "ZeroDivisionError":
        return {
            "risk_level": "LOW",
            "deployment_recommendation": "Safe for Auto Deployment",
            "confidence": 96
        }

    if exception == "ConnectionError":
        return {
            "risk_level": "MEDIUM",
            "deployment_recommendation": "Human Review Recommended",
            "confidence": 89
        }

    if exception == "MemoryError":
        return {
            "risk_level": "HIGH",
            "deployment_recommendation": "Human Approval Required",
            "confidence": 82
        }

    return {
        "risk_level": "MEDIUM",
        "deployment_recommendation": "Review Required",
        "confidence": 85
    }