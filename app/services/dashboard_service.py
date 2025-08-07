# app/services/dashboard_service.py
import json

def get_cached_dashboard_data(r):
    cache_key = "dashboard-data"
    cached_data = r.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    # Mock data for demo
    fresh_data = {
        "total_courses": 10,
        "total_students": 120,
        "active_users_today": 150,
        "new_registrations": [
            {"date": "2025-08-01", "count": 5},
            {"date": "2025-08-02", "count": 8},
            {"date": "2025-08-03", "count": 12},
            {"date": "2025-08-04", "count": 6},
            {"date": "2025-08-05", "count": 10},
        ],
        "top_courses": [
            {"name": "Python Basics", "enrollments": 40},
            {"name": "React for Beginners", "enrollments": 35},
            {"name": "Data Science 101", "enrollments": 30},
            {"name": "UI/UX Design", "enrollments": 25},
            {"name": "Machine Learning", "enrollments": 20}
        ]
    }

    r.set(cache_key, json.dumps(fresh_data), ex=60)
    return fresh_data
