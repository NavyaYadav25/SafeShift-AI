def calculate_business_impact(service):

    if service == "checkout-service":
        return {
            "priority": "P1",
            "customer_impact": "High",
            "revenue_risk": "$12,000/hour",
            "users_affected": 15000,
            "escalation_risk": "HIGH",
            "downtime_cost": "$720,000/day"
        }

    if service == "db-service":
        return {
            "priority": "P1",
            "customer_impact": "High",
            "revenue_risk": "$8,000/hour",
            "users_affected": 10000,
            "escalation_risk": "HIGH",
            "downtime_cost": "$480,000/day"
        }

    if service == "analytics-service":
        return {
            "priority": "P3",
            "customer_impact": "Low",
            "revenue_risk": "$3,000/hour",
            "users_affected": 2000,
            "escalation_risk": "LOW",
            "downtime_cost": "$72,000/day"
        }

    return {
        "priority": "P2",
        "customer_impact": "Medium",
        "revenue_risk": "$5,000/hour",
        "users_affected": 5000,
        "escalation_risk": "MEDIUM",
        "downtime_cost": "$120,000/day"
    }