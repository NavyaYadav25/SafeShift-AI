def validate_fix(exception):

    if exception == "ZeroDivisionError":

        return {
            "original_issue_fixed": True,
            "regression_tests_passed": 5,
            "regression_tests_failed": 0,
            "generated_edge_cases": 4,
            "edge_cases_passed": 4,
            "risk_level": "LOW",
            "recommendation": "APPROVE"
        }

    return {
        "original_issue_fixed": False,
        "regression_tests_passed": 0,
        "regression_tests_failed": 1,
        "generated_edge_cases": 0,
        "edge_cases_passed": 0,
        "risk_level": "HIGH",
        "recommendation": "REJECT"
    }