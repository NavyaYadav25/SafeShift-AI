def calculate_metrics(total_incidents):

    revenue_saved = total_incidents * 12000 * 24

    engineer_hours_saved = total_incidents * 8

    success_rate = 96

    return {
        "revenue_saved": revenue_saved,
        "engineer_hours_saved": engineer_hours_saved,
        "success_rate": success_rate
    }